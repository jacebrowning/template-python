Foobar
======

[![Build Status](https://travis-ci.org/jacebrowning/template-python.png?branch=master)](https://travis-ci.org/jacebrowning/template-python)
[![Coverage Status](https://coveralls.io/repos/jacebrowning/template-python/badge.png?branch=master)](https://coveralls.io/r/jacebrowning/template-python?branch=master)
[![PyPI Version](https://badge.fury.io/py/Foobar.png)](http://badge.fury.io/py/Foobar)

Foobar is a template for a typical Python 3 library package.

To adopt for a new project:

* replace foobar/template-python with your package name
* replace Foobar with your project name (might be the same as the project)
* update the links to point to your code repository and badges
* change the license



Getting Started
===============

Requirements
------------

* Python 3.3: http://www.python.org/download/releases/3.3.4/#download


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
