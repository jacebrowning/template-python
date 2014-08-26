#!/usr/bin/env python

"""Package for Foobar."""

__project__ = 'Foobar'
__version__ = '0.0.0'

VERSION = __project__ + '-' + __version__

MIN_PYTHON_VERSION = 3, 4

import sys
if not sys.version_info >= MIN_PYTHON_VERSION:  # pragma: no cover (manual test)
    exit("Python %s.%s+ is required." % MIN_PYTHON_VERSION)
