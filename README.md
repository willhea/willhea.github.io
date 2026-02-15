# willhea.github.io

Source repo for [willhea.com](https://willhea.com)

## Stack

- **Generator:** [Hugo](https://gohugo.io/)
- **Theme:** [PaperMod](https://adityatelange.github.io/hugo-PaperMod/)
- **Hosting:** GitHub Pages
- **Deployment:** GitHub Actions (pushes to `gh-pages` branch)

## Quickstart

**Prerequisites:** Hugo installed ([installation guide](https://gohugo.io/installation/))

```bash
# Clone with submodules (for theme)
git clone --recurse-submodules <repo-url>
cd willhea.github.io

# Run dev server
hugo server
```

Site will be available at http://localhost:1313

## Commands

```bash
hugo server        # Dev server with live reload
hugo server -D     # Include draft posts
hugo               # Build site to public/
```

## Project Structure

```
content/
  posts/           # Blog posts
  about.md         # About page
  contact.md       # Contact page
  portfolio.md     # Portfolio page
  search.md        # Search page
hugo.yaml          # Site configuration
static/            # Static assets (images, CNAME, llms.txt)
themes/PaperMod/   # Theme (git submodule)
```

## Writing Posts

```bash
hugo new posts/my-new-post.md
```

Frontmatter:
```yaml
---
title: "Post Title"
date: 2025-01-15
tags: ["tag1", "tag2"]
draft: false
summary: "Brief description for listings"
---
```

## Deployment

Push to `main` triggers automatic deployment via GitHub Actions:
1. Builds site with Hugo
2. Deploys to `gh-pages` branch
3. GitHub Pages serves the site

## Theme Setup

PaperMod is installed as a git submodule. If you need to reinstall:

```bash
git submodule update --init --recursive
```

## Configuration

Main config is in `hugo.yaml`:
- Site metadata and SEO
- PaperMod theme settings (profile mode, social icons, etc.)
- Menu structure
- Search settings
