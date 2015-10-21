#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Geng Yufeng'
SITENAME = u"Deadline's Coming"
SITESUBTITLE = u"Deadline是第一生产力."
SITEURL = 'http://potatola.github.io'

PATH = 'content'
USE_FOLDER_AS_CATEGORY = True

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

#themes
THEME = 'bootstrap3'

DISQUS_SITENAME = 'potatola'

# plugin config
PLUGIN_PATHS = [u'./pelican-plugins']
PLUGINS = [
    u'sitemap',
    u'summary',
    u'neighbors',
]

# sitemap plugin config
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Github', 'https://github.com/potatola'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/potatola'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
