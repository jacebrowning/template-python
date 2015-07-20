{%- if cookiecutter.python_major_version == "2" -%}# -*- coding: utf-8 -*-
# pylint: disable=W0613,R,C

{% endif -%}
import os
import time
import subprocess

from sniffer.api import select_runnable, file_validator, runnable
try:
    from pync import Notifier
except ImportError:
    notify = None
else:
    notify = Notifier.notify


watch_paths = ['{{cookiecutter.package_name}}/', 'tests/']


@select_runnable('python_tests')
@file_validator
def py_files(filename):
    return all((filename.endswith('.py'),
               not os.path.basename(filename).startswith('.')))


@runnable
def python_tests(*_):

    group = int(time.time())  # unique per run

    for count, (command, title) in enumerate((
        (('make', 'test-unit'), "Unit Tests"),
        (('make', 'test-int'), "Integration Tests"),
        (('make', 'test-all'), "Combined Tests"),
        (('make', 'check'), "Static Analysis"),
        (('make', 'doc'), None),
    ), start=1):

        print("")
        print("$ %s" % ' '.join(command))
        failure = subprocess.call(command)

        show_coverage()

        if failure:
            if notify and title:
                mark = "❌" * count
                notify(mark + " [FAIL] " + mark, title=title, group=group)
            return False
        else:
            if notify and title:
                mark = "✅" * count
                notify(mark + " [PASS] " + mark, title=title, group=group)

    return True


_show_coverage = True


def show_coverage():
    global _show_coverage
    if _show_coverage:
        subprocess.call(['make', 'read-coverage'])
    _show_coverage = False
