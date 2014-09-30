#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

DEFAULT_PAGINATION = 4

BASE_DIR = os.path.dirname(__file__)

AUTHOR = u'Magnun Leno'
SITENAME = u"Hack 'n' Cast"
RELATIVE_URLS = True
TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Theme
THEME = os.path.join(BASE_DIR, '.theme')

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
ARTICLE_URL = "{slug}"
ARTICLE_SAVE_AS = "{slug}/index.html"

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/index.html"

SERIES_URL = "series/{slug}"
SERIES_SAVE_AS = "series/{slug}/index.html"

AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
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
ACTIVE_AUTHORS = ['Magnun Leno', 'Bruno Barbosa', 'Ricardo Medeiros', 'Gilson Filho']
SITEAUTHORS = {
        'Magnun Leno':
            {
                'image': 'https://lh5.googleusercontent.com/-tdNroc0oPGc/AAAAAAAAAAI/AAAAAAAAAOw/q_jbij7hbVI/s120-c/photo.jpg',
                'description': '<p>Criador, Desenvolvedor e Autor do blog <a href="http://mindbending.org/">Mind Bending</a></p>',
                'links': [
                    '<a href="https://twitter.com/mind_bend" class="label label-default"><i class="fa fa-twitter"></i> Twitter</a>',
                    '<a href="https://github.com/magnunleno" class="label label-default"><i class="fa fa-github"></i> Github</a>',
                    ]
            },
        'Bruno Barbosa':
            {
                'image': 'https://lh3.googleusercontent.com/-ubgzC730QYE/AAAAAAAAAAI/AAAAAAAAAMA/baBevnRUSGQ/s120-c/photo.jpg',
                'description': '<p>Co-Fundador do <a href="http://algoritmizando.com">Algoritmizando</a>, usuário GNU/Linux. Utiliza as tecnologias Zope/Plone, Django e web2py.</p>',
                'links': [
                    '<a href="https://twitter.com/brunobbbs" class="label label-default"><i class="fa fa-twitter"></i> Twitter</a>',
                    '<a href="https://github.com/bruninbsb/" class="label label-default"><i class="fa fa-github"></i> Github</a>',
                    ]
            },
        'Ricardo Medeiros':
            {
                'image': 'https://lh3.googleusercontent.com/-AfUOQdW-5zU/AAAAAAAAAAI/AAAAAAAAIbM/XO-Cf-sTbA8/s120-c/photo.jpg',
                'description':'<p>Cara a cara eu gaguejo, tenho dúvidas, sou pouco sociável. Mas, escrevendo, cuidado comigo.</p>',
                'links': [
                    '<a href="https://twitter.com/rictm" class="label label-default"><i class="fa fa-twitter"></i> Twitter</a>',
                ]
            },
        'Gilson Filho':
            {
                'image': 'https://lh6.googleusercontent.com/-WqpgBkIaepM/AAAAAAAAAAI/AAAAAAAAAJI/W2sWTkMnv1I/s120-c/photo.jpg',
                'description': '<p>Desenvolvedor Python e Django, cansado de Java, recém carioca. Entusiasta Vim e usuário assíduo do <a href="http://github.com/gilsondev">Github</a></p>',
                'links': [
                    '<a href="https://twitter.com/gilsondev" class="label label-default"><i class="fa fa-twitter"></i> Twitter</a>',
                    '<a href="https://github.com/gilsondev" class="label label-default"><i class="fa fa-github"></i> Github</a>',
                ]
            },
        }

