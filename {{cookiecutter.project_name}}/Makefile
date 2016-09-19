# Project settings
PROJECT := {{cookiecutter.project_name}}
PACKAGE := {{cookiecutter.package_name}}
REPOSITORY := {{cookiecutter.github_username}}/{{cookiecutter.github_repo}}
PACKAGES := $(PACKAGE) tests
CONFIG := $(shell ls *.py)
MODULES := $(shell find $(PACKAGES) -name '*.py') $(CONFIG)

# Python settings
ifndef TRAVIS
	PYTHON_MAJOR ?= {{cookiecutter.python_major_version}}
	PYTHON_MINOR ?= {{cookiecutter.python_minor_version}}
endif

# System paths
PLATFORM := $(shell python -c 'import sys; print(sys.platform)')
ifneq ($(findstring win32, $(PLATFORM)), )
	WINDOWS := true
	SYS_PYTHON_DIR := C:\\Python$(PYTHON_MAJOR)$(PYTHON_MINOR)
	SYS_PYTHON := $(SYS_PYTHON_DIR)\\python.exe
{%- if cookiecutter.python_major_version == "3" and cookiecutter.python_minor_version >= "3"  %}{% else %}
	SYS_VIRTUALENV := $(SYS_PYTHON_DIR)\\Scripts\\virtualenv.exe
{%- endif %}
	# https://bugs.launchpad.net/virtualenv/+bug/449537
	export TCL_LIBRARY=$(SYS_PYTHON_DIR)\\tcl\\tcl8.5
else
	ifneq ($(findstring darwin, $(PLATFORM)), )
		MAC := true
	else
		LINUX := true
	endif
	SYS_PYTHON := python$(PYTHON_MAJOR)
	ifdef PYTHON_MINOR
		SYS_PYTHON := $(SYS_PYTHON).$(PYTHON_MINOR)
	endif
{%- if cookiecutter.python_major_version == "3" and cookiecutter.python_minor_version >= "3"  %}{% else %}
	SYS_VIRTUALENV := virtualenv
{%- endif %}
endif

# Virtual environment paths
ENV := env
ifneq ($(findstring win32, $(PLATFORM)), )
	BIN := $(ENV)/Scripts
	ACTIVATE := $(BIN)/activate.bat
	OPEN := cmd /c start
else
	BIN := $(ENV)/bin
	ACTIVATE := . $(BIN)/activate
	ifneq ($(findstring cygwin, $(PLATFORM)), )
		OPEN := cygstart
	else
		OPEN := open
	endif
endif

# Virtual environment executables
ifndef TRAVIS
	BIN_ := $(BIN)/
endif
PYTHON := $(BIN_)python
PIP := $(BIN_)pip
EASY_INSTALL := $(BIN_)easy_install
SNIFFER := $(BIN_)sniffer
HONCHO := $(ACTIVATE) && $(BIN_)honcho

# MAIN TASKS ###################################################################

.PHONY: all
all: doc

.PHONY: ci
ci: check test ## Run all tasks that determine CI status

.PHONY: watch
watch: install .clean-test ## Continuously run all CI tasks when files chanage
	$(SNIFFER)

.PHONY: run ## Start the program
run: install
	$(PYTHON) $(PACKAGE)/__main__.py

# SYSTEM DEPENDENCIES ##########################################################

.PHONY: doctor
doctor:  ## Confirm system dependencies are available
	@ echo "Checking Python version:"
	@ python --version | tee /dev/stderr | grep -q "{{cookiecutter.python_major_version}}.{{cookiecutter.python_minor_version}}."

# PROJECT DEPENDENCIES #########################################################

DEPS_CI := $(ENV)/.install-ci
DEPS_DEV := $(ENV)/.install-dev
DEPS_BASE := $(ENV)/.install-base

.PHONY: install
install: $(DEPS_CI) $(DEPS_DEV) $(DEPS_BASE) ## Install all project dependencies

$(DEPS_CI): requirements/ci.txt $(PIP)
	$(PIP) install --upgrade -r $<
	@ touch $@  # flag to indicate dependencies are installed

$(DEPS_DEV): requirements/dev.txt $(PIP)
	$(PIP) install --upgrade -r $<
ifdef WINDOWS
	@ echo "Manually install pywin32: https://sourceforge.net/projects/pywin32/files/pywin32"
else ifdef MAC
	$(PIP) install --upgrade pync MacFSEvents
else ifdef LINUX
	$(PIP) install --upgrade pyinotify
endif
	@ touch $@  # flag to indicate dependencies are installed

$(DEPS_BASE): setup.py requirements.txt $(PYTHON)
	$(PYTHON) setup.py develop
	@ touch $@  # flag to indicate dependencies are installed

$(PIP): $(PYTHON)
	$(PYTHON) -m pip install --upgrade pip setuptools
	@ touch $@

