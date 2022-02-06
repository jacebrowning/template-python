"""A sample module."""

import log


def feet_to_meters(feet):
    """Convert feet to meters."""
    try:
        value = float(feet)
    except ValueError:
        log.error("Unable to convert to float: %s", feet)
        return None
    else:
        return (0.3048 * value * 10000.0 + 0.5) / 10000.0
