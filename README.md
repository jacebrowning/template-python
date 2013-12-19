Foobar
======

Foobar is a template for a typical Python library package.

To adopt for a new project:

* change the license
* change Foobar/foobar to your project/package name (they might be the same)



Getting Started
===============

Requirements
------------

* Python 3: http://www.python.org/download/releases/3.3.3/#download


Installation
------------

Foobar can be installed with ``pip`` or ``easy_install``:

    pip install Foobar

Or directly from the source code:

    python setup.py install



Basic Usage
===========

After installation, abstract base classes can be imported from the package:

    python
    >>> import foobar
    foobar.__version__

Foobar doesn't do anything, it's a template.



For Developers
==============

Requirements
------------
* Python 3: http://www.python.org/download/releases/3.3.3/#download
* GNU Make:
    * Windows: http://cygwin.com/install.html
    * Mac: https://developer.apple.com/xcode
    * Linux: http://www.gnu.org/software/make (likely already installed)
* virtualenv: https://pypi.python.org/pypi/virtualenv#installation
* Pandoc: http://johnmacfarlane.net/pandoc/installing.html


Environment
-----------

Create a virtualenv:

    make develop

Run static analysis:

    make doc
    make pep8
    make pylint
    make check  # all of the above

Run the tests:

    make test
    make tests  # includes integration tests
