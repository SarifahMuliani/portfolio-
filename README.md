# Sarifah Muliani — Portfolio

A one-page portfolio site, generated with **Python + Jinja2** from `data.json`.
The design theme riffs on image annotation / dataset labeling (LabelMe-style
bounding boxes and class tags) since that's real work Sarifah does.

## How it's built

- `data.json` — all the content (name, experience, projects, skills...). Edit this to update the site.
- `templates/index.html.j2` — the Jinja2 HTML template + all CSS.
- `static/script.js` — small scroll-reveal script.
- `generate.py` — reads `data.json`, renders the template, writes `index.html` (and copies `script.js`) to the repo root.

## 1. Generate the site

```bash
pip install -r requirements.txt
python generate.py
```

This creates `index.html` + `script.js` at the repo root. Open `index.html`
in a browser to preview locally.

**Before you publish**, open `data.json` and fill in your real links:

```json
"links": {
  "LinkedIn": "https://linkedin.com/in/your-handle",
  "GitHub": "https://github.com/your-handle",
  "Kaggle": "https://kaggle.com/your-handle"
}
```
Then re-run `python generate.py`.

## 2. Push to GitHub

```bash
git init
git add .
git commit -m "Initial portfolio site"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

(Create the empty repo on GitHub first at https://github.com/new — don't
initialize it with a README there, since this folder already has one.)

## 3. Turn on GitHub Pages

1. On GitHub, go to your repo → **Settings → Pages**.
2. Under **Build and deployment → Source**, choose **Deploy from a branch**.
3. Branch: `main`, folder: `/ (root)` → **Save**.
4. Wait a minute, then your site is live at:
   `https://<your-username>.github.io/<repo-name>/`

## Updating later

Edit `data.json` (add a job, a project, a skill...), run `python generate.py`
again, then:

```bash
git add .
git commit -m "Update portfolio content"
git push
```

GitHub Pages redeploys automatically within a minute or two.
