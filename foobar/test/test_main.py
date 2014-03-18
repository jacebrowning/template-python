#!/usr/bin/env python

"""Tests for foobar.main."""

import unittest

from foobar import main


class Test(unittest.TestCase):

    def test_main(self):
        self.assertIs(None, main.main())


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
