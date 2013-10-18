#!/usr/bin/env python

"""
Setup script for Comparable.
"""

import setuptools

from foobar import __project__


class TestCommand(setuptools.Command):  # pylint: disable=R0904
    """Runs the unit and integration tests."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys
        import subprocess
        raise SystemExit(subprocess.call([sys.executable, '-m',
                                          'unittest', 'discover']))

setuptools.setup(
    name=__project__,
    version='0.0.0',

    description="Python package template.",
    url='http://pypi.python.org/pypi/Foobar',
    author='Jace Browning',
    author_email='jace.browning@gmail.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': []},

    cmdclass={'test': TestCommand},
    long_description=open('README.rst').read(),
    license='WTFPL',

    install_requires=[],
)
