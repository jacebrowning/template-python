"""Package for {{cookiecutter.project_name}}."""

import sys
import pkg_resources

__project__ = '{{cookiecutter.project_name}}'
try:
    __version__ = pkg_resources.get_distribution(__name__).version
except pkg_resources.RequirementParseError:
    __version__ = '<local>'

VERSION = "{0} v{1}".format(__project__, __version__)
