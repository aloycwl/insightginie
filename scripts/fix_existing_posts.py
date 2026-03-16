import os
import re
import requests
import yaml
from pathlib import Path

SITE = "https://insightginie.com"

CATEGORY_API = f"{SITE}/wp-json/wp/v2/categories"
POST_API = f"{SITE}/wp-json/wp/v2/posts"

POST_DIR = "../_posts"
MEDIA_DIR = "../media/images"

os.makedirs(MEDIA_DIR, exist_ok=True)


# ---------------------------
# Fetch WordPress categories
# ---------------------------

def fetch_categories():

    categories = {}
    page = 1

    while True:

        r = requests.get(f"{CATEGORY_API}?per_page=100&page={page}")

        if r.status_code != 200:
            break

        data = r.json()

        if not data:
            break

        for c in data:

            categories[c["id"]] = {
                "slug": c["slug"],
                "parent": c["parent"]
            }

        page += 1

    return categories


# ---------------------------
# Resolve category hierarchy
# ---------------------------

def resolve_category(cat_id, categories):

    parts = []

    while cat_id in categories:

        c = categories[cat_id]

        parts.append(c["slug"])

        if c["parent"] == 0:
            break

        cat_id = c["parent"]

    parts.reverse()

    return parts


# ---------------------------
# Fetch featured image
# ---------------------------

def fetch_featured_image(slug):

    r = requests.get(f"{POST_API}?slug={slug}")

    if r.status_code != 200:
        return None

    posts = r.json()

    if not posts:
        return None

    media_id = posts[0]["featured_media"]

    if not media_id:
        return None

    media = requests.get(f"{SITE}/wp-json/wp/v2/media/{media_id}")

    if media.status_code != 200:
        return None

    url = media.json()["source_url"]

    filename = url.split("/")[-1]

    local_path = f"{MEDIA_DIR}/{filename}"

    if not os.path.exists(local_path):

        img = requests.get(url)

        with open(local_path, "wb") as f:
            f.write(img.content)

    return f"/media/images/{filename}"


# ---------------------------
# Fix liquid syntax
# ---------------------------

def sanitize(content):

    content = content.replace("‘", "'").replace("’", "'")

    content = re.sub(
        r"(\{%\s*include.*?%\})",
        r"{% raw %}\1{% endraw %}",
        content
    )

    content = re.sub(
        r"(\{\{.*?\}\})",
        r"{% raw %}\1{% endraw %}",
        content
    )

    content = re.sub(
        r"<script.*?>.*?</script>",
        "",
        content,
        flags=re.DOTALL
    )

    return content


# ---------------------------
# Process a single post
# ---------------------------

def process_post(path, categories):

    with open(path, "r", encoding="utf-8") as f:

        text = f.read()

    parts = text.split("---")

    if len(parts) < 3:
        return

    frontmatter = yaml.safe_load(parts[1])
    content = parts[2]

    slug = frontmatter.get("original_url", "").split("/")[-1]

    # fix liquid
    content = sanitize(content)

    # convert category ID → slug
    cat_ids = frontmatter.get("categories", [])

    if cat_ids and isinstance(cat_ids[0], int):

        cat_path = resolve_category(cat_ids[0], categories)

        frontmatter["categories"] = cat_path

    else:

        cat_path = frontmatter.get("categories", ["general"])

    # fetch featured image
    if "featured_image" not in frontmatter:

        img = fetch_featured_image(slug)

        if img:
            frontmatter["featured_image"] = img

    # rebuild markdown
    new_front = yaml.dump(frontmatter, sort_keys=False)

    new_text = f"---\n{new_front}---\n{content}"

    folder = os.path.join(POST_DIR, *cat_path)

    Path(folder).mkdir(parents=True, exist_ok=True)

    new_path = os.path.join(folder, os.path.basename(path))

    with open(new_path, "w", encoding="utf-8") as f:

        f.write(new_text)

    if new_path != path:
        os.remove(path)


# ---------------------------
# Main
# ---------------------------

def main():

    categories = fetch_categories()

    total = 0

    for root, dirs, files in os.walk(POST_DIR):

        for file in files:

            if file.endswith(".md"):

                path = os.path.join(root, file)

                process_post(path, categories)

                total += 1

    print("processed:", total)


if __name__ == "__main__":
    main()