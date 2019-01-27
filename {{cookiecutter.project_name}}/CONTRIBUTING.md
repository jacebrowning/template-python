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

```text
$ make doctor
```

## Installation

Install project dependencies into a virtual environment:

```text
$ make install
```

# Development Tasks

## Manual

Run the tests:

```text
$ make test
```

Run static analysis:

```text
$ make check
```

Build the documentation:

```text
$ make docs
```

## Automatic

Keep all of the above tasks running on change:

```text
$ make watch
```

> In order to have OS X notifications, `brew install terminal-notifier`.

# Continuous Integration

The CI server will report overall build status:

```text
$ make ci
```

# Release Tasks

Release to PyPI:

```text
$ make upload
```
