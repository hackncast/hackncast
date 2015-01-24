# -*- coding: utf-8 -*-
"""
Tipue Search
============

A Pelican plugin to serialize generated HTML to JSON
that can be used by jQuery plugin - Tipue Search.

Copyright (c) Talha Mansoor
"""

from __future__ import unicode_literals

import os.path
import json
from codecs import open
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

from pelican import signals

VALID_SORTING = (
    'alphabetically',
    'alphabetically-rev',
    'weight',
    'weight-rev',
    )


class StaticAPIGenerator(object):
    def __init__(self, context, settings, path, theme, output_path):
        self.siteurl = settings.get('SITEURL') or '/'
        self.context = context
        self.settings = settings
        self.path = path
        self.theme = theme
        self.base_output_path = output_path

        self.tag_cloud_sorting = settings.get('STATIC_API_TAGCLOUD_SORTING')
        if self.tag_cloud_sorting not in VALID_SORTING:
            self.tag_cloud_sorting = 'alphabetically'

        self.base_path = os.path.join(
            output_path,
            settings.get('STATIC_API_PATH') or 'api'
            )

        self.api_mapper = {
            'tag_cloud': {
                'filename': 'tag_cloud.json',
                'func': self.generate_tag_cloud_api,
                },
            'tags': {
                'filename': 'tags.json',
                'func': self.generate_tags_api,
                },
            'categories': {
                'filename': 'categories.json',
                'func': self.generate_categories_api,
                },
            'authors': {
                'filename': 'authors.json',
                'func': self.generate_authors_api,
                },
            'pages': {
                'filename': 'pages.json',
                'func': self.generate_pages_api,
                },
            'articles': {
                'filename': 'articles.json',
                'func': self.generate_articles_api,
                },
            }
        for context_name in self.api_mapper:
            filename = settings.get(
                'STATIC_API_{}_FILENAME'.format(context_name.upper())
                )
            if filename:
                self.api_mapper[context_name]['filename'] = filename

    def generate_output(self, writer):
        for context in self.api_mapper.values():
            output = context['func']()
            if not output:
                continue
            self.write_json(output, context['filename'])

    def generate_tag_cloud_api(self):
        tags = self.context['tags']
        content = []
        for tag, articles in tags:
            element = {
                'text': tag.name,
                'slug': tag.slug,
                'weight': len(articles),
                'link': urljoin(self.siteurl, tag.url),
                }
            content.append(element)

        if self.tag_cloud_sorting == 'alphabetically':
            content.sort(key=lambda e: e['slug'])
        elif self.tag_cloud_sorting == 'alphabetically-rev':
            content.sort(key=lambda e: e['slug'], reverse=True)
        elif self.tag_cloud_sorting == 'weight':
            content.sort(key=lambda e: e['weight'])
        elif self.tag_cloud_sorting == 'weight-rev':
            content.sort(key=lambda e: e['weight'], reverse=True)
        return content

    def generate_tags_api(self):
        tags = self.context['tags']
        content = []
        for tag, articles in tags:
            element = {
                'text': tag.name,
                'slug': tag.slug,
                'link': urljoin(self.siteurl, tag.url),
                'articles': [],
                }
            for article in articles:
                element['articles'].append({
                    'text': article.title,
                    'slug': article.slug,
                    'link': urljoin(self.siteurl, article.url),
                    })
            content.append(element)

        content.sort(key=lambda e: e['slug'])
        return content

    def generate_categories_api(self):
        content = []
        categories = self.context['categories']

        for category, articles in categories:
            element = {
                'text': category.name,
                'slug': category.slug,
                'link': urljoin(self.siteurl, category.url),
                'articles': [],
                }
            for article in articles:
                element['articles'].append({
                    'text': article.title,
                    'slug': article.slug,
                    'link': urljoin(self.siteurl, article.url),
                    })
            content.append(element)

        content.sort(key=lambda e: e['slug'])
        return content

    def generate_authors_api(self):
        content = []
        authors = self.context['authors']

        for author, articles in authors:
            element = {
                'text': author.name,
                'slug': author.slug,
                'link': urljoin(self.siteurl, author.url),
                'articles': [],
                }
            for article in articles:
                element['articles'].append({
                    'text': article.title,
                    'slug': article.slug,
                    'link': urljoin(self.siteurl, article.url),
                    })
            content.append(element)

        content.sort(key=lambda e: e['slug'])
        return content

    def generate_pages_api(self):
        content = []
        pages = self.context['pages']

        for page in pages:
            if page.status != 'published':
                continue

            element = {
                'text': page.title,
                'slug': page.slug,
                'link': urljoin(self.siteurl, page.url),
                'lang': page.lang,
                'authors': [],
                }
            for author in page.authors:
                element['authors'].append({
                    'text': author.name,
                    'slug': author.slug,
                    'link': urljoin(self.siteurl, author.url),
                    })
            content.append(element)

        content.sort(key=lambda e: e['slug'])
        return content

    def generate_articles_api(self):
        content = []
        articles = self.context['articles']

        for article in articles:
            if article.status != 'published':
                continue

            element = {
                'text': article.title,
                'slug': article.slug,
                'category': {
                    'text': article.category.name,
                    'slug': article.category.slug,
                    'link': urljoin(self.siteurl, article.category.url),
                    },
                'link': urljoin(self.siteurl, article.url),
                'lang': article.lang,
                'authors': [],
                }
            for author in article.authors:
                element['authors'].append({
                    'text': author.name,
                    'slug': author.slug,
                    'link': urljoin(self.siteurl, author.url),
                    })
            content.append(element)

        content.sort(key=lambda e: e['slug'])
        return content

    def write_json(self, content, filename):
        path = os.path.join(self.base_path, filename)
        base_dir = os.path.dirname(path)
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        with open(path, 'w', encoding='utf-8') as fd:
            json.dump(content, fd, separators=(',', ':'), ensure_ascii=False)


def get_generators(generators):
    return StaticAPIGenerator


def register():
    signals.get_generators.connect(get_generators)
