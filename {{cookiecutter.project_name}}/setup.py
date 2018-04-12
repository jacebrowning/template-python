#!/usr/bin/env python

import os
import sys

import setuptools


PACKAGE_NAME = '{{cookiecutter.package_name}}'
MINIMUM_PYTHON_VERSION = '{{cookiecutter.python_major_version}}.{{cookiecutter.python_minor_version}}'


def check_python_version():
    """Exit when the Python version is too low."""
    if sys.version < MINIMUM_PYTHON_VERSION:
        sys.exit("Python {0}+ is required.".format(MINIMUM_PYTHON_VERSION))


def read_package_variable(key, filename='__init__.py'):
    """Read the value of a variable from the package without importing."""
    module_path = os.path.join(PACKAGE_NAME, filename)
    with open(module_path) as module:
        for line in module:
            parts = line.strip().split(' ', 2)
            if parts[:-1] == [key, '=']:
                return parts[-1].strip("'")
    sys.exit("'%s' not found in '%s'", key, module_path)


def build_description():
    """Build a description for the project from documentation files."""
    try:
        readme = open("README.rst").read()
        changelog = open("CHANGELOG.rst").read()
    except IOError:
        return "<placeholder>"
    else:
        return readme + '\n' + changelog


check_python_version()

setuptools.setup(
    name=read_package_variable('__project__'),
    version=read_package_variable('__version__'),

    description="{{cookiecutter.project_short_description}}",
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': [
        '{{cookiecutter.package_name}}-cli = {{cookiecutter.package_name}}.cli:main',
        '{{cookiecutter.package_name}}-gui = {{cookiecutter.package_name}}.gui:main',
    ]},

    long_description=build_description(),
    license='MIT',
    classifiers=[
        # TODO: update this list to match your application: https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: {{cookiecutter.python_major_version}}',
        'Programming Language :: Python :: {{cookiecutter.python_major_version}}.{{cookiecutter.python_minor_version}}',
    ],

    install_requires=[
        # TODO: Add your library's requirements here
        "click ~= 6.0",
        "minilog ~=0.2.1",
    ]
)
