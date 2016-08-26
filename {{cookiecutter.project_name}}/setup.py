#!/usr/bin/env python

"""Setup script for {{cookiecutter.project_name}}."""

import sys

import setuptools

MINIMUM_PYTHON_VERSION = {{cookiecutter.python_major_version}}, {{cookiecutter.python_minor_version}}
if sys.version_info < MINIMUM_PYTHON_VERSION:
    sys.exit("Python {}.{}+ is required.".format(*MINIMUM_PYTHON_VERSION))

try:
    README = open("README.rst").read()
    CHANGELOG = open("CHANGELOG.rst").read()
except IOError:
    LONG_DESCRIPTION = "<placeholder>"
else:
    LONG_DESCRIPTION = README + '\n' + CHANGELOG

setuptools.setup(
    name='{{cookiecutter.project_name}}',
    version='0.0.0',

    description="{{cookiecutter.project_short_description}}",
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': []},

    long_description=LONG_DESCRIPTION,
    license='MIT',
    classifiers=[
        # TODO: update this list to match your application: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    install_requires=open("requirements.txt").readlines(),
)
