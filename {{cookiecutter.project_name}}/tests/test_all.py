"""Sample integration test module."""

import unittest

from {{cookiecutter.package_name}} import sample


class Test{{cookiecutter.package_name | capitalize}}(unittest.TestCase):

    """Sample integration test class."""

    def test_io_stuff(self):
        assert sample.function_that_does_io() is True