$(PYTHON):
{%- if cookiecutter.python_major_version == "3" and cookiecutter.python_minor_version >= "3"  %}
	$(SYS_PYTHON) -m venv $(ENV)
{%- else %}
	$(SYS_VIRTUALENV) --python $(SYS_PYTHON) $(ENV)
{%- endif %}

# CHECKS #######################################################################

PEP8 := $(BIN_)pep8
PEP8RADIUS := $(BIN_)pep8radius
PEP257 := $(BIN_)pep257
PYLINT := $(BIN_)pylint

.PHONY: check
check: pep8 pep257 pylint ## Run linters and static analysis

.PHONY: pep8
pep8: install ## Check for convention issues
	$(PEP8) $(PACKAGES) $(CONFIG) --config=.pep8rc

.PHONY: pep257
pep257: install ## Check for docstring issues
	$(PEP257) $(PACKAGES) $(CONFIG)

.PHONY: pylint
pylint: install ## Check for code issues
	$(PYLINT) $(PACKAGES) $(CONFIG) --rcfile=.pylintrc

.PHONY: fix
fix: install
	$(PEP8RADIUS) --docformatter --in-place

# TESTS ########################################################################

{% if cookiecutter.test_runner == "nose" -%}
NOSE := $(BIN_)nosetests
{%- elif cookiecutter.test_runner == "pytest" -%}
PYTEST := $(BIN_)py.test
{%- endif %}
COVERAGE := $(BIN_)coverage
COVERAGE_SPACE := $(BIN_)coverage.space

RANDOM_SEED ?= $(shell date +%s)
{% if cookiecutter.test_runner == "nose" %}
NOSE_OPTS := --with-doctest --with-cov --cov=$(PACKAGE) --cov-report=html  --cov-report=term-missing

.PHONY: test
test: test-all ## Run unit and integration tests

.PHONY: test-unit
test-unit: install .clean-test ## Run the unit tests
	$(NOSE) $(PACKAGE) $(NOSE_OPTS)
	$(COVERAGE_SPACE) $(REPOSITORY) unit

.PHONY: test-int
test-int: install .clean-test ## Run the integration tests
	$(NOSE) tests $(NOSE_OPTS)
	$(COVERAGE_SPACE) $(REPOSITORY) integration

.PHONY: test-all
test-all: install .clean-test ## Run all the tests
	$(NOSE) $(PACKAGES) $(NOSE_OPTS)
	$(COVERAGE_SPACE) $(REPOSITORY) overall
{% elif cookiecutter.test_runner == "pytest" %}
PYTEST_CORE_OPTS := --doctest-modules -r xXw -vv
PYTEST_COV_OPTS := --cov=$(PACKAGE) --no-cov-on-fail --cov-report=term-missing --cov-report=html
PYTEST_RANDOM_OPTS := --random --random-seed=$(RANDOM_SEED)

PYTEST_OPTS := $(PYTEST_CORE_OPTS) $(PYTEST_COV_OPTS) $(PYTEST_RANDOM_OPTS)
PYTEST_OPTS_FAILFAST := $(PYTEST_OPTS) --last-failed --exitfirst

FAILURES := .cache/v/cache/lastfailed
REPORTS ?= xmlreport

.PHONY: test
test: test-all

.PHONY: test-unit
test-unit: install ## Run the unit tests
	@- mv $(FAILURES) $(FAILURES).bak
	$(PYTEST) $(PYTEST_OPTS) $(PACKAGE) --junitxml=$(REPORTS)/unit.xml
	@- mv $(FAILURES).bak $(FAILURES)
	$(COVERAGE_SPACE) $(REPOSITORY) unit

.PHONY: test-int
test-int: install ## Run the integration tests
	@ if test -e $(FAILURES); then $(PYTEST) $(PYTEST_OPTS_FAILFAST) tests; fi
	$(PYTEST) $(PYTEST_OPTS) tests --junitxml=$(REPORTS)/integration.xml
	$(COVERAGE_SPACE) $(REPOSITORY) integration

.PHONY: test-all
test-all: install ## Run all the tests
	@ if test -e $(FAILURES); then $(PYTEST) $(PYTEST_OPTS_FAILFAST) $(PACKAGES); fi
	$(PYTEST) $(PYTEST_OPTS) $(PACKAGES) --junitxml=$(REPORTS)/overall.xml
	$(COVERAGE_SPACE) $(REPOSITORY) overall
{% endif %}
.PHONY: read-coverage
read-coverage:
	$(OPEN) htmlcov/index.html

# DOCUMENTATION ################################################################

PYREVERSE := $(BIN_)pyreverse
PDOC := $(PYTHON) $(BIN_)pdoc
MKDOCS := $(BIN_)mkdocs

