# For Contributors

## Setup

### Requirements

* Make:
    * Windows: http://cygwin.com/install.html
    * Mac: https://developer.apple.com/xcode
    * Linux: http://www.gnu.org/software/make (likely already installed)
* Pandoc: http://johnmacfarlane.net/pandoc/installing.html
* Graphviz: http://www.graphviz.org/Download.php

### Installation

Create a virtual environment:

```
$ make env
```

## Development Tasks

### Testing

Manually run the tests:

```
$ make test
$ make tests  # includes integration tests
```

or keep them running on change:

```
$ make watch
```

> In order to have OS X notifications, `brew install terminal-notifier`.

### Documentation

Build the documentation:

```
$ make doc
```

### Static Analysis

Run linters and static analyzers:

```
$ make pep8
$ make pep257
$ make pylint
$ make check  # includes all checks
```

## Continuous Integration

The CI server will report overall build status:

```
$ make ci
```

## Release Tasks

Release to PyPI:

```
$ make upload-test  # dry run upload to a test server
$ make upload
```
