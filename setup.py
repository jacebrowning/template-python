#!/usr/bin/env python

"""
Setup script for Foobar.
"""

import setuptools

from foobar import __project__

# Touch the README, it will be generated on release
README = 'README.rst'
import os
if not os.path.exists(README):
    open(README, 'wb').close()


setuptools.setup(
    name=__project__,
    version='0.0.0',

    description="Python package template.",
    url='http://pypi.python.org/pypi/Foobar',
    author='Jace Browning',
    author_email='jacebrowning@gmail.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': []},

    long_description=open(README).read(),
    license='WTFPL',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],

    install_requires=[],
)
