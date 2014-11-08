#!/usr/bin/env python

"""Sample test module."""

import unittest

from {{cookiecutter.package_name}} import sample


class Test{{cookiecutter.package_name | capitalize}}(unittest.TestCase):

    """Sample test class."""

    def test_dependency_import(self):
        """Sample test method for dependencies."""
        try:
            import testpackage  # pylint: disable=W0612
            assert True
        except ImportError:
            self.fail("depenency not installed")

    def test_dependency_import_special(self):
        """Sample test method for special dependencies."""
        try:
            import newrelic_plugin_agent  # pylint: disable=W0612
            assert True
        except ImportError:
            self.fail("depenency not installed")

    def test_foobar(self):
        """Sample test method for branch coverage."""
        self.assertEquals(sample.foobar(True), 'True')
        self.assertEquals(sample.foobar(False), 'False')
        self.assertEquals(sample.foobar(None), 'None')
