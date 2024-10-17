AUTHOR = 'kei ikegami'
SITENAME = "Kei's Homepage"
SITEURL = ""
PATH = "content"

STATIC_PATHS = ['images', 'pdfs']

TIMEZONE = 'EST'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['neighbors']

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = False


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
