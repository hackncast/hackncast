#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)
from authors import SITEAUTHORS

DEFAULT_PAGINATION = 10

BASE_DIR = os.path.dirname(__file__)

AUTHOR = u'Magnun'
SITENAME = u"Hack 'n' Cast"
RELATIVE_URLS = True
TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Theme
THEME = os.path.join(BASE_DIR, '.theme')

JINJA_EXTENSIONS = ['jinja2.ext.do']

DEFAULT_DATE_FORMAT = "%A, %d de %B de %Y às %H:%M"

# Plugins
PLUGIN_PATHS = [os.path.join(BASE_DIR, '.plugins')]
PLUGINS = [
        'gzip_cache',
        'sitemap',
        'touch',
        'archive_org_podcast_directive',
        'better_figures_and_images',
        ]

# Configurações para armazenar cada página dentro do seu próprio diretório
INDEX_SAVE_AS = "/releases/index.html"

ARTICLE_URL = "{slug}"
ARTICLE_SAVE_AS = "{slug}/index.html"

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"

CATEGORIES_URL = "trilhas"
CATEGORIES_SAVE_AS = "trilhas/index.html"

CATEGORY_URL = "trilha/{slug}"
CATEGORY_SAVE_AS = "trilha/{slug}/index.html"

TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/index.html"

SERIES_URL = "serie/{slug}"
SERIES_SAVE_AS = "serie/{slug}/index.html"

AUTHOR_URL = 'dev/{slug}'
AUTHOR_SAVE_AS = 'dev/{slug}/index.html'
AUTHORS_URL = ''
AUTHORS_SAVE_AS = ''

ARCHIVES_URL = 'changelog'
ARCHIVES_SAVE_AS = 'changelog/index.html'

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/pagina/{number}/', '{base_name}/pagina/{number}/index.html'),
)
RELATIVE_URLS = False

# Configuração de Imagens
RESPONSIVE_IMAGES = True

# Static
STATIC_PATHS = ["images"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS = (
#     ('Pelican', 'http://getpelican.com/'),
#     ('Python.org', 'http://python.org/'),
#     ('Jinja2', 'http://jinja.pocoo.org/'),
#     ('You can modify those links in your config file', '#'),
# )

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# SITEMAP SETTINGS
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.2,
        'pages': 0.7
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    },
}

# SEO Settings
TWITTER = "@hackncast"
GLOBAL_KEYWORDS = ['podcast', "hack", "cast", "gnu", "linux", "programação", "python", "tecnologia", "nerd"]
OPEN_GRAPH_IMAGE = "/images/logos/HNC-beta.png"
SITEDESCRIPTION = "Um podcast sobre tecnologia em geral, mas especialmente focado em Software Livre, Open Source e GNU/Linux"

# Colaboradores
MAIN_AUTHORS = ['Magnun', 'Bruno', 'Ricardo', 'Gilson', 'Davi']

PODCASTS_AMIGOS = [
        ("Piratas da Internet", "http://piratasdainternet.com.br/"),
        ("DatabaseCast", "http://imasters.com.br/perfil/databasecast"),
        ("SciCast", "http://www.scicast.com.br/scicast/"),
        ("NetoCast", "http://www.josecastanhasneto.blogspot.com.br/"),
        ]

LINKS_ACOMPANHE = (
    ("E-Mail", "fa-envelope", "mailto: hackncast@gmail.com"),
    ("Titter", "fa-twitter", "http://twitter.com/hackncast"),
    ("Facebook", "fa-facebook", "https://www.facebook.com/hackncast"),
    ("Google+", "fa-google-plus", "https://plus.google.com/u/0/b/118416649082623988287/118416649082623988287/about"),
    ("Grupo de Discussão", "fa-group", "https://groups.google.com/forum/?hl=pt-BR#!forum/hackncast"),
    ("Feed RSS", "fa-rss", "http://feeds.feedburner.com/hack-n-cast"),
    ("iTunes", "fa-apple", "https://itunes.apple.com/br/podcast/hack-n-cast/id884916846"),
    )
