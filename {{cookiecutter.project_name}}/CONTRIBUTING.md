# Setup

## Requirements

* Make:
    * macOS: `$ xcode-select --install`
    * Linux: [https://www.gnu.org/software/make](https://www.gnu.org/software/make)
    * Windows: [https://mingw.org/download/installer](https://mingw.org/download/installer)
* Python: `$ pyenv install`
* Poetry: [https://poetry.eustace.io/docs/#installation](https://poetry.eustace.io/docs/#installation)
* Graphviz:
    * macOS: `$ brew install graphviz`
    * Linux: [https://graphviz.org/download](https://graphviz.org/download/)
    * Windows: [https://graphviz.org/download](https://graphviz.org/download/)

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

# Demo Tasks

Run the program:

```text
$ make run
````

Launch an IPython session:

```text
$ make ipython
```

# Release Tasks

Release to PyPI:

```text
$ make upload
```
