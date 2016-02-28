#!/usr/bin/python
# -*- coding: utf8 -*-
__author__ = 'Ante Barić @capJavert'

import click
import requests

@click.command()
@click.option('--word', '-w', default="", help='Word that you wish to translate.')
@click.option('--lang', '-l', default="en", help='Language in which word is wrote ("en" or "hr"). Default is english language.')
def main(word, lang):
    if word=="":
        print("     You are missing --word param. Use --help for more info.")
        return

    url = 'http://www.design-ers.net/eh-rjecnik.asp'

    form_data = {
        'rijec': word.encode("Windows-1250"),
        'lang': lang,
        'Submit': 'Prevedi',
    }

    response = requests.post(url, data=form_data)
    response.encoding = 'Windows-1250'

    i = 0;
    translations = '     translation is not available :('
    for line in response.text.splitlines():
        i = i + 1;
        if (i==115) and (line!='     data-ad-client="ca-pub-9335582685562862"'):
            translations = line

    print(translations)
    return

main()