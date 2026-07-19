#!/usr/bin/env python3
"""
Portfolio site generator.

Reads content from data.json, renders templates/index.html.j2, and writes a
static, ready-to-deploy index.html (+ script.js) to the repo root so it can
be pushed straight to GitHub and served with GitHub Pages.

Usage:
    pip install -r requirements.txt
    python generate.py
"""
import json
import shutil
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).parent
TEMPLATES_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"
DATA_FILE = ROOT / "data.json"
OUTPUT_HTML = ROOT / "index.html"


def load_data() -> dict:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    data["year"] = date.today().year
    return data


def render_html(data: dict) -> str:
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    template = env.get_template("index.html.j2")
    return template.render(**data)


def main():
    data = load_data()
    html = render_html(data)

    OUTPUT_HTML.write_text(html, encoding="utf-8")
    print(f"Wrote {OUTPUT_HTML.relative_to(ROOT)}")

    # Copy static assets (script.js, images/, etc.) next to index.html so
    # relative paths in the template resolve correctly on GitHub Pages.
    for asset in STATIC_DIR.iterdir():
        dest = ROOT / asset.name
        if asset.is_dir():
            shutil.copytree(asset, dest, dirs_exist_ok=True)
            print(f"Copied {asset.name}/")
        elif asset.is_file():
            shutil.copy(asset, dest)
            print(f"Copied {asset.name}")

    print("\nDone. Open index.html in a browser to preview, "
          "or push this folder to GitHub and enable Pages.")


if __name__ == "__main__":
    main()
