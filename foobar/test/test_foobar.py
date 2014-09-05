#!/usr/bin/env python

import unittest


class TestFooBar(unittest.TestCase):
    def test_dependency_import(self):
        try:
            import testpackage
            assert True
        except ImportError:
            assert False
