"""A sample module."""


class Class(object):
    """A sample class."""


def function(value):
    """A function with branches to demonstrate branch coverage reporting."""
    if value is True:
        return 'True'
    elif value is False:
        return 'False'
    else:
        return 'None'


def function_with_network_stuff():
    """A sample function that might take a long time to test."""
    return True


def function_with_disk_stuff():
    """A sample function that might take a long time to test."""
    return False
