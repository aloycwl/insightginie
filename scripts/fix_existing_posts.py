import os
import re

POST_DIR = "../_posts"


def fix_file(path):

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # remove raw blocks
    content = content.replace("{% raw %}", "")
    content = content.replace("{% endraw %}", "")

    # remove remaining liquid tags
    content = re.sub(r"\{%.+?%\}", "", content)

    # remove double blank lines
    content = re.sub(r"\n{3,}", "\n\n", content)

    if content != original:

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        print("fixed:", path)


def main():

    for root, dirs, files in os.walk(POST_DIR):

        for file in files:

            if file.endswith(".md"):

                path = os.path.join(root, file)

                fix_file(path)


if __name__ == "__main__":
    main()