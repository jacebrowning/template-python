#!/usr/bin/env python

"""Sample test module."""

import unittest

from {{cookiecutter.package_name}} import foobar


class Test{{cookiecutter.package_name | capitalize}}(unittest.TestCase):

    """Sample test class."""

    def test_dependency_import_1(self):
        """Sample test method 1."""
        try:
            import testpackage  # pylint: disable=W0612
            assert True
        except ImportError:
            self.fail("depenency not installed")

    def test_dependency_import_2(self):
        """Sample test method 2."""
        try:
            import newrelic_plugin_agent  # pylint: disable=W0612
            assert True
        except ImportError:
            self.fail("depenency not installed")

    def test_foobar(self):
        self.assertEquals(foobar(True), 'True')
        self.assertEquals(foobar(False), 'False')
        self.assertEquals(foobar(None), 'None')