PDOC_INDEX := docs/apidocs/$(PACKAGE)/index.html
MKDOCS_INDEX := site/index.html

.PHONY: doc
doc: uml pdoc mkdocs ## Run documentation generators

.PHONY: uml
uml: install docs/*.png ## Generate UML diagrams for classes and packages
docs/*.png: $(MODULES)
	$(PYREVERSE) $(PACKAGE) -p $(PACKAGE) -a 1 -f ALL -o png --ignore tests
	- mv -f classes_$(PACKAGE).png docs/classes.png
	- mv -f packages_$(PACKAGE).png docs/packages.png

.PHONY: pdoc
pdoc: install $(PDOC_INDEX)  ## Generate API documentaiton with pdoc
$(PDOC_INDEX): $(MODULES)
	$(PDOC) --html --overwrite $(PACKAGE) --html-dir docs/apidocs
	@ touch $@

.PHONY: mkdocs
mkdocs: install $(MKDOCS_INDEX) ## Build the documentation site with mkdocs
$(MKDOCS_INDEX): mkdocs.yml docs/*.md
	ln -sf `realpath README.md --relative-to=docs` docs/index.md
	ln -sf `realpath CHANGELOG.md --relative-to=docs/about` docs/about/changelog.md
	ln -sf `realpath CONTRIBUTING.md --relative-to=docs/about` docs/about/contributing.md
	ln -sf `realpath LICENSE.md --relative-to=docs/about` docs/about/license.md
	$(MKDOCS) build --clean --strict

.PHONY: mkdocs-live
mkdocs-live: mkdocs ## Launch and continuously rebuild the mkdocs site
	eval "sleep 3; open http://127.0.0.1:8000" &
	$(MKDOCS) serve

# BUILD ########################################################################

PYINSTALLER := $(BIN_)pyinstaller
PYINSTALLER_MAKESPEC := $(BIN_)pyi-makespec

DIST_FILES := dist/*.tar.gz dist/*.whl
EXE_FILES := dist/$(PROJECT).*

.PHONY: dist
dist: install $(DIST_FILES)
$(DIST_FILES): $(MODULES) README.rst CHANGELOG.rst
	rm -f $(DIST_FILES)
	$(PYTHON) setup.py check --restructuredtext --strict --metadata
	$(PYTHON) setup.py sdist
	$(PYTHON) setup.py bdist_wheel

%.rst: %.md
	pandoc -f markdown_github -t rst -o $@ $<

.PHONY: exe
exe: install $(EXE_FILES)
$(EXE_FILES): $(MODULES) $(PROJECT).spec
	# For framework/shared support: https://github.com/yyuu/pyenv/wiki
	$(PYINSTALLER) $(PROJECT).spec --noconfirm --clean

$(PROJECT).spec:
	$(PYINSTALLER_MAKESPEC) $(PACKAGE)/__main__.py --onefile --windowed --name=$(PROJECT)

# RELEASE ######################################################################

TWINE := $(BIN_)twine

.PHONY: register
register: dist ## Register the project on PyPI
	@ echo NOTE: your project must be registered manually
	@ echo https://github.com/pypa/python-packaging-user-guide/issues/263
	# TODO: switch to twine when the above issue is resolved
	# $(TWINE) register dist/*.whl

.PHONY: upload
upload: .git-no-changes register ## Upload the current version to PyPI
	$(TWINE) upload dist/*
	$(OPEN) https://pypi.python.org/pypi/$(PROJECT)

.PHONY: .git-no-changes
.git-no-changes:
	@ if git diff --name-only --exit-code;        \
	then                                          \
		echo Git working copy is clean...;        \
	else                                          \
		echo ERROR: Git working copy is dirty!;   \
		echo Commit your changes and try again.;  \
		exit -1;                                  \
	fi;

# CLEANUP ######################################################################

.PHONY: clean
clean: .clean-dist .clean-test .clean-doc .clean-build ## Delete all generated and temporary files

.PHONY: clean-all
clean-all: clean .clean-env .clean-workspace

.PHONY: .clean-build
.clean-build:
	find $(PACKAGES) -name '*.pyc' -delete
	find $(PACKAGES) -name '__pycache__' -delete
	rm -rf *.egg-info

.PHONY: .clean-doc
.clean-doc:
	rm -rf README.rst docs/apidocs *.html docs/*.png site

.PHONY: .clean-test
.clean-test:
	rm -rf .cache .pytest .coverage htmlcov xmlreport

.PHONY: .clean-dist
.clean-dist:
	rm -rf *.spec dist build

.PHONY: .clean-env
.clean-env: clean
	rm -rf $(ENV)

.PHONY: .clean-workspace
.clean-workspace:
	rm -rf *.sublime-workspace

# HELP #########################################################################

.PHONY: help
help: all
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
