Foobar
======

[![Build Status](http://img.shields.io/travis/jacebrowning/template-python/master.svg)](https://travis-ci.org/jacebrowning/template-python)
[![Coverage Status](http://img.shields.io/coveralls/jacebrowning/template-python/master.svg)](https://coveralls.io/r/jacebrowning/template-python)
[![Scrutinizer Code Quality](http://img.shields.io/scrutinizer/g/jacebrowning/template-python.svg)](https://scrutinizer-ci.com/g/jacebrowning/template-python/?branch=master)
[![PyPI Version](http://img.shields.io/pypi/v/foobar.svg)](https://pypi.python.org/pypi/foobar)
[![PyPI Downloads](http://img.shields.io/pypi/dm/foobar.svg)](https://pypi.python.org/pypi/foobar)

This is a template for a typical Python library following modern packaging conventions. It utilizes popular libraries alongside Make, Graphviz, and Pandoc to fully automate all development and deployment tasks. To adopt for a new project:

* replace `foobar` and `template-python` with your package name
* replace `Foobar` with your project name (might be the same as the package)
* set `TEST_RUNNER` in the `Makefile` to your preferred test runner (`nose` or `pytest`)
* remove the `TEST_RUNNER` environment lines in `.travis.yml`
* update the links to point to your code repository and badges
* change the license

Here are few sample projects based on this template:

* [jacebrowning/yorm](https://github.com/jacebrowning/yorm)
* [MichiganLabs/flask-gcm](https://github.com/MichiganLabs/flask-gcm)
* [theovoss/BoggleSolver](https://github.com/theovoss/BoggleSolver)

Getting Started
===============

Requirements
------------

* Python 2.7+ or Python 3.3+

Installation
------------

Foobar can be installed with pip:

```shell
$ pip install Foobar
```

or directly from the source code:

```shell
$ git clone https://github.com/jacebrowning/template-python.git
$ cd template-python
$ python setup.py install
```

Basic Usage
===========

After installation, abstract base classes can be imported from the package:

```shell
$ python
>>> import foobar
foobar.__version__
```

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

```shell
$ make env
```

Run the tests:

```shell
$ make test
$ make tests  # includes integration tests
```

Build the documentation:

```shell
$ make doc
```

Run static analysis:

```shell
$ make pep8
$ make pep257
$ make pylint
$ make check  # includes all checks
```

Prepare a release:

```shell
$ make dist  # dry run
$ make upload
```
