from setuptools import setup

__author__ = '@capJavert'

setup(
    name='python-translate',
    version='0.2.0',
    summary='shell tool',
    homepage='https://github.com/capJavert/python-translate',
    author='capJavert',
    author_email='/',
    license='MIT',
    description='Simple command line tool for croatian/english translation',
    platforms='windows, linux, os x',

    py_modules=['translate'],
    install_requires=[
        'Click',
        'Requests',
        'lxml',
    ],
    entry_points='''
        [console_scripts]
        translate=translate:main
    ''',
)
