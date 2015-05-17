{%- if cookiecutter.python_major_version == "2" -%}# -*- coding: utf-8 -*-

{% endif -%}
import os
import subprocess

from sniffer.api import select_runnable, file_validator, runnable
from pync import Notifier


watch_paths = ['{{cookiecutter.package_name}}/', 'tests/']


@select_runnable('python_tests')
@file_validator
def py_files(filename):
    return all((filename.endswith('.py'),
               not os.path.basename(filename).startswith('.')))


@runnable
def python_tests(*args):

    for count, (command, title) in enumerate((
        (('make', 'test-unit'), "Unit Tests"),
        (('make', 'test-int'), "Integration Tests"),
        (('make', 'test-all'), "Combined Tests"),
    ), start=1):

        failure = subprocess.call(command)

        if failure:
            mark = "❌" * count
            Notifier.notify(mark + " [FAIL] " + mark, title=title)
            return False
        else:
            mark = "✅" * count
            Notifier.notify(mark + " [PASS] " + mark, title=title)

    return True
