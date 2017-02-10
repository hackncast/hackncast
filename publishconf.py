#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = '//hackncast.org'
RELATIVE_URLS = False

# Configuração do Feed
FEED_ALL_RSS = 'feeds.rss'
CATEGORY_FEED_RSS = 'feeds/%s.rss'
FEED_ALL_ATOM = 'feeds.atom'
CATEGORY_FEED_ATOM = 'feeds/%s.atom'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Disqus
DISQUS_SITENAME = 'hackncast-podcast'

GOOGLE_ANALYTICS = "UA-62136730-1"
