"""Sample unit test module."""

import unittest

from {{cookiecutter.package_name}} import utils


class Test{{cookiecutter.package_name | capitalize}}(unittest.TestCase):
    """Sample unit test class."""

    def test_conversion_is_correct(self):
        self.assertEqual(utils.feet_to_meters(42), 12.80165)

    def test_invalid_inputs_are_handled(self):
        self.assertEqual(utils.feet_to_meters("hello"), None)
