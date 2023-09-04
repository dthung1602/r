import json
import os
import shutil

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "config.json")
OUTPUT_DIR = os.path.join(BASE_DIR, "docs")
INDEX_FILE = os.path.join(OUTPUT_DIR, "index.html")
INDEX_TEMPLATE_FILE = os.path.join(BASE_DIR, "index-template.html")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="refresh" content="0; url={url}">
</head>
<body></body>
</html>
"""

LINK_TEMPLATE = """
<tr>
    <td>
        <button onclick="copy(this)">Copy</button>
        <a href="{path}">{path}</a>
    </td>
    <td>
        <button onclick="copy(this)">Copy</button>
        <a href="{url}">{url}</a>
    </td>
</tr>
"""


def main():
    print("Start generating HTML files")
    with open(CONFIG_FILE) as f:
        urls = json.load(f)["urls"]

    urls = flatten_dict(urls)

    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)

    index_body = ""

    for original_path, url in urls.items():
        path = os.path.join(OUTPUT_DIR, original_path) + ".htm"
        directory, _ = path.rsplit("/", 1)

        print(f"Generating {path}")

        html_str = HTML_TEMPLATE.format(url=url)
        os.makedirs(directory, exist_ok=True)
        with open(path, "w") as f:
            f.write(html_str)

        index_body += LINK_TEMPLATE.format(url=url, path=original_path + ".htm")

    print("Generating index.html")
    with open(INDEX_TEMPLATE_FILE) as f:
        index_template = f.read()
    with open(INDEX_FILE, "w") as f:
        f.write(index_template % {"body": index_body})

    print("Done!\n")


def flatten_dict(d: dict, parent_key: str = "", sep: str = "/") -> dict:
    """Src: https://www.freecodecamp.org/news/how-to-flatten-a-dictionary-in-python-in-4-different-ways/"""
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


if __name__ == "__main__":
    main()
