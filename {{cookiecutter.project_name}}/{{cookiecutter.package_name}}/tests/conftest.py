"""Unit tests configuration file."""

import log


def pytest_configure(config):
    """Disable verbose output when running tests."""
    log.init(debug=True)

    terminal = config.pluginmanager.getplugin('terminal')
    base = terminal.TerminalReporter

    class QuietReporter(base):
        """Reporter that only shows dots when running tests."""

        def __init__(self, *args, **kwargs):
            {%- if cookiecutter.python_major_version == "3" %}
            super().__init__(*args, **kwargs)
            {%- else %}
            base.__init__(self, *args, **kwargs)
            {%- endif %}
            self.verbosity = 0
            self.showlongtestinfo = False
            self.showfspath = False

    terminal.TerminalReporter = QuietReporter
