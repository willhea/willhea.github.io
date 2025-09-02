#Pelican config file

AUTHOR = 'Will Hea'
SITENAME = 'willhea.com'
SITEURL = ""

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
RELATIVE_URLS = False # good for local dev if you enable it
THEME = 'simple'

# path-specific metadata
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
}

# Static files copied as-is to the output directory
# - Place post images under content/images and reference as /images/<file>
STATIC_PATHS = [
    "images",
    "extra",
]