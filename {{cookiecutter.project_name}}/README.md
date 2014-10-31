{{cookiecutter.project_name}}
======
{{cookiecutter.project_short_description}}

[![Build Status](http://img.shields.io/travis/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/master.svg)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_name}})
[![Coverage Status](http://img.shields.io/coveralls/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/master.svg)](https://coveralls.io/r/{{cookiecutter.github_username}}/{{cookiecutter.project_name}})
[![Scrutinizer Code Quality](http://img.shields.io/scrutinizer/g/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.svg)](https://scrutinizer-ci.com/g/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/?branch=master)
[![PyPI Version](http://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg)](https://pypi.python.org/pypi/{{cookiecutter.project_name}})
[![PyPI Downloads](http://img.shields.io/pypi/dm/{{cookiecutter.project_name}}.svg)](https://pypi.python.org/pypi/{{cookiecutter.project_name}})


Getting Started
===============

Requirements
------------

* Python 2.7+ or Python 3.3+

Installation
------------

{{cookiecutter.project_name}} can be installed with pip:

```shell
$ pip install {{cookiecutter.project_name}}
```

or directly from the source code:

```shell
$ git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.git
$ cd {{cookiecutter.project_name}}
$ python setup.py install
```

Basic Usage
===========

After installation, abstract base classes can be imported from the package:

```shell
$ python
>>> import {{cookiecutter.project_name}}
{{cookiecutter.package_name}}.__version__
```

{{cookiecutter.project_name}} doesn't do anything, it's a template.

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
