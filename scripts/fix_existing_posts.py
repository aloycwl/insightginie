import os
import re
import json
import requests
from pathlib import Path

SITE = "https://insightginie.com"
CATEGORY_API = f"{SITE}/wp-json/wp/v2/categories"

POST_DIR = "../_posts"


def fetch_categories():

    categories = {}
    page = 1

    while True:

        url = f"{CATEGORY_API}?per_page=100&page={page}"

        r = requests.get(url)

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


def resolve_category_path(cat_id, categories):

    path = []

    while cat_id in categories:

        c = categories[cat_id]

        path.append(c["slug"])

        if c["parent"] == 0:
            break

        cat_id = c["parent"]

    path.reverse()

    return path


def sanitize(content):

    # fix smart quotes in include tags
    content = content.replace("‘", "'").replace("’", "'")

    # escape include
    content = re.sub(
        r"\{%\s*include\s+(.+?)\s*%\}",
        r"`{% include \1 %}`",
        content
    )

    # escape liquid variables
    content = content.replace("{{", "`{{")
    content = content.replace("}}", "}}`")

    # remove scripts
    content = re.sub(
        r"<script.*?>.*?</script>",
        "",
        content,
        flags=re.DOTALL
    )

    return content


def update_post(path, categories):

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    content = sanitize(content)

    cat_id_match = re.search(r"_posts\/(\d+)", path)

    if cat_id_match:

        cat_id = int(cat_id_match.group(1))

        if cat_id in categories:

            cat_path = resolve_category_path(cat_id, categories)

            new_folder = os.path.join(POST_DIR, *cat_path)

            Path(new_folder).mkdir(parents=True, exist_ok=True)

            new_path = os.path.join(new_folder, os.path.basename(path))

            with open(new_path, "w", encoding="utf-8") as f:
                f.write(content)

            os.remove(path)

            return new_path

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return path


def main():

    categories = fetch_categories()

    fixed = 0

    for root, dirs, files in os.walk(POST_DIR):

        for file in files:

            if file.endswith(".md"):

                path = os.path.join(root, file)

                update_post(path, categories)

                fixed += 1

    print("posts processed:", fixed)


if __name__ == "__main__":
    main()