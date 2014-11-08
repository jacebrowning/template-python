"""A sample module."""


def foobar(value):
    """A function with branches to demonstrate branch coverage reporting."""
    if value is True:
        return 'True'
    elif value is False:
        return 'False'
    else:
        return 'None'
