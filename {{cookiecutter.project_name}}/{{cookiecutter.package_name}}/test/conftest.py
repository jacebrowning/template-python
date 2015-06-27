"""Unit test configuration file."""


def pytest_configure(config):
    """Disable verbose output when running tests."""
    terminal = config.pluginmanager.getplugin('terminal')
    base = terminal.TerminalReporter

    class QuietReporter(base):
        """A py.test reporting that only shows dots when running tests."""

        def __init__(self, *args, **kwargs):
            # Python 2/3 compatible super class __init__, pylint: disable=E1002
            if issubclass(base, object):
                super(base, self).__init__(*args, **kwargs)
            else:
                base.__init__(self, *args, **kwargs)
            self.verbosity = 0
            self.showlongtestinfo = False
            self.showfspath = False

    terminal.TerminalReporter = QuietReporter
