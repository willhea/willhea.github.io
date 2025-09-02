# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://willhea.github.io" # change to "willhea.com" when ready
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = "output/"

# Do not publish drafts
WITH_FUTURE_DATES = False
ARTICLE_EXCLUDES = ["drafts"]
PAGE_EXCLUDES = ["drafts"]

# Don’t generate draft artifacts at all in publish builds
DRAFT_SAVE_AS = ''
DRAFT_URL = ''
DRAFT_PAGE_SAVE_AS = ''
DRAFT_PAGE_URL = ''

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
