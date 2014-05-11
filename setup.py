#!/usr/bin/env python

"""
Setup script for Foobar.
"""

import setuptools

from foobar import __project__, __version__

import os
if os.path.exists('README.rst'):
    README = open('README.rst').read()
else:
    README = ""  # a placeholder, readme is generated on release
CHANGES = open('CHANGES.md').read()


setuptools.setup(
    name=__project__,
    version=__version__,

    description="Foobar is a Python 3 package template.",
    url='http://pypi.python.org/pypi/Foobar',
    author='Jace Browning',
    author_email='jacebrowning@gmail.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': ['foobar = foobar.main:main']},

    long_description=(README + '\n' + CHANGES),
    license='WTFPL',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
    ],

    install_requires=[],
)
