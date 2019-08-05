#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Conseil d'Orientation"
SITENAME = "Afric'Edu"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

MARKDOWN = {
    'extension_configs': {
        #'video': {},
        'mdx_video': {},
        'markdown.extensions.tables': {},
    },
    'output_format': 'html5',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ["autopages", "pin_to_top", "bootstrapify"]

# Blogroll
LINKS = (('Contact', '/pages/contact.html'),
        ('Ecam', 'http://ecam.fr/'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/AfricEdu/community/?ref=page_internal'),
          )

DEFAULT_PAGINATION = 10


THEME = 'themes/built-texts'
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
STATIC_PATHS = ['images', 'files']
DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
