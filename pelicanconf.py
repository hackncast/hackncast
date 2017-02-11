#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
from datetime import datetime
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
        'static_api',
        'pelican-podcast-feed',
        'pelican-vimeo',
        'pelican-youtube',
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

AUTHOR_URL = 'devs#{slug}'
AUTHOR_SAVE_AS = ''
AUTHORS_URL = 'devs'
AUTHORS_SAVE_AS = 'devs/index.html'

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

# Tag Cloud
TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = None

# Podcast Feed
PODCAST_FEED_PATH = u'feeds/podcast.rss'
PODCAST_FEED_TITLE = "Hack 'n' Cast"
PODCAST_FEED_EXPLICIT = u'No'
PODCAST_FEED_LANGUAGE = u'pt-br'
PODCAST_FEED_AUTHOR = u'Magnun, Ricardo, Gilson e Davi'
PODCAST_FEED_COPYRIGHT = u'&#x2117; &amp; &#xA9; 2011-{0} {1}'.format(datetime.now().year, PODCAST_FEED_AUTHOR)
PODCAST_FEED_SUBTITLE = 'Um podcast para old school hackers'
PODCAST_FEED_SUMMARY = 'Um podcast sobre tecnologias, software livre, open source e outros temas nerds.'
PODCAST_FEED_IMAGE = 'http://84.hackncast.org/images/logos/HNC-beta.png'
PODCAST_FEED_OWNER_NAME = PODCAST_FEED_AUTHOR
PODCAST_FEED_EMAIL_EMAIL = 'hackncast@gmail.com'
PODCAST_FEED_CATEGORY = ['Technology', 'Software How-To']

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

# DISQUS
#DISQUS_SITENAME = 'hackncast-podcast'
DISQUS_NO_ID = True

# SEO Settings
TWITTER = "@hackncast"
GLOBAL_KEYWORDS = ['podcast', "hack", "cast", "gnu", "linux", "programação", "python", "tecnologia", "nerd"]
OPEN_GRAPH_IMAGE = "/images/logos/HNC-beta.png"
SITEDESCRIPTION = "Um podcast sobre tecnologia em geral, mas especialmente focado em Software Livre, Open Source e GNU/Linux"

# Colaboradores
MAIN_AUTHORS = ['Magnun', 'Bruno', 'Ricardo', 'Gilson', 'Davi']

# Nav Bar
INSCREVA_SE = [
    ("iTunes", "https://itunes.apple.com/br/podcast/hack-n-cast/id884916846?l=pt"),
    ("Pocket Casts", "http://pcasts.in/hackncast"),
    ("Podflix", "http://podflix.com.br/hackncast/"),
    ("You Tuner", "http://youtuner.co/channel/mindbending.org_pt_category_hack-n-cast"),
    ("Stitcher", "http://www.stitcher.com/podcast/hack-n-cast"),
    ("iMasters", "http://imasters.com.br/perfil/hackcast/"),
    (None, None),
    ("FeedBurner", "http://feeds.feedburner.com/hack-n-cast"),
    ]

MAIS = [
    ("Trilhas", "/trilhas"),
    ("Tags", "/tags"),
    ("Changelog", "/changelog"),
    ("Devs", "/devs"),
    (None, None),
    ("Sobre", "/sobre"),
    ]

# Footer
PODCASTS_AMIGOS = [
        ("Castálio Podcast", "http://castalio.info/"),
        ("Blog do Edivaldo Brito", "http://www.edivaldobrito.com.br/"),
        ("NetoCast", "http://www.josecastanhasneto.blogspot.com.br/"),
        ("DatabaseCast", "http://imasters.com.br/perfil/databasecast"),
        ("Piratas da Internet", "https://piratasdainternet.github.io/"),
        ]

LINKS_ACOMPANHE = (
    ("E-Mail", "fa-envelope", "mailto: hackncast@gmail.com"),
    ("Twitter", "fa-twitter", "http://twitter.com/hackncast"),
    ("Facebook", "fa-facebook", "https://www.facebook.com/hackncast"),
    ("Google+", "fa-google-plus", "https://plus.google.com/u/0/b/118416649082623988287/118416649082623988287/about"),
    ("Grupo de Discussão", "fa-group", "https://groups.google.com/forum/?hl=pt-BR#!forum/hackncast"),
    ("Feed RSS", "fa-rss", "http://feeds.feedburner.com/hack-n-cast"),
    ("iTunes", "fa-apple", "https://itunes.apple.com/br/podcast/hack-n-cast/id884916846"),
    ("Telegram", "fa-paper-plane", "https://telegram.me/hackncast"),
    )

CATEGORY_IMAGES = {
    'Cultura Pop': 'images/trilhas/cultura-pop.jpg',
    'Filosofia': 'images/trilhas/filosofia.jpg',
    'GNU/Linux': 'images/trilhas/gnu-linux.jpg',
    'Programação': 'images/trilhas/programacao.jpg',
    'Tecnologias Web': 'images/trilhas/tecnologias-web.jpg',
    'Softwares': 'images/trilhas/softwares.jpg',
    'Segurança': 'images/trilhas/seguranca.jpg',
    }

LEVELS = {
        1: 'Newby',
        2: 'Wimp',
        3: 'Script Kiddie',
        4: 'Code Monkey',
        5: 'Programmer',
        6: 'Master Developer',
        7: 'Code Ninja',
        8: 'Rock Star Dev',
        9: 'Binary Wizard',
        10: 'Grand Master Dev',
        11: 'Dennis Ritchie',
        }

from math import log as log

def CALC_STATS(n):
    points = log(n, 2) + 1
    level = int(points)
    next_xp = int((points + 1) * 1024)
    xp = int((points) * 1024)
    return level, xp, next_xp
