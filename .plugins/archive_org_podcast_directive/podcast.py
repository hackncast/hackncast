# -*- coding: utf-8 -*-

#from __future__ import unicode_literals

from docutils import nodes
from docutils.parsers.rst import directives, Directive


class Podcast(Directive):
    """ Include podcast

    Usage:
    .. podcast:: TITLE
        :rss: link
        :itunes: link
    """

    required_arguments = 1
    optional_arguments = 2
    option_spec = {
            'rss': str,
            'itunes': str,
            }

    final_argument_whitespace = False
    has_content = False

    def run(self):

        title = self.arguments[0].strip()

        rss = u''
        itunes = u''

        if 'rss' in self.options:
            rss = self.options['rss']

        if 'itunes' in self.options:
            itunes = self.options['itunes']

        HTML = """
        <div class="podcast text-center">
            <audio class="podcast-player" controls>
                    <source src="https://archive.org/download/{title}/{title}.ogg" type="audio/ogg" />
                    <source src="https://archive.org/download/{title}/{title}.mp3" type="audio/mpeg" />
                    Seu navegador não suporta este objeto. Baixe o podcast abaixo....
            </audio>

            <div class="podcast-download">
                <span class="label label-success"><a href="https://archive.org/download/{title}/{title}.mp3"><i class="fa fa-download"></i> Download MP3</a></span>
                <span class="label label-success"><a href="https://archive.org/download/{title}/{title}.ogg"><i class="fa fa-download"></i> Download OGG</a></span>
                <span class="label label-success"><a href="https://archive.org/download/{title}/{title}_vbr_mp3.zip"><i class="fa fa-download"></i> Download ZIP</a></span>
            </div>
            <div class="podcast-subscribe">
                <span class="label label-success"><a href="{podcast_rss}"><i class="fa fa-rss"></i> Assinar Feed RSS</a></span>
                <span class="label label-success"><a href="{podcast_itunes}"><i class="fa fa-apple"></i> Assinar no iTunes</a></span>
            </div>
        </div>
        """.format(title=title, podcast_rss=rss, podcast_itunes=itunes)

        return [nodes.raw('', HTML, format='html')]


def register():
    directives.register_directive('podcast', Podcast)
