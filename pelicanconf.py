#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Conseil d'Orientation"
SITENAME = "Afric'Edu"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ["category_meta"]

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

MENUITEMS = [('all', '/blog/archives.html')]

THEME = 'themes/built-texts'
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
STATIC_PATHS = ['images', 'files']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
