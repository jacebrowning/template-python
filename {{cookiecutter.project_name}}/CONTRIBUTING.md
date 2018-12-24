# Setup

## Requirements

* Make:
    * Windows: http://mingw.org/download/installer
    * Mac: http://developer.apple.com/xcode
    * Linux: http://www.gnu.org/software/make
* Python: `$ pyenv install`
* Poetry: https://poetry.eustace.io/docs/#installation
* Graphviz: http://www.graphviz.org/Download.php

To confirm these system dependencies are configured correctly:

```sh
$ make doctor
```

## Installation

Install project dependencies into a virtual environment:

```sh
$ make install
```

# Development Tasks

## Manual

Run the tests:

```sh
$ make test
```

Run static analysis:

```sh
$ make check
```

Build the documentation:

```sh
$ make docs
```

## Automatic

Keep all of the above tasks running on change:

```sh
$ make watch
```

> In order to have OS X notifications, `brew install terminal-notifier`.

# Continuous Integration

The CI server will report overall build status:

```sh
$ make ci
```

# Release Tasks

Release to PyPI:

```sh
$ make upload
```
