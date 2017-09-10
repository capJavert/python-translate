import click
from gtoken import TokenAcquirer
import requests

# !/usr/bin/python
# -*- coding: utf8 -*-
__author__ = '@capJavert'


@click.command()
@click.option('--text', '-t', default="", help='Text that you wish to translate. For supported languages check '
                                               'https://en.wikipedia.org/wiki/Google_Translate#Supported_languages')
@click.option('--source-lang', '-s', default="auto", help='Source language.'
                                                          'Default is auto detect language.')
@click.option('--destination-lang', '-d', default="en", help='Destination language for translation. '
                                                             'Default is English')
def main(text, source_lang, destination_lang):
    if text == "":
        print("You are missing text param. Use --help for more info.")
        return

    acquirer = TokenAcquirer()
    token = acquirer.do(text)

    url = 'https://translate.google.com/translate_a/single?client=t' \
          '&sl=' + source_lang + \
          '&tl=' + destination_lang + \
          '&hl=en' \
          '&dt=at' \
          '&dt=bd' \
          '&dt=ex' \
          '&dt=ld' \
          '&dt=md' \
          '&dt=qca' \
          '&dt=rw' \
          '&dt=rm' \
          '&dt=ss' \
          '&dt=t' \
          '&ie=UTF-8' \
          '&oe=UTF-8' \
          '&otf=2' \
          '&ssel=0' \
          '&tsel=0' \
          '&kc=2' \
          '&tk=' + token + \
          '&q=' + text

    request = requests.get(url)

    print(request.content.split('",')[0].replace('[[["', ''))

    return


main()
