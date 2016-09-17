#!/usr/bin/env python

"""Sample package entry point."""

import sys
import logging
from os.path import abspath, dirname

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from demo import sample  # pylint: disable=wrong-import-position


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    sample.Application()
