import os
import re

POST_DIR = "../_posts"

def sanitize(content):

    # Escape liquid include
    content = re.sub(
        r"\{%\s*include\s+(.+?)\s*%\}",
        r"`{% include \1 %}`",
        content
    )

    # Escape liquid variables
    content = content.replace("{{", "`{{")
    content = content.replace("}}", "}}`")

    # Remove script tags
    content = re.sub(
        r"<script.*?>.*?</script>",
        "",
        content,
        flags=re.DOTALL
    )

    return content


def fix_file(path):

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = sanitize(content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():

    fixed = 0

    for root, dirs, files in os.walk(POST_DIR):

        for file in files:

            if file.endswith(".md"):

                path = os.path.join(root, file)

                fix_file(path)

                fixed += 1

    print("posts fixed:", fixed)


if __name__ == "__main__":
    main()