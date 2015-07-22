"""Sample integration test module."""
# pylint: disable=no-self-use

import unittest

from {{cookiecutter.package_name}} import sample


class Test{{cookiecutter.package_name | capitalize}}(unittest.TestCase):

    """Sample integration test class."""

    def test_network_stuff(self):
        assert sample.function_with_network_stuff() is True

    def test_disk_stuff(self):
        assert sample.function_with_disk_stuff() is False
