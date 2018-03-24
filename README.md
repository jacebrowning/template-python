# template-python

Generates the structure for Python libraries using [cookiecutter][cookiecutter].

Unix: [![Unix Build Status](https://img.shields.io/travis/jacebrowning/template-python/master.svg)](https://travis-ci.org/jacebrowning/template-python)
Windows: [![Windows Build Status](https://img.shields.io/appveyor/ci/jacebrowning/template-python.svg)](https://ci.appveyor.com/project/jacebrowning/template-python)

This is a template for a typical Python library following modern packaging conventions. It utilizes popular libraries alongside Make, Pandoc, and Graphviz to fully automate all development and deployment tasks. Check out the live demo: [jacebrowning/template-python-demo](https://github.com/jacebrowning/template-python-demo)

Here are a few sample projects based on this template:

* [jacebrowning/sappy](https://github.com/jacebrowning/sappy)
* [theovoss/Chess](https://github.com/theovoss/Chess)
* [sprout42/StarStruct](https://github.com/sprout42/StarStruct)
* [MichiganLabs/flask-gcm](https://github.com/MichiganLabs/flask-gcm)
* [flask-restful/flask-restful](https://github.com/flask-restful/flask-restful)

If you are instead looking for a [Python application](https://caremad.io/posts/2013/07/setup-vs-requirement/) template, check out one of the sibling projects:

* [jacebrowning/template-django](https://github.com/jacebrowning/template-django)
* [jacebrowning/template-flask](https://github.com/jacebrowning/template-flask)

## Usage

Install `cookiecutter` and generate a project:

```
$ pip install cookiecutter
$ cookiecutter gh:jacebrowning/template-python -f
```

Cookiecutter will ask you for some basic info (your name, project name, python package name, etc.) and generate a base Python project for you.

If you still need to use legacy Python, older versions of this template are available on a branch:

```
$ cookiecutter gh:jacebrowning/template-python -f --checkout python2
```

## Features

* Preconfigured setup for [Travis-CI][travis], [Coveralls][coveralls], and [Scrutinizer][scrutinizer]
* `Makefile` for automating common development tasks:
    - Installing dependencies into a virtual environment using `pipenv`
    - Running tests
    - Running style checkers (`pycodestyle`/`pydocstyle`) and linters (`pylint`)
    - Building documentation
    - Creating and releasing distributions to PyPI

[cookiecutter]: https://github.com/audreyr/cookiecutter
[travis]: https://travis-ci.org/
[coveralls]: https://coveralls.io/
[scrutinizer]: https://scrutinizer-ci.com/

## Updates

Checkout the appropriate branch of [template-python-demo](https://github.com/jacebrowning/template-python-demo) and manually merge changes into your project.
