#Pelican config file
import datetime

AUTHOR = 'Will Hea'
SITENAME = 'Will Hea'
SITEURL = "https://willhea.com"

PATH = "content"
OUTPUT_PATH = "output"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
)

# Social widget
SOCIAL = (
    ("Linkedin", "https://www.linkedin.com/in/willhea/"),
    ("X", "https://x.com/WilliamHea"),
    ("Bsky", "https://bsky.app/profile/willhea.com"),
    ("GitHub", "https://github.com/willhea")
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True # good for local dev if you enable it
THEME = 'simple'

# Allow overriding theme templates from local templates directory
THEME_TEMPLATES_OVERRIDES = ["templates"]

# path-specific metadata
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/llms.txt": {"path": "llms.txt"},

    # Map custom site stylesheet to root for easy linking as /site.css
    "extra/site.css": {"path": "site.css"},
}

# Static files copied as-is to the output directory
# - Place post images under content/images and reference as /images/<file>
STATIC_PATHS = [
    "images",
    "extra",
]

# Exclude drafts from generation
ARTICLE_EXCLUDES = ["drafts"]

# Plugins
PLUGINS = ["sitemap"]

# Sitemap configuration
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.7,  # About and Portfolio are high value
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "weekly",
        "pages": "monthly",
    },
}

# Expose current year to templates (avoid using Jinja now())
CURRENT_YEAR = datetime.date.today().year

# Enable useful Markdown extensions, including admonitions, tables, and footnotes
# - admonition: allows vanilla-style callouts with `!!! note`, `!!! info`, etc.
# - tables: GitHub-like table syntax
# - footnotes: compact source footnotes for table/source notes
# - attr_list: optional, allows adding attributes/classes if ever needed
MARKDOWN = {
    "extensions": [
        "markdown.extensions.admonition",
        "markdown.extensions.tables",
        "markdown.extensions.footnotes",
        "markdown.extensions.attr_list",
    ],
    "extension_configs": {
        # No special config needed; using defaults keeps this close to vanilla
    },
}