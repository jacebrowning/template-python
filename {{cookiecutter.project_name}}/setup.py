#!/usr/bin/env python

"""Setup script for {{cookiecutter.project_name}}."""

import setuptools

from {{cookiecutter.package_name}} import __project__, __version__

import os
if os.path.exists('README.rst'):
    README = open('README.rst').read()
else:
    README = ""  # a placeholder, readme is generated on release
CHANGES = open('CHANGES.md').read()


setuptools.setup(
    name=__project__,
    version=__version__,

    description="{{cookiecutter.project_name}} is a Python 3 package template.",
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': []},

    long_description=(README + '\n' + CHANGES),
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
    ],

    install_requires=open('requirements.txt').readlines(),
)
