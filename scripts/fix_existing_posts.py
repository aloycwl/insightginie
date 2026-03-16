import re
from pathlib import Path
from datetime import datetime, timedelta

BASE_DIR = Path(__file__).resolve().parent.parent
POST_DIR = BASE_DIR / "_posts"

SGT_OFFSET = timedelta(hours=8)

date_pattern = re.compile(r"date:\s*['\"]?([0-9T:\-]+)['\"]?")

def convert_date(date_str):
    dt = datetime.fromisoformat(date_str)
    dt_utc = dt - SGT_OFFSET
    return dt_utc.replace(microsecond=0).isoformat()

def fix_file(path):
    text = path.read_text(encoding="utf-8")

    match = date_pattern.search(text)
    if not match:
        return False

    old_date = match.group(1)

    try:
        new_date = convert_date(old_date)
    except Exception:
        return False

    new_text = text.replace(
        f"date: '{old_date}'",
        f"date: '{new_date}'"
    )

    path.write_text(new_text, encoding="utf-8")

    print("fixed:", path.name, old_date, "→", new_date)
    return True

def run():

    count = 0

    for file in POST_DIR.rglob("*.md"):
        if fix_file(file):
            count += 1

    print("\nupdated", count, "posts")

if __name__ == "__main__":
    run()
