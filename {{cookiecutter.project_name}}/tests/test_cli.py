"""Sample integration test module using pytest-describe and expecter."""
# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned

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
