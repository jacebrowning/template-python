{{cookiecutter.project_name}}
======
{{cookiecutter.project_short_description}}

[![Build Status](http://img.shields.io/travis/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}/master.svg)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}})
[![Coverage Status](http://img.shields.io/coveralls/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}/master.svg)](https://coveralls.io/r/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}})
[![Scrutinizer Code Quality](http://img.shields.io/scrutinizer/g/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}.svg)](https://scrutinizer-ci.com/g/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}/?branch=master)
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

```
$ pip install {{cookiecutter.project_name}}
```

or directly from the source code:

```
$ git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}.git
$ cd {{cookiecutter.github_repo}}
$ python setup.py install
```

Basic Usage
===========

After installation, abstract base classes can be imported from the package:

```
$ python
>>> import {{cookiecutter.package_name}}
>>> {{cookiecutter.package_name}}.__version__
```

{{cookiecutter.project_name}} doesn't do anything, it's a template.

For Contributors
================

Requirements
------------

* Make:
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
