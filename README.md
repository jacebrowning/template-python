Foobar
======

[![Build Status](https://travis-ci.org/jacebrowning/template-python.png?branch=master)](https://travis-ci.org/jacebrowning/template-python)
[![Coverage Status](https://coveralls.io/repos/jacebrowning/template-python/badge.png?branch=master)](https://coveralls.io/r/jacebrowning/template-python?branch=master)

Foobar is a template for a typical Python library package.

To adopt for a new project:

* change Foobar/foobar to your project/package name (they might be the same)
* change the links to point to your code repository
* change the license



Getting Started
===============

Requirements
------------

* Python 3: http://www.python.org/download/releases/3.3.3/#download


Installation
------------

Foobar can be installed with ``pip``:

    pip install Foobar

Or directly from the source code:

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


Installation
------------

Create a virtualenv:

    make develop

Run the tests:

    make test
    make tests  # includes integration tests

Run static analysis:

    make doc
    make pep8
    make pylint
    make check  # all of the above
