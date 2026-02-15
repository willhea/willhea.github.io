# Website Migration Plan: All-Hugo Setup

## Decision
- **willhea.com**: Migrate Pelican → Hugo with PaperMod theme
- **skepticallabs.com**: Keep Hugo with Blowfish, finish setup
- **DNS**: Configure Cloudflare for both domains

## Goals
1. One tool (Hugo) for both sites
2. Dark mode support (auto-detect + toggle)
3. SEO/LLM discoverability (sitemap, robots.txt, meta tags, llms.txt)
4. Professional look for both sites
5. Easy content editing via Obsidian/markdown

---

## Phase 1: willhea.com Migration (Pelican → Hugo/PaperMod)

### 1.1 Setup Hugo + PaperMod
- Initialize Hugo in willhea repo (or new structure)
- Add PaperMod theme as submodule
- Configure hugo.toml with site settings

### 1.2 Migrate Content
Files to migrate:
- `content/pages/about.md` → `content/about.md`
- `content/pages/contact.md` → `content/contact.md`
- `content/pages/portfolio.md` → `content/portfolio.md`
- `content/blog/*.md` → `content/posts/*.md`
- `content/images/*` → `static/images/*`

Frontmatter changes:
- `Title:` → `title:`
- `Date:` → `date:`
- `Summary:` → `summary:` (or `description:`)
- `Status: published` → remove (Hugo uses `draft: true/false`)
- `Category:` → `categories:`
- `Tags:` → `tags:`
- `{static}` image refs → standard paths

### 1.3 Configure PaperMod
- Enable dark mode (auto + toggle)
- Set up navigation menu
- Configure homepage (profile mode or list)
- Add social links
- Enable search

### 1.4 SEO Setup
- robots.txt (Hugo generates automatically)
- sitemap.xml (Hugo generates automatically)
- Meta descriptions (from frontmatter)
- Open Graph tags (PaperMod handles this)
- llms.txt (copy from current site)

### 1.5 Deploy
- Update GitHub Actions workflow
- Test build locally
- Deploy to GitHub Pages
- Verify Cloudflare DNS

---

## Phase 2: skepticallabs.com Completion

### 2.1 Content Creation
Pages needed:
- **Home** (`content/_index.md`): Company intro, value prop
- **About** (`content/about.md`): Company background, Will's bio link
- **Services** (`content/services.md`): Consulting offerings
- **Contact** (`content/contact.md`): Email, location

### 2.2 Services Draft (based on willhea.com portfolio)
- Operations Consulting: Process improvement, systems design
- Data & Reporting: Visibility dashboards, metrics tracking
- Federal Contracting: Compliance, project recovery
- Fractional Leadership: Interim COO/Director roles

### 2.3 Cross-linking
- skepticallabs.com About → links to willhea.com
- willhea.com About → mentions Skeptical Labs LLC

### 2.4 Blowfish Configuration
- Color scheme (professional, not default)
- Navigation menu
- Footer with contact info
- Social links

### 2.5 SEO Setup
- Same as willhea.com (robots, sitemap, meta, llms.txt)

### 2.6 Deploy
- Set up GitHub Actions
- Configure GitHub Pages
- Set up Cloudflare DNS

---

## Phase 3: Cloudflare DNS Setup (Both Sites)

### willhea.com
- Verify current DNS records
- Ensure GitHub Pages CNAME configured
- Enable Cloudflare proxy (orange cloud)
- SSL: Full (strict)

### skepticallabs.com
- Add DNS records for GitHub Pages:
  - A record: 185.199.108.153 (and .109, .110, .111)
  - CNAME: www → skepticallabs.github.io
- Add CNAME file to repo
- Enable Cloudflare proxy
- SSL: Full (strict)

---

## Verification Checklist

### Both sites
- [ ] Homepage loads
- [ ] All pages accessible
- [ ] Dark mode toggle works
- [ ] Mobile responsive
- [ ] sitemap.xml accessible
- [ ] robots.txt accessible
- [ ] Meta descriptions appear in page source
- [ ] Social sharing cards work (test with Twitter/LinkedIn validators)
- [ ] HTTPS working (no mixed content)
- [ ] Cross-links between sites work

---

## Obsidian Compatibility Notes

Both themes work with standard Obsidian markdown:
- YAML frontmatter (same format)
- Standard markdown syntax
- Image links work the same way
- Wiki-links NOT supported (use standard markdown links)

Recommended Obsidian setup:
- Use standard `[text](url)` links, not `[[wiki-links]]`
- Put images in `static/images/` and reference as `/images/filename.png`
- Use YAML frontmatter at top of each file

---

## Execution Order

1. **willhea.com migration** (can run in background)
   - Set up Hugo + PaperMod
   - Migrate content
   - Test locally
   - You review before deploy

2. **skepticallabs.com content** (needs your input)
   - I draft services/about content
   - You review and edit
   - Then deploy

3. **DNS setup** (wizard-style, together)
   - Walk through Cloudflare settings
   - Verify each step
