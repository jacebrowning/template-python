# template-python

A Python 3 project template for [cookiecutter][cookiecutter]

[![Build Status](http://img.shields.io/travis/jacebrowning/template-python/master.svg)](https://travis-ci.org/jacebrowning/template-python)
[![Coverage Status](http://img.shields.io/coveralls/jacebrowning/template-python/master.svg)](https://coveralls.io/r/jacebrowning/template-python)
[![Scrutinizer Code Quality](http://img.shields.io/scrutinizer/g/jacebrowning/template-python.svg)](https://scrutinizer-ci.com/g/jacebrowning/template-python/?branch=master)

# Get Started!

    $ pip install cookiecutter
    $ cookiecutter https://github.com/jacebrowning/template-python.git

Cookiecutter will ask you some basic info (your name, project name, python package name, etc.) and generate a base Python 3 project for you.

# Features

* Preconfigured setup for [Travis-CI][travis], [Coveralls][coveralls], and [Scrutinizer][scrutinizer]
* `Makefile` for automating common development tasks:
    - Setting up a `virtualenv`
    - Installing dependencies using `pip`
    - Running tests
    - Running style checkers (`pep8`/`pep257`) and linters (`pylint`)
    - Building documentation
    - Creating and releasing distributions to PyPi

[cookiecutter]: https://github.com/audreyr/cookiecutter
[travis]: https://travis-ci.org/
[coveralls]: https://coveralls.io/
[scrutinizer]: https://scrutinizer-ci.com/
