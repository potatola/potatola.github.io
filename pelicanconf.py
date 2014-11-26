#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Geng Yufeng'
SITENAME = u"Deadline's Coming"
SITESUBTITLE = u"I don't need time, I need a deadline."
SITEURL = 'http://potatola.github.io/'

PATH = 'content'
USE_FOLDER_AS_CATEGORY = True

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

#themes
THEME = 'bootstrap3'

DISQUS_SITENAME = 'potatola'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('git-book', 'http://git-scm.com/book/zh/v1'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
          # ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
