import datetime

# Basic information about the site.
SITENAME = "Apache Responsible AI"
SITEDESC = "The Apache Software Foundation Responsible AI initiative"
SITEDOMAIN = "rai.apache.org"
SITEURL = "https://rai.apache.org"
SITELOGO = "https://www.apache.org/img/asf_logo.png"
SITEREPOSITORY = "https://github.com/apache/rai-site/blob/main/content/"
CURRENTYEAR = datetime.date.today().year
TRADEMARKS = "Apache and the Apache feather logo are trademarks of The Apache Software Foundation."
TIMEZONE = "UTC"
# Theme includes templates and possibly static files
THEME = "content/theme"
# Specify location of plugins, and which to use
PLUGIN_PATHS = [
    "plugins",
]
# If the website uses any *.ezmd files, include the 'gfm' and 'asfreader' plugins (in that order)
PLUGINS = [
    "toc",
    "spu",
    "gfm",
    "asfgenid",
    "asfrun",
]

# All content is located at '.' (aka content/ )
PAGE_PATHS = ["pages"]
STATIC_PATHS = [
    ".",
]
# Where to place/link generated pages

PATH_METADATA = "pages/(?P<path_no_ext>.*)\\..*"

PAGE_SAVE_AS = "{path_no_ext}.html"
# Don't try to translate
PAGE_TRANSLATION_ID = None
# Disable unused Pelican features
# N.B. These features are currently unsupported, see https://github.com/apache/infrastructure-pelican/issues/49
FEED_ALL_ATOM = None
INDEX_SAVE_AS = ""
TAGS_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""
# Per-tag / per-category / per-author pages too: the theme has no template for
# them, and posts carry tags only as labels on the post and the blog index.
TAG_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
# Blog posts live in content/blog/ and are published under /blog/
ARTICLE_PATHS = ["blog"]
ARTICLE_URL = "blog/{slug}.html"
ARTICLE_SAVE_AS = "blog/{slug}.html"
ARTICLE_ORDER_BY = "reversed-date"
# The blog index: content/theme/templates/blog.html rendered to /blog/index.html
DIRECT_TEMPLATES = ["blog"]
BLOG_URL = "blog/"
BLOG_SAVE_AS = "blog/index.html"
# Posts carry a Date; drafts are excluded until their status says published
DEFAULT_DATE_FORMAT = "%d %B %Y"
WITH_FUTURE_DATES = False
# Disable all processing of .html files
READERS = {
    "html": None,
}

# Configure the asfgenid plugin
ASF_GENID = {
    "unsafe_tags": True,
    "metadata": False,
    "elements": False,
    "permalinks": False,
    "tables": False,
    "headings": False,
    "toc": False,
    "debug": False,
}


# Configure the asfrun plugin (finalization)
ASF_POSTRUN = [
    "/bin/bash pagefind.sh",
]


# Configure ignore files
# File and directory basenames matching any of these patterns will be ignored by the processor.
IGNORE_FILES = [
    "theme",
]
