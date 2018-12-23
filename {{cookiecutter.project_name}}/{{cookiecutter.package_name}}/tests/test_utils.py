"""Sample unit test module using pytest-describe and expecter."""
# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

from {{cookiecutter.package_name}} import utils


def describe_feet_to_meters():

    def when_integer(expect):
        expect(utils.feet_to_meters(42)) == 12.80165

    def when_string(expect):
        expect(utils.feet_to_meters("hello")) == None
