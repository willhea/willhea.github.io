# AGENTS.md

Project context for Claude and other AI agents.

## Project Overview

**Site:** willhea.com
**Stack:** Hugo static site generator + PaperMod theme
**Deployment:** GitHub Pages via GitHub Actions (gh-pages branch)

## Commands

```bash
hugo server        # Dev server at http://localhost:1313
hugo server -D     # Dev server with drafts
hugo               # Build site to public/
```

## Content Structure

```
content/
  posts/           # Blog posts
  about.md         # About page
  contact.md       # Contact page
  portfolio.md     # Portfolio/work page
  search.md        # Search page (PaperMod feature)
```

## Configuration

- `hugo.yaml` - Main Hugo config (site params, menu, theme settings)
- `static/CNAME` - Custom domain
- `static/llms.txt` - LLM discovery file
- `static/images/` - Site images

## Theme

PaperMod theme installed as git submodule in `themes/PaperMod/`.
Documentation: https://adityatelange.github.io/hugo-PaperMod/

### Key PaperMod Features
- Profile mode homepage (configured in hugo.yaml)
- Dark/light mode toggle
- Search functionality (requires JSON output)
- Social icons

## Analytics

Uses **Cloudflare Web Analytics** (injected via `layouts/partials/extend_head.html`, production only). Do not suggest Google Analytics or other tracking systems.

## Deployment

Push to `main` triggers GitHub Actions workflow that:
1. Checks out repo with submodules
2. Builds site with Hugo
3. Deploys to `gh-pages` branch
4. GitHub Pages serves from gh-pages with custom domain

## Writing New Posts

```bash
hugo new posts/my-new-post.md
```

Frontmatter format:
```yaml
---
title: "Post Title"
date: 2025-01-15
tags: ["tag1", "tag2"]
draft: false
---
```
