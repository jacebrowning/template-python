Foobar
======

[![Build Status](http://img.shields.io/travis/jacebrowning/template-python/master.svg)](https://travis-ci.org/jacebrowning/template-python)
[![Coverage Status](http://img.shields.io/coveralls/jacebrowning/template-python/master.svg)](https://coveralls.io/r/jacebrowning/template-python)
[![PyPI Version](http://img.shields.io/pypi/v/foobar.svg)](https://pypi.python.org/pypi/foobar)
[![PyPI Downloads](http://img.shields.io/pypi/dm/foobar.svg)](https://pypi.python.org/pypi/foobar)

Foobar is a template for a typical Python 3 library package.

To adopt for a new project:

* replace foobar/template-python with your package name
* replace Foobar with your project name (might be the same as the package)
* update the links to point to your code repository and badges
* change the license



Getting Started
===============

Requirements
------------

* Python 3.3+


Installation
------------

Foobar can be installed with 'pip':

    pip install Foobar

Or directly from the source code:

    git clone https://github.com/jacebrowning/template-python.git
    cd template-python
    python setup.py install



Basic Usage
===========

After installation, abstract base classes can be imported from the package:

    python
    >>> import foobar
    foobar.__version__

Foobar doesn't do anything, it's a template.



For Contributors
================

Requirements
------------

* GNU Make:
    * Windows: http://cygwin.com/install.html
    * Mac: https://developer.apple.com/xcode
    * Linux: http://www.gnu.org/software/make (likely already installed)
* virtualenv: https://pypi.python.org/pypi/virtualenv#installation
* Pandoc: http://johnmacfarlane.net/pandoc/installing.html
* Graphviz: http://www.graphviz.org/Download.php


Installation
------------

Create a virtualenv:

    make env

Run the tests:

    make test
    make tests  # includes integration tests

Build the documentation:

    make doc

Run static analysis:

    make pep8
    make pylint
    make check  # pep8 and pylint

Prepare a release:

    make dist  # dry run
    make upload
