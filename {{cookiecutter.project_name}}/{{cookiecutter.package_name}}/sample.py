"""A sample module."""


def function(value):
    """A function with branches to demonstrate branch coverage reporting."""
    if value is True:
        return 'True'
    elif value is False:
        return 'False'
    else:
        return 'None'


def function_that_does_io():
    """A sample function that might take a long time to test."""
    return True
