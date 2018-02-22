{%- if cookiecutter.test_runner == "nose" -%}
"""Sample unit test module using nose."""

import unittest

from {{cookiecutter.package_name}} import utils


class Test{{cookiecutter.package_name | capitalize}}(unittest.TestCase):
    """Sample unit test class."""

    def test_conversion_is_correct(self):
        self.assertEqual(utils.feet_to_meters(42), 12.80165)

    def test_invalid_inputs_are_handled(self):
        self.assertEqual(utils.feet_to_meters("hello"), None)
{% elif cookiecutter.test_runner == "pytest" -%}
"""Sample unit test module using pytest-describe and expecter."""
# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

from {{cookiecutter.package_name}} import utils


def describe_feet_to_meters():

    def when_integer(expect):
        expect(utils.feet_to_meters(42)) == 12.80165

    def when_string(expect):
        expect(utils.feet_to_meters("hello")) == None
{% endif -%}
