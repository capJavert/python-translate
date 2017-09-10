# Translate
[![Build Status](https://travis-ci.org/capJavert/python-translate.svg?branch=master)](https://travis-ci.org/capJavert/python-translate)
## Simple command line tool for translation using google translation api
### Install
You will need pip tool for python to install renamer into your shell environment.

Pip is included in python 3.x+

Tool is compatible with python 2.7+

$ git clone https://github.com/capJavert/python-translate.git python-translate

$ cd python-translate

$ pip install --editable . (you have to be root on linux or use sudo)

After install you can use script as:

$ translate --word=woman or shorter $ translate -w woman
### Usage
Usage: translate [OPTIONS]

Options:
  -t, --text TEXT              Text that you wish to translate. 
                               For supported languages check https://en.wikipedia.org/wiki/Google_Translate#Supported_languages
                               
  -s, --source-lang TEXT       Source language. Default is auto detect language.
                               
  -d, --destination-lang TEXT  Destination language for translation. Default is English
                               
  --help                       Show this message and exit.

### Credits
Using modified https://github.com/ssut/py-googletrans/blob/master/googletrans/gtoken.py gtoken generation algorithm that is reverse engineered from Google Translate Web JS script.