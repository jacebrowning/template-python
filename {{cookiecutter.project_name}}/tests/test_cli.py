{%- if cookiecutter.test_runner == "nose" -%}
"""Sample integration test module using nose."""
# pylint: disable=no-self-use,missing-docstring

import unittest

from click.testing import CliRunner

from {{cookiecutter.package_name}}.cli import main


class Test{{cookiecutter.package_name | capitalize}}(unittest.TestCase):
    """Sample integration test class."""

    def test_conversion(self):
        runner = CliRunner()
        result = runner.invoke(main, ['42'])

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, "12.80165\n")
{% elif cookiecutter.test_runner == "pytest" -%}
"""Sample integration test module using pytest-describe and expecter."""
# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

import pytest
from expecter import expect

from click.testing import CliRunner

from {{cookiecutter.package_name}}.cli import main


@pytest.fixture
def runner():
    return CliRunner()


def describe_cli():

    def describe_conversion():

        def when_integer(runner):
            result = runner.invoke(main, ['42'])

            expect(result.exit_code) == 0
            expect(result.output) == "12.80165\n"

        def when_invalid(runner):
            result = runner.invoke(main, ['foobar'])

            expect(result.exit_code) == 0
            expect(result.output) == ""
{% endif -%}
