import os
import re

POST_DIR = "../_posts"


def wrap_liquid(content):

    # wrap liquid include blocks
    content = re.sub(
        r"(\{%\s*include.*?%\})",
        r"{% raw %}\1{% endraw %}",
        content
    )

    # wrap liquid variable blocks
    content = re.sub(
        r"(\{\{.*?\}\})",
        r"{% raw %}\1{% endraw %}",
        content
    )

    return content


def remove_scripts(content):

    content = re.sub(
        r"<script.*?>.*?</script>",
        "",
        content,
        flags=re.DOTALL
    )

    return content


def normalize_quotes(content):

    content = content.replace("‘", "'")
    content = content.replace("’", "'")

    return content


def fix_post(path):

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    content = normalize_quotes(content)

    content = remove_scripts(content)

    content = wrap_liquid(content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main():

    count = 0

    for root, dirs, files in os.walk(POST_DIR):

        for file in files:

            if file.endswith(".md"):

                path = os.path.join(root, file)

                fix_post(path)

                count += 1

    print("posts fixed:", count)


if __name__ == "__main__":
    main()