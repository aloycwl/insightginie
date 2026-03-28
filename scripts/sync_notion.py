#!/usr/bin/env python3

import json
import re
import time
import urllib.parse
from pathlib import Path
from typing import Any
from urllib import request, error

# -----------------------------
# CONFIG
# -----------------------------
NOTION_API_KEY = "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"
POSTS_DB_ID = "778c4be6ee44828f883c0181a47083d8"
CATEGORIES_DB_ID = "331c4be6ee448024a2fdf32b99d057c0"

BASE_DIR = Path(__file__).resolve().parent.parent
POSTS_DIR = BASE_DIR / "_posts"

NOTION_API_BASE = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

# -----------------------------
# API
# -----------------------------
def notion_request(method: str, path: str, payload: dict[str, Any] | None = None):
    url = f"{NOTION_API_BASE}{path}"
    body = json.dumps(payload).encode("utf-8") if payload else None

    req = request.Request(
        url,
        data=body,
        method=method,
        headers={
            "Authorization": f"Bearer {NOTION_API_KEY}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        },
    )

    for _ in range(5):
        try:
            with request.urlopen(req, timeout=60) as res:
                raw = res.read().decode()
                return json.loads(raw) if raw else {}
        except error.HTTPError as e:
            if e.code == 429:
                time.sleep(2)
                continue
            raise RuntimeError(e.read().decode())

# -----------------------------
# PARSE FRONTMATTER
# -----------------------------
def parse_frontmatter(raw):
    m = re.match(r"\A---\n(.*?)\n---\n?(.*)\Z", raw, re.DOTALL)
    if not m:
        return {}, raw

    fm = {}
    current = None

    for line in m.group(1).splitlines():
        if line.startswith("- ") and current:
            fm.setdefault(current, []).append(line[2:].strip())
        elif ":" in line:
            k, v = line.split(":", 1)
            current = k.strip()
            v = v.strip()
            if not v:
                fm[current] = []
            else:
                fm[current] = v.strip("'\"")

    return fm, m.group(2)

# -----------------------------
# HTML → NOTION BLOCKS
# -----------------------------
def html_to_blocks(content):
    blocks = []

    patterns = re.findall(
        r"<h[1-3][^>]*>.*?</h[1-3]>|<p[^>]*>.*?</p>|<li[^>]*>.*?</li>|<img[^>]*>",
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    for chunk in patterns:
        tag = re.match(r"<\s*([a-zA-Z0-9]+)", chunk)
        text = re.sub(r"<[^>]+>", "", chunk)
        text = re.sub(r"\s+", " ", text).strip()

        if not tag:
            continue

        t = tag.group(1).lower()

        if t == "h1":
            blocks.append({
                "object": "block",
                "type": "heading_1",
                "heading_1": {"rich_text": [{"type": "text", "text": {"content": text}}]}
            })

        elif t == "h2":
            blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {"rich_text": [{"type": "text", "text": {"content": text}}]}
            })

        elif t == "h3":
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {"rich_text": [{"type": "text", "text": {"content": text}}]}
            })

        elif t == "li":
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": text}}]}
            })

        elif t == "img":
            src_match = re.search(r'src="([^"]+)"', chunk)
            if src_match:
                src = src_match.group(1)

                if src.startswith("/image/"):
                    encoded = src.split("/image/")[1].split("?")[0]
                    src = urllib.parse.unquote(encoded)

                if src.startswith("/"):
                    src = f"https://insightginie.com{src}"

                blocks.append({
                    "object": "block",
                    "type": "image",
                    "image": {"type": "external", "external": {"url": src}}
                })

        else:
            if text:
                blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {"rich_text": [{"type": "text", "text": {"content": text}}]}
                })

    return blocks

# -----------------------------
# CATEGORY LOGIC
# -----------------------------
def find_category(name, parent_id=None):
    res = notion_request("POST", f"/databases/{CATEGORIES_DB_ID}/query", {
        "filter": {
            "and": [
                {"property": "Name", "title": {"equals": name}},
                {
                    "property": "Parent",
                    "relation": {"contains": parent_id}
                } if parent_id else {
                    "property": "Parent",
                    "relation": {"is_empty": True}
                }
            ]
        },
        "page_size": 1
    })

    return res["results"][0]["id"] if res["results"] else None


def create_category(name, parent_id=None):
    props = {
        "Name": {"title": [{"text": {"content": name}}]}
    }

    if parent_id:
        props["Parent"] = {"relation": [{"id": parent_id}]}

    res = notion_request("POST", "/pages", {
        "parent": {"database_id": CATEGORIES_DB_ID},
        "properties": props
    })

    return res["id"]


def get_or_create_category_path(cat_list):
    parent_id = None

    for name in cat_list:
        existing = find_category(name, parent_id)

        if existing:
            parent_id = existing
        else:
            parent_id = create_category(name, parent_id)

    return parent_id

# -----------------------------
# POSTS
# -----------------------------
def find_post(slug):
    res = notion_request("POST", f"/databases/{POSTS_DB_ID}/query", {
        "filter": {"property": "Slug", "rich_text": {"equals": slug}},
        "page_size": 1
    })
    return res["results"][0]["id"] if res["results"] else None


def sync_post(path: Path):
    raw = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(raw)

    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)

    title = fm.get("title")
    if isinstance(title, list):
        title = " ".join(title)
    if not title or title == "[]":
        title = slug
    title = str(title).strip()

    date = fm.get("date")
    url = fm.get("original_url", "")

    # CATEGORY FROM FOLDER
    rel_path = path.relative_to(POSTS_DIR)
    parts = rel_path.parts[:-1]
    cats = [p.strip() for p in parts if p.strip()]

    cat_id = get_or_create_category_path(cats) if cats else None

    # IMAGE
    img = fm.get("featured_image")

    if img:
        if img.startswith("/image/"):
            encoded = img.split("/image/")[1].split("?")[0]
            img = urllib.parse.unquote(encoded)

        if img.startswith("/"):
            img = f"https://insightginie.com{img}"

    props = {
        "Name": {"title": [{"text": {"content": title}}]},
        "Slug": {"rich_text": [{"text": {"content": slug}}]}
    }

    if date:
        props["Date"] = {"date": {"start": date}}

    if url:
        props["Source URL"] = {"url": url}

    if cat_id:
        props["Category"] = {"relation": [{"id": cat_id}]}

    if img:
        props["Featured Image"] = {
            "files": [{"name": "img", "external": {"url": img}}]
        }

    blocks = html_to_blocks(body)
    page_id = find_post(slug)

    if page_id:
        notion_request("PATCH", f"/pages/{page_id}", {"properties": props})
        notion_request("PATCH", f"/blocks/{page_id}/children", {"children": blocks})
        print("updated:", slug)
    else:
        notion_request("POST", "/pages", {
            "parent": {"database_id": POSTS_DB_ID},
            "properties": props,
            "children": blocks
        })
        print("created:", slug)

# -----------------------------
# MAIN
# -----------------------------
def main():
    files = sorted(POSTS_DIR.rglob("*.md"))[:5]

    for f in files:
        sync_post(f)

    print("done:", len(files))


if __name__ == "__main__":
    main()