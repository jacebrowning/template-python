from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version('{{cookiecutter.project_name}}')
except PackageNotFoundError:
    __version__ = '(local)'

del PackageNotFoundError
del version
