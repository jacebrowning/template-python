Foobar
======

[![Build Status](https://travis-ci.org/jacebrowning/template-python.png?branch=master)](https://travis-ci.org/jacebrowning/template-python)
[![Coverage Status](https://coveralls.io/repos/jacebrowning/template-python/badge.png?branch=master)](https://coveralls.io/r/jacebrowning/template-python?branch=master)
[![PyPI Version](https://badge.fury.io/py/Foobar.png)](http://badge.fury.io/py/Foobar)

[![wercker status](https://app.wercker.com/status/7c50d732cc289a862cab2613b151e867/m/ "wercker status")](https://app.wercker.com/project/bykey/7c50d732cc289a862cab2613b151e867)

Foobar is a template for a typical Python 3 library package.

To adopt for a new project:

* replace Foobar/foobar with your project/package name (they might be the same)
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
