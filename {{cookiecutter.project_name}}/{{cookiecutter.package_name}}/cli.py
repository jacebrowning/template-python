"""A sample CLI."""

import click
import log

from . import utils


@click.command()
@click.argument('feet')
def main(feet: str):
    log.init()

    meters = utils.feet_to_meters(feet)

    if meters is not None:
        click.echo(meters)


if __name__ == '__main__':  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
