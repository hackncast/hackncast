#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import re

from PIL import Image

WIDE_RW = re.compile('.*v[0-9]+.[0-9]+-cover-wide.jpg$')
SQR_RW = re.compile('.*v[0-9]+.[0-9]+-cover-sqr.jpg$')

SIZES = {
    'sqr': 500,
    'wide': 700,
    }


def lista_arquivos(path):
    images = []
    for root, folders, files in os.walk(path):
        files = map(os.sep.join, zip([root]*len(files), files))
        images += files
    return images


def redimensiona(image_path, width):
    image = Image.open(image_path)
    w, h = image.size
    proportion = float(w)/h
    height = int(float(width)/proportion)
    if w != width:
        print "Resizing %s from %s to %s" % (image_path, str((w, h)), str((width, height)))
        out = image.resize((width, height), Image.ANTIALIAS)
        out.save(image_path, quality=100)


def resize(path):
    arqs = lista_arquivos(path)
    sqr_images = filter(SQR_RW.match, arqs)
    wide_images = filter(WIDE_RW.match, arqs)
    sqr_images.sort()
    wide_images.sort()

    for image in sqr_images:
        redimensiona(image, SIZES['sqr'])

    for image in wide_images:
        redimensiona(image, SIZES['wide'])


def lista(path):
    arqs = lista_arquivos(path)
    sqr_images = filter(SQR_RW.match, arqs)
    wide_images = filter(WIDE_RW.match, arqs)
    sqr_images.sort()
    wide_images.sort()
    print "Covers Wide:"
    for image_path in wide_images:
        image = Image.open(image_path)
        w, h = image.size
        print image_path, (w, h), image.getbands()

    print "\nCovers Sqr:"
    for image_path in sqr_images:
        image = Image.open(image_path)
        w, h = image.size
        print image_path, (w, h), image.getbands()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Utilização incorreta!"
        print "Utilização: %s [list|resize] <caminho_de_covers>" % sys.argv[0]
        exit(1)

    if sys.argv[1] not in ('list', 'resize'):
        print "Favor informar uma operação válida!"
        print "Utilização: %s [list|resize] <caminho_de_covers>" % sys.argv[0]
        exit(1)

    if not os.path.exists(sys.argv[2]):
        print "Caminho não encontrado: %s" % sys.argv[1]
        exit(1)

    if sys.argv[1] == 'list':
        lista(sys.argv[2])
    else:
        resize(sys.argv[2])
