# template-python

A Python project template for [cookiecutter][cookiecutter]

[![Build Status](http://img.shields.io/travis/jacebrowning/template-python/master.svg)](https://travis-ci.org/jacebrowning/template-python)
[![Coverage Status](http://img.shields.io/coveralls/jacebrowning/template-python/master.svg)](https://coveralls.io/r/jacebrowning/template-python)
[![Scrutinizer Code Quality](http://img.shields.io/scrutinizer/g/jacebrowning/template-python.svg)](https://scrutinizer-ci.com/g/jacebrowning/template-python/?branch=master)

This is a template for a typical Python library following modern packaging conventions. It utilizes popular libraries alongside Make, Graphviz, and Pandoc to fully automate all development and deployment tasks.

Here are few sample projects based on this template:

* [jacebrowning/doorstop](https://github.com/jacebrowning/doorstop)
* [MichiganLabs/flask-gcm](https://github.com/MichiganLabs/flask-gcm)
* [theovoss/BoggleSolver](https://github.com/theovoss/BoggleSolver)

# Get Started!

    $ pip install cookiecutter
    $ cookiecutter https://github.com/jacebrowning/template-python.git

Cookiecutter will ask you for some basic info (your name, project name, python package name, etc.) and generate a base Python project for you.

After Cookiecutter creates your new project from the template:

* set `TEST_RUNNER` in the `Makefile` to your preferred test runner (`nose` or `pytest`)
* change the license

# Features

* Preconfigured setup for [Travis-CI][travis], [Coveralls][coveralls], and [Scrutinizer][scrutinizer]
* `Makefile` for automating common development tasks:
    - Setting up a `virtualenv`
    - Installing dependencies using `pip`
    - Running tests
    - Running style checkers (`pep8`/`pep257`) and linters (`pylint`)
    - Building documentation
    - Creating and releasing distributions to PyPI

[cookiecutter]: https://github.com/audreyr/cookiecutter
[travis]: https://travis-ci.org/
[coveralls]: https://coveralls.io/
[scrutinizer]: https://scrutinizer-ci.com/
