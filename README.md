# willhea.github.io_private

This private repo builds the static site for https://willhea.com using Pelican. The generated site is deployed to the public repo.

- Public: https://github.com/willhea/willhea.github.io  
- Private: https://github.com/willhea/willhea.github.io_private  
- Deployment status: [pages-build-deployment](https://github.com/willhea/willhea.github.io/actions/workflows/pages/pages-build-deployment)

## Quickstart

- Requirements:
  - Python 3.13
  - Make (for local commands)
- Setup:
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Common commands

- Local dev (watch + serve):
```bash
make devserver                     # http://localhost:8000
# or with relative URLs:
make RELATIVE=1 devserver
```

- Local build (dev config):
```bash
make html
```

- Production build (publish config):
```bash
make publish
```

- Serve current build:
```bash
make serve PORT=8000
```

- Clean output:
```bash
make clean
```

- Publish to GitHub Pages (pushes `output/` to `main` via ghp-import):
```bash
make github
```

## Repository layout

- `content/` — Markdown content
  - `pages/` — static pages
  - `drafts/` — drafts (excluded in publish)
  - `extra/robots.txt` — published at `/robots.txt` via `EXTRA_PATH_METADATA`
- `output/` — generated site (ignored)
- `pelicanconf.py` — development config (toggle `RELATIVE_URLS` as needed)
- `publishconf.py` — production config (sets `SITEURL`, enables feeds, excludes drafts)
- `Makefile` — canonical dev/build/publish commands
- `tasks.py` — Invoke-based tasks (alternative to Makefile; optional)
- `.cursor/rules/` — AI/cursor rules and documentation for contributors

## Content conventions

- Timezone: America/New_York; Language: en
- Filenames: `YYYY-MM-DD-slug.md` for articles; short, hyphenated slugs
- Categories/tags: lowercase, hyphenated
- Recommended front matter:
```text
Title: Title Case
Date: 2025-01-31 10:00
Category: blog
Tags: tag1, tag2
Slug: short-hyphenated
Summary: One concise sentence (<= 160 chars).
```

## AI collaboration guidelines

- Do:
  - Focus edits in `content/**` unless asked to modify configuration.
  - Use Make targets (`make devserver`, `make publish`, `make github`).
  - Preserve minimal diffs and existing formatting.
- Avoid:
  - Changing `publishconf.py` `SITEURL` without explicit instruction.
  - Committing `env/` or `output/`.
- See `.cursor/rules/` for detailed project- and Pelican-specific rules.

## How to run and expected outputs

- Local dev (`make devserver`): serves the site with auto-regeneration at `http://localhost:8000`; changes in `content/` reflect after save.
- Local build (`make html`): writes static site to `output/`; open `output/index.html` in a browser.
- Production build (`make publish`): writes a production-optimized site to `output/` (feeds enabled, drafts excluded).

## Example: create and view a draft post

```bash
# 1) Create a draft
cat > content/drafts/2025-01-31-hello-world.md << 'EOF'
Title: Hello World
Date: 2025-01-31 10:00
Category: blog
Tags: test, ai
Slug: hello-world
Summary: First draft post to verify build and serve.

This is a draft post.
EOF

# 2) Run the dev server
make devserver

# 3) Visit http://localhost:8000 and verify content
```

## Notes

- Theme: `simple` (configured in `pelicanconf.py`)
- Feeds are disabled in dev and enabled in publish.
- Robots.txt is managed via `content/extra/robots.txt`.
