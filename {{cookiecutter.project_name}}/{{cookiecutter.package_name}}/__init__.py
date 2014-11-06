#!/usr/bin/env python

"""Package for Foobar."""

__project__ = 'Foobar'
__version__ = '0.0.0'

VERSION = __project__ + '-' + __version__


def foobar(value):
    """A function with branches to demonstrate branch coverage reporting."""
    if value is True:
        return 'True'
    elif value is False:
        return 'False'
    else:
        return 'None'
