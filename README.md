Foobar
======

[![Build Status](http://img.shields.io/travis/jacebrowning/template-python/master.svg)](https://travis-ci.org/jacebrowning/template-python)
[![Coverage Status](http://img.shields.io/coveralls/jacebrowning/template-python/master.svg)](https://coveralls.io/r/jacebrowning/template-python)
[![Scrutinizer Code Quality](http://img.shields.io/scrutinizer/g/jacebrowning/template-python.svg)](https://scrutinizer-ci.com/g/jacebrowning/template-python/?branch=master)
[![PyPI Version](http://img.shields.io/pypi/v/Foobar.svg)](https://pypi.python.org/pypi/Foobar)
[![PyPI Downloads](http://img.shields.io/pypi/dm/Foobar.svg)](https://pypi.python.org/pypi/Foobar)

This is a template for a typical Python library following modern packaging conventions. It utilizes popular Python libraries, external tools, and web services to fully automate all development and deployment tasks. 

Here are few sample projects to see this template in action:

* [jacebrowning/doorstop](https://github.com/jacebrowning/doorstop)
* [MichiganLabs/flask-gcm](https://github.com/MichiganLabs/flask-gcm)
* [theovoss/BoggleSolver](https://github.com/theovoss/BoggleSolver)

To adopt for your next project:

* download this repository's [source code](https://github.com/jacebrowning/template-python/archive/master.zip) to a new directory
* set `PYTHON_MAJOR` and `PYTHON_MINOR` in the `Makefile` to your default Python version
* set `TEST_RUNNER` in the `Makefile` to your preferred test runner (`nose` or `pytest`)
* remove the `TEST_RUNNER` [environment lines](https://github.com/jacebrowning/template-python/blob/850cdcbcfec99d9d844482761ed5492274720687/.travis.yml#L6-8) in `.travis.yml`
* replace all instances of `foobar` and `template-python` with your package name
* replace all instances of `Foobar` with your project name (might be the same as the package)
* update all links to point to your code repository and badges
* change the license
* replace all the above text with your project's description

Getting Started
===============

Requirements
------------

* Python 2.7+ or Python 3.3+

Installation
------------

Foobar can be installed with pip:

```
$ pip install Foobar
```

or directly from the source code:

```
$ git clone https://github.com/jacebrowning/template-python.git
$ cd template-python
$ python setup.py install
```

Basic Usage
===========

After installation, abstract base classes can be imported from the package:

```
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

```
$ make env
```

Run the tests:

```
$ make test
$ make tests  # includes integration tests
```

Build the documentation:

```
$ make doc
```

Run static analysis:

```
$ make pep8
$ make pep257
$ make pylint
$ make check  # includes all checks
```

Prepare a release:

```
$ make dist  # dry run
$ make upload
```
