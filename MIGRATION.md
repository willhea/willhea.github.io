# Hugo Migration Guide

**Created:** 2026-01-06  
**Current SSG:** Pelican 4.11.0  
**Target SSG:** Hugo  
**Purpose:** Document current site structure, URLs, and features before migrating to Hugo

---

## Table of Contents

1. [Current URL Structure](#current-url-structure)
2. [Content Inventory](#content-inventory)
3. [Feature Inventory](#feature-inventory)
4. [Front Matter Mapping](#front-matter-mapping)
5. [Template Architecture](#template-architecture)
6. [Static Assets](#static-assets)
7. [External Dependencies](#external-dependencies)
8. [Build & Deployment](#build--deployment)
9. [Migration Checklist](#migration-checklist)

---

## Current URL Structure

### Site Configuration
- **Development URL:** `http://localhost:8000`
- **Production URL:** `https://willhea.github.io` (configured in publishconf.py)
- **Custom Domain:** `willhea.com` (via CNAME)

### Blog Posts (Articles)

Pelican generates articles at root with slug-based URLs:

| Source File | Generated URL | Title |
|-------------|---------------|-------|
| `content/blog/1_why_willhea.md` | `/why_willhea.html` | Why willhea.com? |
| `content/blog/2_how_I_built_this_site.md` | `/how_i_built_this_site.html` | How I Built This Site |
| `content/blog/3_skeptical_labs.md` | `/skeptical_labs_goals.html` | Skeptical Labs Goals |
| `content/blog/4_timeline_vs_runway.md` | `/timeline_vs_runway.html` | Timeline vs Runway |
| `content/blog/5-money_market_funds.md` | `/money-market.html` | Just use money market funds |
| `content/blog/6-national_links_trust.md` | `/national-links-trust.html` | In Praise of National Links Trust |

**Pattern:** `/{slug}.html` (slug defined in front matter)

### Pages (Static Pages)

| Source File | Generated URL | Title |
|-------------|---------------|-------|
| `content/pages/about.md` | `/pages/about.html` | About |
| `content/pages/contact.md` | `/pages/contact.html` | Contact |
| `content/pages/404.md` | `/404.html` | 404 |

**Pattern:** `/pages/{slug}.html` (except 404 which is at root)

### Taxonomy Pages

Pelican automatically generates taxonomy index pages:

- **Tags:** `/tag/{tag-name}.html` (25 tag pages)
  - Example: `/tag/pelican.html`, `/tag/personal.html`, `/tag/finance.html`
- **Categories:** `/category/{category-name}.html`
  - Example: `/category/blog.html` (only one category currently)
- **Authors:** `/author/{author-slug}.html`
  - Example: `/author/will-hea.html`

### Index & Archive Pages

- **Homepage:** `/index.html` - Lists all posts
- **Archives:** `/archives.html` - Archive listing
- **Tags index:** `/tags.html` - All tags
- **Categories index:** `/categories.html` - All categories
- **Authors index:** `/authors.html` - All authors

### Feeds

- **All posts:** `/feeds/all.atom.xml`
- **Category feed:** `/feeds/blog.atom.xml`

### Static Assets

- **CSS:** `/site.css` (from `content/extra/site.css`)
- **Images:** `/images/{filename}` (from `content/images/`)
- **Robots:** `/robots.txt` (from `content/extra/robots.txt`)

---

## Content Inventory

### Published Articles (6)

1. **Why willhea.com?** (2025-09-03)
   - Tags: personal, writing, goals, introduction, meta
   - Summary: I need a place to play and share my thoughts.

2. **How I Built This Site** (2025-09-13)
   - Tags: pelican, python, github_pages, static_site, goatcounter, privacy, meta
   - Summary: A guide to building a simple website with Pelican and GitHub Pages.

3. **Skeptical Labs Goals** (2025-09-28)
   - Tags: skeptical_labs, goals, operations, principles, personal
   - Summary: What is Skeptical Labs and what do I want to do with it?

4. **Timeline vs Runway** (2025-10-02)
   - Tags: startups, finance, runway, fundraising, prioritization, operations
   - Summary: In startups, runway is a useful construct, but it can misguide resource allocation.

5. **Just use money market funds** (2025-10-17)
   - Tags: finance, cash, treasury, liquidity
   - Summary: Simple, easy, accessible cash with a fair return.

6. **In Praise of National Links Trust** (2026-01-06)
   - Tags: golf, company_structure, llc
   - Summary: National Links Trust has been an excellent steward of DC's public golf courses.

### Pages (3)

1. **About** - Personal bio and professional background
2. **Contact** - Contact information page
3. **404** - Custom 404 error page

### Drafts (7)

- `default_is_death.md`
- `ideas.md`
- `new-post-template.md`
- `portfolio.md`
- `resume.md`
- `execution_is_strategy.md`
- `have_you_considered_fraud.md`

**Note:** Drafts are excluded from production builds via `ARTICLE_EXCLUDES = ["drafts"]`

### Images (1)

- `east_potomac_practice.jpg` (259KB) - Used in "National Links Trust" article

---

## Feature Inventory

### Markdown Extensions (pelicanconf.py:83)

Pelican uses Python-Markdown with the following extensions:

```python
MARKDOWN = {
    "extensions": [
        "markdown.extensions.admonition",   # Callout boxes (!!! note, !!! info)
        "markdown.extensions.tables",       # GitHub-style tables
        "markdown.extensions.footnotes",    # Footnotes [^1]
        "markdown.extensions.attr_list",    # Add attributes to elements
    ],
}
```

**Hugo Equivalent:**
- Admonitions: Use shortcodes or custom HTML
- Tables: Native support
- Footnotes: Native support
- Attr_list: Native support via attribute syntax

### Template Features

#### Custom Templates (4 files)

1. **base.html** - Master template with:
   - Semantic HTML5 structure
   - GoatCounter analytics integration
   - Site header with navigation
   - Footer with copyright and social links
   - Responsive meta viewport

2. **index.html** - Blog listing with:
   - Article summaries
   - Publish dates
   - Author links

3. **article.html** - Individual posts with:
   - Article title (h1)
   - Content section
   - Publish date metadata
   - Author attribution

4. **page.html** - Static pages with:
   - Page title (h1)
   - Content section (no metadata)

#### Template Variables Used

- `{{ SITENAME }}` - Site name
- `{{ SITEURL }}` - Base URL
- `{{ CURRENT_YEAR }}` - Current year for copyright
- `{{ SOCIAL }}` - Social media links
- `{{ pages }}` - All pages for navigation
- `{{ articles }}` - All articles
- `{{ article.* }}` - Article metadata (title, date, content, etc.)
- `{{ page.* }}` - Page metadata

### CSS Features (content/extra/site.css:1)

Custom minimal stylesheet (~148 lines):

- **CSS Variables:** Uses `:root` for color scheme support
- **System fonts:** Native font stack (system-ui, -apple-system, etc.)
- **Responsive design:** Mobile-first with breakpoint at 640px
- **Accessibility:** High contrast links (#00BFFF), semantic HTML
- **Sticky header:** Position sticky navigation
- **Container max-width:** 920px centered layout
- **Image optimization:** Responsive images, max-width constraints

**Key design principles:**
- Minimalist aesthetic
- Browser-default heading sizes (no remapping)
- High readability (16px base font, 1.6 line-height)
- Clean spacing and borders

### Analytics

**GoatCounter** (templates/base.html:11)
- Privacy-focused analytics
- Script: `https://gc.zgo.at/count.js`
- Site: `https://willhea.goatcounter.com/count`
- No cookies, GDPR-compliant

### Feeds

**Atom Feeds** (publishconf.py:11)
- All posts: `/feeds/all.atom.xml`
- Category feeds: `/feeds/{slug}.atom.xml`
- Format: Atom XML (not RSS)

---

## Front Matter Mapping

### Pelican Front Matter (Current)

```yaml
---
Title: Post Title
Date: 2025-09-03
Status: published
Category: blog
Tags: tag1, tag2, tag3
Slug: post-slug
Summary: One-line summary of the post.
---
```

### Hugo Front Matter (Target)

```yaml
---
title: "Post Title"
date: 2025-09-03
draft: false
categories: ["blog"]
tags: ["tag1", "tag2", "tag3"]
slug: "post-slug"
summary: "One-line summary of the post."
---
```

### Field Mapping Table

| Pelican Field | Hugo Field | Conversion Notes |
|---------------|------------|------------------|
| `Title:` | `title:` | Lowercase key, add quotes |
| `Date:` | `date:` | Lowercase key, same format |
| `Status: published` | `draft: false` | Invert logic |
| `Category: blog` | `categories: ["blog"]` | Lowercase key, array format |
| `Tags: tag1, tag2` | `tags: ["tag1", "tag2"]` | Lowercase key, array format |
| `Slug: slug` | `slug: "slug"` | Lowercase key, add quotes |
| `Summary:` | `summary:` or `description:` | Lowercase key, add quotes |

### Conversion Script Needed

A script to convert all 6 published posts + 3 pages front matter from Pelican to Hugo format.

---

## Template Architecture

### Jinja2 → Go Templates Conversion

#### Base Template Structure

**Pelican (Jinja2):**
```jinja2
{% extends "base.html" %}
{% block content %}
  {{ article.content }}
{% endblock %}
```

**Hugo (Go templates):**
```go
{{ define "main" }}
  {{ .Content }}
{{ end }}
```

#### Common Template Patterns

| Pelican (Jinja2) | Hugo (Go) |
|------------------|-----------|
| `{{ SITENAME }}` | `{{ .Site.Title }}` |
| `{{ SITEURL }}` | `{{ .Site.BaseURL }}` |
| `{{ article.title }}` | `{{ .Title }}` |
| `{{ article.content }}` | `{{ .Content }}` |
| `{{ article.date }}` | `{{ .Date }}` |
| `{% for article in articles %}` | `{{ range .Pages }}` |
| `{% if SOCIAL %}` | `{{ with .Site.Params.social }}` |
| `{{ article.url }}` | `{{ .RelPermalink }}` |

#### Required Hugo Templates

1. **baseof.html** - Base layout (replaces base.html)
2. **list.html** - Blog listing (replaces index.html)
3. **single.html** - Individual posts (replaces article.html)
4. **layouts/page/single.html** - Static pages (replaces page.html)
5. **404.html** - Error page

---

## Static Assets

### Current Structure

```
content/
├── images/
│   └── east_potomac_practice.jpg
└── extra/
    ├── CNAME          # Custom domain configuration
    ├── robots.txt     # Empty file (allows all)
    └── site.css       # Main stylesheet
```

### Hugo Target Structure

```
static/
├── images/
│   └── east_potomac_practice.jpg
├── CNAME
├── robots.txt
└── css/
    └── site.css       # or assets/css/site.css if using Hugo Pipes
```

### Path Metadata Mappings (pelicanconf.py:69)

Pelican uses `EXTRA_PATH_METADATA` to control output paths:

```python
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/site.css": {"path": "site.css"},
}
```

Hugo achieves this automatically - files in `static/` are copied to root.

### Static Paths (pelicanconf.py:74)

```python
STATIC_PATHS = [
    "images",
    "extra",
]
```

Hugo equivalent: Everything in `static/` directory.

---

## External Dependencies

### Domain & DNS

- **Domain:** willhea.com (registered externally)
- **DNS Configuration:** CNAME pointing to `willhea.github.io`
- **CNAME file:** `content/extra/CNAME` contains `willhea.com`
- **Migration impact:** None - CNAME file moves to `static/CNAME`

### Hosting

- **Provider:** GitHub Pages
- **Repository:** 
  - Private source: `willhea/willhea.github.io_private`
  - Public deploy: `willhea/willhea.github.io`
- **Branch:** `main` (published content)
- **Deploy tool:** `ghp-import` (Makefile:82)
- **Migration impact:** Hugo can use GitHub Actions or continue with ghp-import

### Analytics

- **Provider:** GoatCounter
- **Account:** `willhea.goatcounter.com`
- **Implementation:** JavaScript in `templates/base.html:11-13`
- **Privacy:** Cookie-free, GDPR-compliant
- **Migration impact:** Copy script tag to Hugo base template

### Build Tools

- **Python version:** 3.13+
- **Package manager:** uv (not pip)
- **Task runner:** Make (primary), Invoke (alternative)
- **Migration impact:** Replace with Hugo CLI

### Version Control

- **VCS:** Git
- **Remote:** GitHub
- **Deployment status:** https://github.com/willhea/willhea.github.io/actions/workflows/pages/pages-build-deployment

---

## Build & Deployment

### Current Build Process

#### Development
```bash
make devserver           # Build + watch + serve at localhost:8000
# or
make html               # Build only (dev config)
make serve              # Serve existing build
```

#### Production
```bash
make publish            # Build with production config
make github            # Build + deploy to GitHub Pages
```

#### Clean
```bash
make clean             # Remove output/ directory
```

### Build Configuration

**Development** (pelicanconf.py):
- SITEURL: `https://willhea.com`
- RELATIVE_URLS: Can be toggled via `RELATIVE=1` flag
- Feeds: Disabled
- Drafts: Included (in `content/drafts/`)

**Production** (publishconf.py):
- SITEURL: `https://willhea.github.io`
- RELATIVE_URLS: False
- Feeds: Enabled (Atom XML)
- Drafts: Excluded
- DELETE_OUTPUT_DIRECTORY: True

### Deployment Process (Makefile:82)

```bash
make github
```

This runs:
1. `make publish` - Build with production config
2. `ghp-import -m "Generate Pelican site" -b main output/ --no-jekyll`
3. `git push origin main`

The `--no-jekyll` flag creates `.nojekyll` file (tells GitHub Pages to skip Jekyll processing).

### Hugo Equivalent

#### Development
```bash
hugo server -D         # Serve with drafts
hugo server           # Serve without drafts
```

#### Production
```bash
hugo                  # Build to public/
```

#### Deployment Options

1. **Continue with ghp-import:**
   ```bash
   hugo
   ghp-import -m "Generate Hugo site" -b main public/ --no-jekyll
   git push origin main
   ```

2. **GitHub Actions (recommended):**
   - Use official Hugo GitHub Action
   - Automatic builds on push to source branch
   - No need for ghp-import

---

## Migration Checklist

### Pre-Migration

- [x] Document current URL structure
- [x] Inventory all content (6 posts, 3 pages, 7 drafts)
- [x] Document front matter format
- [x] Identify all Markdown extensions used
- [x] List external dependencies
- [x] Screenshot current site for comparison
- [ ] Export GoatCounter baseline metrics
- [ ] Test current site locally one final time

### Content Migration

- [ ] Install Hugo
- [ ] Create new Hugo site structure
- [ ] Convert front matter (6 posts + 3 pages)
  - [ ] Lowercase all field names
  - [ ] Convert Status → draft (inverted)
  - [ ] Convert Category → categories (array)
  - [ ] Convert Tags → tags (array)
  - [ ] Add quotes to string values
- [ ] Copy content files to Hugo content structure
  - [ ] `content/blog/*.md` → `content/posts/*.md`
  - [ ] `content/pages/*.md` → `content/*.md` (or `content/pages/`)
  - [ ] `content/drafts/*.md` → `content/drafts/*.md`
- [ ] Move static assets
  - [ ] `content/images/*` → `static/images/`
  - [ ] `content/extra/site.css` → `static/css/site.css`
  - [ ] `content/extra/CNAME` → `static/CNAME`
  - [ ] `content/extra/robots.txt` → `static/robots.txt`

### Template Migration

- [ ] Create Hugo theme or use existing minimal theme
- [ ] Convert base.html → baseof.html
  - [ ] Replace Jinja2 syntax with Go templates
  - [ ] Add GoatCounter script
  - [ ] Implement navigation from pages
  - [ ] Add social links to footer
- [ ] Convert index.html → list.html
- [ ] Convert article.html → single.html
- [ ] Create page layout (single.html variant)
- [ ] Convert 404.html
- [ ] Port custom CSS
  - [ ] Copy site.css or integrate into theme
  - [ ] Test responsive breakpoints
  - [ ] Verify color scheme

### Configuration

- [ ] Create hugo.toml (or config.yaml)
  - [ ] Set baseURL = "https://willhea.github.io"
  - [ ] Set title = "Will Hea"
  - [ ] Set timezone = "America/New_York"
  - [ ] Configure permalinks to match current URLs
  - [ ] Add social links to params
  - [ ] Configure CURRENT_YEAR variable
- [ ] Configure taxonomy (tags, categories)
- [ ] Configure Markdown renderer
  - [ ] Enable tables
  - [ ] Enable footnotes
  - [ ] Configure heading IDs
- [ ] Set up feeds (Atom if possible, RSS otherwise)

### URL Preservation

- [ ] Test that post URLs match: `/{slug}.html`
- [ ] Test that page URLs match: `/pages/{slug}.html`
- [ ] Test that tag URLs match: `/tag/{tag}.html`
- [ ] Test that category URLs match: `/category/{category}.html`
- [ ] Create 301 redirects if URLs changed
  - [ ] Document redirect rules
  - [ ] Implement via _redirects file or Hugo aliases

### Testing

- [ ] Build Hugo site locally
- [ ] Compare rendered HTML to Pelican output
- [ ] Test all 6 published posts render correctly
- [ ] Test all 3 pages render correctly
- [ ] Test image paths work
- [ ] Test CSS loads correctly
- [ ] Test navigation links work
- [ ] Test social links work
- [ ] Test GoatCounter tracking works
- [ ] Test feeds generate correctly
- [ ] Test 404 page
- [ ] Test CNAME file in output
- [ ] Test robots.txt in output
- [ ] Mobile responsive test
- [ ] Cross-browser test

### Deployment

- [ ] Choose deployment method:
  - Option A: Continue with ghp-import
  - Option B: GitHub Actions (recommended)
- [ ] If using GitHub Actions:
  - [ ] Create `.github/workflows/hugo.yml`
  - [ ] Configure Hugo version
  - [ ] Configure deployment to main branch
  - [ ] Test workflow on test branch first
- [ ] Deploy to test environment
- [ ] Verify all URLs work on live site
- [ ] Check GoatCounter receives events
- [ ] Monitor for 404 errors

### Post-Migration

- [ ] Update README.md with Hugo instructions
- [ ] Update notes.md
- [ ] Update .cursor/rules/ for Hugo
- [ ] Archive Pelican-specific files
  - [ ] Move pelicanconf.py → archive/
  - [ ] Move publishconf.py → archive/
  - [ ] Move tasks.py → archive/
  - [ ] Keep Makefile for reference or adapt for Hugo
- [ ] Update pyproject.toml or remove if no longer using Python
- [ ] Clean up dependencies (remove Pelican, keep ghp-import if used)
- [ ] Update .gitignore
  - [ ] Replace `output/` with `public/` and `resources/`
  - [ ] Add Hugo-specific ignores
- [ ] Commit migration to git
- [ ] Monitor analytics for traffic patterns
- [ ] Monitor for broken links
- [ ] Verify search engine indexing preserved

### Documentation

- [ ] Document new build commands in README
- [ ] Document new deployment process
- [ ] Create CHANGELOG.md entry for migration
- [ ] Update AI collaboration guidelines for Hugo
- [ ] Archive this MIGRATION.md for reference

---

## Notes & Considerations

### URL Preservation Strategy

**Critical:** Current URLs use `.html` extension. Hugo defaults to clean URLs (`/post/` instead of `/post.html`).

**Options:**
1. Configure Hugo to use `.html` extensions (preserves URLs, SEO)
2. Use clean URLs + create redirects/aliases for old URLs
3. Mix: Keep `.html` for migrated content, clean URLs for new content

**Recommendation:** Configure Hugo permalinks to maintain `.html` extensions for continuity.

Example hugo.toml:
```toml
[permalinks]
  posts = "/:slug.html"
  pages = "/pages/:slug.html"
```

### Markdown Extension Compatibility

**Admonitions** are the biggest concern:
- Pelican uses Python-Markdown admonition syntax: `!!! note`
- Hugo doesn't have native admonition support
- Options:
  1. Convert to HTML in content files
  2. Create Hugo shortcodes for callouts
  3. Use a Hugo theme with admonition support

**Recommendation:** If using admonitions heavily, create Hugo shortcodes. Otherwise, convert to HTML or use blockquotes.

### Feed Format

- Current: Atom XML (`/feeds/all.atom.xml`)
- Hugo default: RSS 2.0 (`/index.xml`)

Consider:
- Hugo can generate Atom feeds with custom templates
- Or provide both Atom and RSS
- Update feed URLs if changing format

### Performance Comparison

Once migrated, compare:
- Build times (Hugo should be faster)
- Site size
- Lighthouse scores
- Time to first byte (TTFB)

### Migration Timeline Estimate

- **Content conversion:** 2-3 hours (script + manual review)
- **Template migration:** 4-6 hours (Jinja2 → Go templates)
- **Configuration:** 1-2 hours
- **Testing:** 2-3 hours
- **Deployment setup:** 1-2 hours
- **Total:** 10-16 hours

This assumes familiarity with Hugo. First-time Hugo users should add 4-6 hours for learning.

### Rollback Plan

Keep Pelican setup intact until Hugo migration is proven:
1. Don't delete Pelican files immediately
2. Keep both builds working in parallel during transition
3. Can revert to Pelican if issues arise
4. Archive Pelican files only after 30 days of successful Hugo deployment

---

## Reference Links

- **Current site:** https://willhea.com
- **GitHub repo (source):** https://github.com/willhea/willhea.github.io_private
- **GitHub repo (public):** https://github.com/willhea/willhea.github.io
- **Pelican docs:** https://docs.getpelican.com/
- **Hugo docs:** https://gohugo.io/documentation/
- **Hugo migration guide:** https://gohugo.io/tools/migrations/
- **GoatCounter:** https://www.goatcounter.com/

---

**Last updated:** 2026-01-06  
**Site build:** Pelican 4.11.0 (current)  
**Status:** Ready for migration
