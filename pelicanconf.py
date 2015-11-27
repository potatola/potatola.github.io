#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Geng Yufeng'
SITENAME = u"GYF"
SITESUBTITLE = u"Deadline是第一生产力."
SITEURL = 'http://gengyf.com'

PATH = 'content'
USE_FOLDER_AS_CATEGORY = True

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

#themes
THEME = 'pelican-bootstrap3'
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DEFAULT_PAGINATION = 10
FAVICON = 'images/favicon.ico'

DISQUS_SITENAME = 'potatola'
GOOGLE_ANALYTICS = 'UA-70409451-1'

# plugin config
PLUGIN_PATHS = [u'./pelican-plugins']
PLUGINS = [u'sitemap', u'summary', u'related_posts', u'tag_cloud', u'section_number']

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
SOCIAL = (('Github', 'https://github.com/potatola'),
	('LinkedIn', 'https://cn.linkedin.com/in/yufeng-geng-a643b27b'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
