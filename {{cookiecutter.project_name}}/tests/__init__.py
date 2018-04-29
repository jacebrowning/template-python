"""Integration tests for the package."""

try:
    from IPython.terminal.debugger import TerminalPdb as Debugger
except ImportError:
    from pdb import Pdb as Debugger
