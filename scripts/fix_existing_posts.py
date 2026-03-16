import os
import re
import requests
import yaml
from pathlib import Path

SITE = "https://insightginie.com"
CATEGORY_API = f"{SITE}/wp-json/wp/v2/categories"

POST_DIR = "../_posts"


# --------------------------
# Fetch WordPress categories
# --------------------------

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


# --------------------------
# Resolve category hierarchy
# --------------------------

def resolve_category(cat_id, categories):

    path = []

    while cat_id in categories:

        c = categories[cat_id]

        path.append(c["slug"])

        if c["parent"] == 0:
            break

        cat_id = c["parent"]

    path.reverse()

    return path


# --------------------------
# Convert category IDs
# --------------------------

def convert_categories(frontmatter, categories):

    cat_ids = frontmatter.get("categories", [])

    if not cat_ids:
        return ["general"]

    first = cat_ids[0]

    # Already slug
    if isinstance(first, str):
        return cat_ids

    # Convert ID -> slug
    if first in categories:
        return resolve_category(first, categories)

    return ["general"]


# --------------------------
# Process a single post
# --------------------------

def process_post(path, categories):

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    parts = text.split("---")

    if len(parts) < 3:
        return

    frontmatter = yaml.safe_load(parts[1])
    content = parts[2]

    new_categories = convert_categories(frontmatter, categories)

    frontmatter["categories"] = new_categories

    new_front = yaml.dump(frontmatter, sort_keys=False)

    new_text = f"---\n{new_front}---\n{content}"

    # new folder based on slug categories
    new_folder = os.path.join(POST_DIR, *new_categories)

    Path(new_folder).mkdir(parents=True, exist_ok=True)

    new_path = os.path.join(new_folder, os.path.basename(path))

    with open(new_path, "w", encoding="utf-8") as f:
        f.write(new_text)

    if new_path != path:
        os.remove(path)


# --------------------------
# Remove numeric folders
# --------------------------

def cleanup_numeric_folders():

    for name in os.listdir(POST_DIR):

        full = os.path.join(POST_DIR, name)

        if os.path.isdir(full) and name.isdigit():

            print("removing numeric folder:", name)

            for root, dirs, files in os.walk(full):

                for file in files:

                    os.remove(os.path.join(root, file))

            os.rmdir(full)


# --------------------------
# Main
# --------------------------

def main():

    categories = fetch_categories()

    total = 0

    for root, dirs, files in os.walk(POST_DIR):

        for file in files:

            if file.endswith(".md"):

                path = os.path.join(root, file)

                process_post(path, categories)

                total += 1

    cleanup_numeric_folders()

    print("posts processed:", total)


if __name__ == "__main__":
    main()