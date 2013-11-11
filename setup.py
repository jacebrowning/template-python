#!/usr/bin/env python

"""
Setup script for Comparable.
"""

import setuptools

from foobar import __project__

setuptools.setup(
    name=__project__,
    version='0.0.0',

    description="Python package template.",
    url='http://pypi.python.org/pypi/Foobar',
    author='Jace Browning',
    author_email='jace.browning@gmail.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': []},


    long_description=open('README.rst').read(),
    license='WTFPL',

    install_requires=[],
)
