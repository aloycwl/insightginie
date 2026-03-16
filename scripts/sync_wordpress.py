import requests
import os
import json
import subprocess
import re
from urllib.parse import urlparse
from pathlib import Path
from markdownify import markdownify as md
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

SITE = "https://insightginie.com"
API = f"{SITE}/wp-json/wp/v2/posts"

PER_PAGE = 100
THREADS = 10

POST_DIR = "../_posts"
MEDIA_DIR = "../media/images"

INDEX_FILE = "../index/posts.json"
SYNC_FILE = "../index/sync.json"

os.makedirs(POST_DIR, exist_ok=True)
os.makedirs(MEDIA_DIR, exist_ok=True)
os.makedirs("../index", exist_ok=True)

if os.path.exists(INDEX_FILE):
    with open(INDEX_FILE) as f:
        index = json.load(f)
else:
    index = {}

def get_last_sync():

    if not os.path.exists(SYNC_FILE):
        return "2000-01-01T00:00:00"

    with open(SYNC_FILE) as f:
        return json.load(f)["last_sync"]


def save_sync():

    now = datetime.utcnow().isoformat()

    with open(SYNC_FILE, "w") as f:
        json.dump({"last_sync": now}, f)

def sanitize_markdown(content):

    import re

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


def fetch_posts(last_sync):

    posts = []
    page = 1

    while True:

        url = f"{API}?per_page={PER_PAGE}&page={page}&modified_after={last_sync}"

        r = requests.get(url)

        if r.status_code != 200:
            break

        data = r.json()

        if not data:
            break

        posts.extend(data)

        page += 1

    return posts


def download_image(url):

    filename = os.path.basename(urlparse(url).path)
    path = os.path.join(MEDIA_DIR, filename)

    if os.path.exists(path):
        return filename

    try:

        r = requests.get(url, timeout=10)

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

    for url, filename in zip(urls, filenames):

        content = content.replace(url, f"/media/images/{filename}")

    return content


def convert_post(post):

    slug = post["slug"]

    title = post["title"]["rendered"]
    content = post["content"]["rendered"]

    date = post["date"]
    modified = post["modified"]

    categories = post["categories"]

    category = "general"
    subcategory = ""

    if categories:
        category = str(categories[0])

    content = process_images(content)

    markdown = sanitize_markdown(md(content))

    folder = f"{POST_DIR}/{category}/{subcategory}"

    Path(folder).mkdir(parents=True, exist_ok=True)

    filename = f"{date[:10]}-{slug}.md"

    frontmatter = f"""---
layout: post
title: "{title}"
date: {date}
categories: [{category}]
original_url: {SITE}/{slug}
---

"""

    final = frontmatter + markdown

    with open(f"{folder}/{filename}", "w", encoding="utf-8") as f:
        f.write(final)

    index[slug] = modified

    print("saved", slug)


def process_post(post):

    slug = post["slug"]
    modified = post["modified"]

    if slug in index and index[slug] == modified:
        return

    convert_post(post)


def git_commit():

    subprocess.run(["git", "add", "."])

    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True)

    if result.stdout:

        subprocess.run(["git", "commit", "-m", "wordpress sync"])
        subprocess.run(["git", "push"])


def main():

    last_sync = get_last_sync()

    posts = fetch_posts(last_sync)

    print("posts to update:", len(posts))

    with ThreadPoolExecutor(max_workers=THREADS) as executor:

        executor.map(process_post, posts)

    with open(INDEX_FILE, "w") as f:
        json.dump(index, f, indent=2)

    save_sync()

    git_commit()


if __name__ == "__main__":
    main()