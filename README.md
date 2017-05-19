# Translate
[![Build Status](https://travis-ci.org/capJavert/python-translate.svg?branch=master)](https://travis-ci.org/capJavert/python-translate)
## Simple command line tool for croatian/english translation
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

  -w, --word TEXT  Word that you wish to translate.
  
  -l, --lang TEXT  Language in which word is wrote ("en" or "hr"). Default is english language.
  
  --help       Show this message and exit.

### Credits
Thanks to http://www.design-ers.net for such a cool and fast translation website

My tool only sends request to there website i do not own a translation algorithm or word database.

### To do
- Add other languages
