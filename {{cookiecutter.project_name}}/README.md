Unix: [![Unix Build Status](https://img.shields.io/travis/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}/{{cookiecutter.default_branch}}.svg)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}) Windows: [![Windows Build Status](https://img.shields.io/appveyor/ci/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}/{{cookiecutter.default_branch}}.svg)](https://ci.appveyor.com/project/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}})<br>Metrics: [![Coverage Status](https://img.shields.io/coveralls/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}/{{cookiecutter.default_branch}}.svg)](https://coveralls.io/r/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}) [![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}.svg)](https://scrutinizer-ci.com/g/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}/?branch={{cookiecutter.default_branch}})<br>Usage: [![PyPI Version](https://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg)](https://pypi.org/project/{{cookiecutter.project_name}})

# Overview

{{cookiecutter.project_short_description}}

This project was generated with [cookiecutter](https://github.com/audreyr/cookiecutter) using [jacebrowning/template-python](https://github.com/jacebrowning/template-python).

# Setup

## Requirements

* Python {{cookiecutter.python_major_version}}.{{cookiecutter.python_minor_version}}+

## Installation

Install {{cookiecutter.project_name}} with pip:

```sh
$ pip install {{cookiecutter.project_name}}
```

or directly from the source code:

```sh
$ git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}.git
$ cd {{cookiecutter.github_repo}}
$ python setup.py install
```

# Usage

After installation, the package can imported:

```sh
$ python
>>> import {{cookiecutter.package_name}}
>>> {{cookiecutter.package_name}}.__version__
```
