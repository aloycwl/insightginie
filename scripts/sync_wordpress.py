import requests
import os
import json
import subprocess
import time
import re

from pathlib import Path
from urllib.parse import urlparse
from markdownify import markdownify as md
from concurrent.futures import ThreadPoolExecutor

# CONFIG
SITE = "https://insightginie.com"
API = f"{SITE}/wp-json/wp/v2/posts"

POST_DIR = "../posts"
MEDIA_DIR = "../media/images"
INDEX_FILE = "../index/posts.json"

PER_PAGE = 100
THREADS = 10

os.makedirs(POST_DIR, exist_ok=True)
os.makedirs(MEDIA_DIR, exist_ok=True)
os.makedirs("../index", exist_ok=True)

# load index
if os.path.exists(INDEX_FILE):
    with open(INDEX_FILE) as f:
        index = json.load(f)
else:
    index = {}

def fetch_posts():

    posts = []
    page = 1

    while True:

        url = f"{API}?per_page={PER_PAGE}&page={page}"

        r = requests.get(url)

        if r.status_code != 200:
            break

        data = r.json()

        if not data:
            break

        posts.extend(data)

        print("Fetched page", page)

        page += 1

    return posts


def download_image(url):

    filename = os.path.basename(urlparse(url).path)
    filepath = os.path.join(MEDIA_DIR, filename)

    if os.path.exists(filepath):
        return filename

    try:

        r = requests.get(url, timeout=10)

        if r.status_code == 200:

            with open(filepath, "wb") as f:
                f.write(r.content)

            print("Downloaded", filename)

    except:
        pass

    return filename


def process_images(content):

    urls = re.findall(r'https?://[^"]+\.(jpg|jpeg|png|webp)', content)

    if not urls:
        return content

    with ThreadPoolExecutor(max_workers=THREADS) as executor:

        results = list(executor.map(download_image, urls))

    for url, filename in zip(urls, results):

        content = content.replace(url, f"/media/images/{filename}")

    return content


def convert_post(post):

    slug = post["slug"]
    title = post["title"]["rendered"]
    content = post["content"]["rendered"]

    date = post["date"]
    modified = post["modified"]

    categories = post["categories"]

    # simple fallback
    category = "uncategorized"
    subcategory = ""

    if categories:
        category = str(categories[0])

    path = f"{POST_DIR}/{category}/{subcategory}"
    Path(path).mkdir(parents=True, exist_ok=True)

    content = process_images(content)

    markdown = md(content)

    final = f"""# {title}

Original article: {SITE}/{slug}

Published: {date}

---

{markdown}

---

Source: {SITE}/{slug}
"""

    with open(f"{path}/{slug}.md", "w", encoding="utf-8") as f:
        f.write(final)

    index[slug] = modified

    print("Saved", slug)


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

    posts = fetch_posts()

    print("Total posts:", len(posts))

    with ThreadPoolExecutor(max_workers=THREADS) as executor:

        executor.map(process_post, posts)

    with open(INDEX_FILE, "w") as f:
        json.dump(index, f, indent=2)

    git_commit()


if __name__ == "__main__":
    main()