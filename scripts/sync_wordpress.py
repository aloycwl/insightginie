import requests
import os
import json
import subprocess
import re
from pathlib import Path
from urllib.parse import urlparse
from markdownify import markdownify as md
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

SITE = "https://insightginie.com"

POST_API = f"{SITE}/wp-json/wp/v2/posts"
CATEGORY_API = f"{SITE}/wp-json/wp/v2/categories"

POST_DIR = "../_posts"
MEDIA_DIR = "../media/images"

INDEX_FILE = "../index/posts.json"
SYNC_FILE = "../index/sync.json"

PER_PAGE = 100
THREADS = 10

os.makedirs(POST_DIR, exist_ok=True)
os.makedirs(MEDIA_DIR, exist_ok=True)
os.makedirs("../index", exist_ok=True)


def sanitize(content):

    content = content.replace("‘", "'").replace("’", "'")

    content = re.sub(
        r"\{%\s*include\s+(.+?)\s*%\}",
        r"`{% include \1 %}`",
        content
    )

    content = content.replace("{{", "`{{")
    content = content.replace("}}", "}}`")

    content = re.sub(
        r"<script.*?>.*?</script>",
        "",
        content,
        flags=re.DOTALL
    )

    return content


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


def download_image(url):

    filename = os.path.basename(urlparse(url).path)

    path = os.path.join(MEDIA_DIR, filename)

    if os.path.exists(path):
        return filename

    try:

        r = requests.get(url)

        if r.status_code == 200:

            with open(path, "wb") as f:
                f.write(r.content)

    except:
        pass

    return filename


def process_images(content):

    urls = re.findall(r'https?://[^"]+\.(jpg|jpeg|png|webp)', content)

    if not urls:
        return content

    with ThreadPoolExecutor(max_workers=THREADS) as executor:

        filenames = list(executor.map(download_image, urls))

    for url, name in zip(urls, filenames):

        content = content.replace(url, f"/media/images/{name}")

    return content


def fetch_posts(last_sync):

    posts = []
    page = 1

    while True:

        url = f"{POST_API}?per_page={PER_PAGE}&page={page}&modified_after={last_sync}"

        r = requests.get(url)

        if r.status_code != 200:
            break

        data = r.json()

        if not data:
            break

        posts.extend(data)

        page += 1

    return posts


def convert_post(post, categories):

    slug = post["slug"]

    title = post["title"]["rendered"]
    content = post["content"]["rendered"]

    date = post["date"]

    content = process_images(content)

    markdown = md(content)

    markdown = sanitize(markdown)

    cat_path = ["general"]

    if post["categories"]:

        cat_path = resolve_category(post["categories"][0], categories)

    folder = os.path.join(POST_DIR, *cat_path)

    Path(folder).mkdir(parents=True, exist_ok=True)

    filename = f"{date[:10]}-{slug}.md"

    frontmatter = f"""---
layout: post
title: "{title}"
date: {date}
categories: {cat_path}
original_url: {SITE}/{slug}
---

"""

    with open(os.path.join(folder, filename), "w", encoding="utf-8") as f:

        f.write(frontmatter + markdown)


def main():

    if os.path.exists(SYNC_FILE):

        with open(SYNC_FILE) as f:
            last_sync = json.load(f)["last_sync"]

    else:

        last_sync = "2000-01-01T00:00:00"

    categories = fetch_categories()

    posts = fetch_posts(last_sync)

    print("posts to update:", len(posts))

    with ThreadPoolExecutor(max_workers=THREADS) as executor:

        executor.map(lambda p: convert_post(p, categories), posts)

    with open(SYNC_FILE, "w") as f:

        json.dump({"last_sync": datetime.utcnow().isoformat()}, f)

    subprocess.run(["git", "add", "."])

    subprocess.run(["git", "commit", "-m", "wordpress sync"])

    subprocess.run(["git", "pull", "--rebase"])

    subprocess.run(["git", "push"])


if __name__ == "__main__":
    main()