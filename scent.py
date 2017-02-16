# -*- coding: utf-8 -*-
"""Configuration file for sniffer."""

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


watch_paths = ['.']


@select_runnable('python')
@file_validator
def py_files(filename):
    return "TemplateDemo" not in filename


@runnable
def python(*_):

    group = int(time.time())  # unique per run

    for count, (command, title) in enumerate((
        (('make', 'build'), "Generate Sample"),
        (('make', 'ci'), "Test Sample"),
    ), start=1):

        print("")
        print("$ %s" % ' '.join(command))
        failure = subprocess.call(command)

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
