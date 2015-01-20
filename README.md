# template-python

A Python project template for [cookiecutter][cookiecutter].

[![Build Status](http://img.shields.io/travis/jacebrowning/template-python/master.svg)](https://travis-ci.org/jacebrowning/template-python)

This is a template for a typical Python library following modern packaging conventions. It utilizes popular libraries alongside Make, Pandoc, and Graphviz to fully automate all development and deployment tasks.

A live demo of this template: [jacebrowning/template-python-demo](https://github.com/jacebrowning/template-python-demo)

And a few sample projects based on this template:

* [flask-restful/flask-restful](https://github.com/flask-restful/flask-restful)
* [jacebrowning/doorstop](https://github.com/jacebrowning/doorstop)
* [theovoss/BoggleSolver](https://github.com/theovoss/BoggleSolver)
* [MichiganLabs/flask-gcm](https://github.com/MichiganLabs/flask-gcm)

## Get Started

    $ pip install cookiecutter>=0.9.1
    $ cookiecutter gh:jacebrowning/template-python

Cookiecutter will ask you for some basic info (your name, project name, python package name, etc.) and generate a base Python project for you.

## Features

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
