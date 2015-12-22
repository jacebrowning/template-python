# Project settings
PROJECT := {{cookiecutter.project_name}}
PACKAGE := {{cookiecutter.package_name}}
SOURCES := Makefile setup.py $(shell find $(PACKAGE) -name '*.py')

# Python settings
PYTHON_MAJOR ?= {{cookiecutter.python_major_version}}
PYTHON_MINOR ?= {{cookiecutter.python_minor_version}}

# Test settings
UNIT_TEST_COVERAGE := 88
INTEGRATION_TEST_COVERAGE := 47
COMBINED_TEST_COVERAGE := 100

# System paths
PLATFORM := $(shell python -c 'import sys; print(sys.platform)')
ifneq ($(findstring win32, $(PLATFORM)), )
	WINDOWS := 1
	SYS_PYTHON_DIR := C:\\Python$(PYTHON_MAJOR)$(PYTHON_MINOR)
	SYS_PYTHON := $(SYS_PYTHON_DIR)\\python.exe
	SYS_VIRTUALENV := $(SYS_PYTHON_DIR)\\Scripts\\virtualenv.exe
	# https://bugs.launchpad.net/virtualenv/+bug/449537
	export TCL_LIBRARY=$(SYS_PYTHON_DIR)\\tcl\\tcl8.5
else
	ifneq ($(findstring darwin, $(PLATFORM)), )
		MAC := 1
	else
		LINUX := 1
	endif
	SYS_PYTHON := python$(PYTHON_MAJOR)
	ifdef PYTHON_MINOR
		SYS_PYTHON := $(SYS_PYTHON).$(PYTHON_MINOR)
	endif
	SYS_VIRTUALENV := virtualenv
endif

# virtualenv paths
ENV := env
ifneq ($(findstring win32, $(PLATFORM)), )
	BIN := $(ENV)/Scripts
	OPEN := cmd /c start
else
	BIN := $(ENV)/bin
	ifneq ($(findstring cygwin, $(PLATFORM)), )
		OPEN := cygstart
	else
		OPEN := open
	endif
endif

# virtualenv executables
PYTHON := $(BIN)/python
PIP := $(BIN)/pip
EASY_INSTALL := $(BIN)/easy_install
RST2HTML := $(PYTHON) $(BIN)/rst2html.py
PDOC := $(PYTHON) $(BIN)/pdoc
PEP8 := $(BIN)/pep8
PEP8RADIUS := $(BIN)/pep8radius
PEP257 := $(BIN)/pep257
PYLINT := $(BIN)/pylint
PYREVERSE := $(BIN)/pyreverse
NOSE := $(BIN)/nosetests
PYTEST := $(BIN)/py.test
COVERAGE := $(BIN)/coverage
SNIFFER := $(BIN)/sniffer

# Flags for PHONY targets
INSTALLED_FLAG := $(ENV)/.installed
DEPENDS_CI_FLAG := $(ENV)/.depends-ci
DEPENDS_DEV_FLAG := $(ENV)/.depends-dev
DOCS_FLAG := $(ENV)/.docs
ALL_FLAG := $(ENV)/.all

# Main Targets #################################################################

.PHONY: all
all: depends doc $(ALL_FLAG)
$(ALL_FLAG): $(SOURCES)
	$(MAKE) check
	touch $(ALL_FLAG)  # flag to indicate all setup steps were successful

.PHONY: ci
ci: check test tests

.PHONY: watch
watch: depends-dev .clean-test
	@ rm -rf $(FAILED_FLAG)
	$(SNIFFER)

# Development Installation #####################################################

.PHONY: env
env: .virtualenv $(INSTALLED_FLAG)
$(INSTALLED_FLAG): Makefile setup.py requirements.txt
	VIRTUAL_ENV=$(ENV) $(PYTHON) setup.py develop
	@ touch $(INSTALLED_FLAG)  # flag to indicate package is installed

.PHONY: .virtualenv
.virtualenv: $(PIP)
$(PIP):
	$(SYS_VIRTUALENV) --python $(SYS_PYTHON) $(ENV)
	$(PIP) install --upgrade pip

.PHONY: depends
depends: depends-ci depends-dev

.PHONY: depends-ci
depends-ci: env Makefile $(DEPENDS_CI_FLAG)
$(DEPENDS_CI_FLAG): Makefile
	$(PIP) install --upgrade pep8 pep257 pylint coverage
		{%- if cookiecutter.test_runner == "nose" %} nose nose-cov
		{%- elif cookiecutter.test_runner == "pytest" %} pytest pytest-cov pytest-random pytest-runfailed
		{%- endif %}
	@ touch $(DEPENDS_CI_FLAG)  # flag to indicate dependencies are installed

.PHONY: depends-dev
depends-dev: env Makefile $(DEPENDS_DEV_FLAG)
$(DEPENDS_DEV_FLAG): Makefile
	$(PIP) install --upgrade pip pep8radius pygments docutils pdoc wheel readme sniffer
ifdef WINDOWS
	$(PIP) install --upgrade pywin32
else ifdef MAC
	$(PIP) install --upgrade pync MacFSEvents==0.4
else ifdef LINUX
	$(PIP) install --upgrade pyinotify
endif
	@ touch $(DEPENDS_DEV_FLAG)  # flag to indicate dependencies are installed

# Documentation ################################################################

.PHONY: doc
doc: readme verify-readme apidocs uml

.PHONY: readme
readme: depends-dev README-github.html README-pypi.html
README-github.html: README.md
	pandoc -f markdown_github -t html -o README-github.html README.md
README-pypi.html: README.rst
	$(RST2HTML) README.rst README-pypi.html
README.rst: README.md
	pandoc -f markdown_github -t rst -o README.rst README.md

.PHONY: verify-readme
verify-readme: $(DOCS_FLAG)
$(DOCS_FLAG): README.rst
	$(PYTHON) setup.py check --restructuredtext --strict --metadata
	@ touch $(DOCS_FLAG)  # flag to indicate README has been checked

.PHONY: apidocs
apidocs: depends-dev apidocs/$(PACKAGE)/index.html
apidocs/$(PACKAGE)/index.html: $(SOURCES)
	$(PDOC) --html --overwrite $(PACKAGE) --html-dir apidocs

.PHONY: uml
uml: depends-dev docs/*.png
docs/*.png: $(SOURCES)
	$(PYREVERSE) $(PACKAGE) -p $(PACKAGE) -a 1 -f ALL -o png --ignore test
	- mv -f classes_$(PACKAGE).png docs/classes.png
	- mv -f packages_$(PACKAGE).png docs/packages.png

.PHONY: read
read: doc
	$(OPEN) apidocs/$(PACKAGE)/index.html
	$(OPEN) README-pypi.html
	$(OPEN) README-github.html

# Static Analysis ##############################################################

.PHONY: check
check: pep8 pep257 pylint

.PHONY: pep8
pep8: depends-ci
	$(PEP8) $(PACKAGE) tests --config=.pep8rc

.PHONY: pep257
pep257: depends-ci
	$(PEP257) $(PACKAGE) tests

.PHONY: pylint
pylint: depends-ci
# These warnings shouldn't fail builds, but warn in editors:
# C0111: Line too long
# R0913: Too many arguments
# R0914: Too many local variables
	$(PYLINT) $(PACKAGE) tests --rcfile=.pylintrc --disable=C0111,R0913,R0914

.PHONY: fix
fix: depends-dev
	$(PEP8RADIUS) --docformatter --in-place

# Testing ######################################################################

RANDOM_SEED ?= $(shell date +%s)
{% if cookiecutter.test_runner == "nose" %}
NOSE_OPTS := --with-doctest --with-cov --cov=$(PACKAGE) --cov-report=html

.PHONY: test-unit
test-unit: test
.PHONY: test
test: depends-ci .clean-test
	$(NOSE) $(PACKAGE) $(NOSE_OPTS)
ifndef TRAVIS
	$(COVERAGE) report --show-missing --fail-under=$(UNIT_TEST_COVERAGE)
endif

.PHONY: test-int
test-int: depends-ci .clean-test
	$(NOSE) tests $(NOSE_OPTS)
ifndef TRAVIS
	$(COVERAGE) report --show-missing --fail-under=$(INTEGRATION_TEST_COVERAGE)
endif

.PHONY: test-all
test-all: tests
.PHONY: test-all
tests: depends-ci .clean-test
	$(NOSE) $(PACKAGE) tests $(NOSE_OPTS) -xv
ifndef TRAVIS
	$(COVERAGE) report --show-missing --fail-under=$(COMBINED_TEST_COVERAGE)
endif
{% elif cookiecutter.test_runner == "pytest" %}
PYTEST_CORE_OPTS := --doctest-modules --verbose -r xXw -vv
PYTEST_COV_OPTS := --cov=$(PACKAGE) --cov-report=term-missing --no-cov-on-fail
PYTEST_RANDOM_OPTS := --random --random-seed=$(RANDOM_SEED)

PYTEST_OPTS := $(PYTEST_CORE_OPTS) $(PYTEST_COV_OPTS) $(PYTEST_RANDOM_OPTS)
PYTEST_OPTS_FAILFAST := $(PYTEST_OPTS) --failed --exitfirst

FAILED_FLAG := .pytest/failed

.PHONY: test test-unit
test: test-unit
test-unit: depends-ci
	@ if test -e $(FAILED_FLAG); then $(MAKE) test-all; fi
	@ $(COVERAGE) erase
	$(PYTEST) $(PYTEST_OPTS) $(PACKAGE)
ifndef TRAVIS
	$(COVERAGE) html --directory htmlcov --fail-under=$(UNIT_TEST_COVERAGE)
endif

.PHONY: test-int
test-int: depends-ci
	@ if test -e $(FAILED_FLAG); then $(MAKE) test-all; fi
	@ $(COVERAGE) erase
	$(PYTEST) $(PYTEST_OPTS_FAILFAST) tests
ifndef TRAVIS
	@ rm -rf $(FAILED_FLAG)  # next time, don't run the previously failing test
	$(COVERAGE) html --directory htmlcov --fail-under=$(INTEGRATION_TEST_COVERAGE)
endif

.PHONY: tests test-all
tests: test-all
test-all: depends-ci
	@ if test -e $(FAILED_FLAG); then $(PYTEST) --failed $(PACKAGE) tests; fi
	@ $(COVERAGE) erase
	$(PYTEST) $(PYTEST_OPTS_FAILFAST) $(PACKAGE) tests
ifndef TRAVIS
	@ rm -rf $(FAILED_FLAG)  # next time, don't run the previously failing test
	$(COVERAGE) html --directory htmlcov --fail-under=$(COMBINED_TEST_COVERAGE)
endif
{% endif %}
.PHONY: read-coverage
read-coverage:
	$(OPEN) htmlcov/index.html

# Cleanup ######################################################################

.PHONY: clean
clean: .clean-dist .clean-test .clean-doc .clean-build
	rm -rf $(ALL_FLAG)

.PHONY: clean-all
clean-all: clean .clean-env .clean-workspace

.PHONY: .clean-build
.clean-build:
	find $(PACKAGE) -name '*.pyc' -delete
	find $(PACKAGE) -name '__pycache__' -delete
	rm -rf $(INSTALLED_FLAG)

.PHONY: .clean-doc
.clean-doc:
	rm -rf README.rst apidocs *.html docs/*.png

.PHONY: .clean-test
.clean-test:
	rm -rf .pytest .coverage htmlcov

.PHONY: .clean-dist
.clean-dist:
	rm -rf dist build

.PHONY: .clean-env
.clean-env: clean
	rm -rf $(ENV)

.PHONY: .clean-workspace
.clean-workspace:
	rm -rf *.sublime-workspace

# Release ######################################################################

.PHONY: register-test
register-test: doc
	$(PYTHON) setup.py register --strict --repository https://testpypi.python.org/pypi

.PHONY: upload-test
upload-test: register-test
	$(PYTHON) setup.py sdist upload --repository https://testpypi.python.org/pypi
	$(PYTHON) setup.py bdist_wheel upload --repository https://testpypi.python.org/pypi
	$(OPEN) https://testpypi.python.org/pypi/$(PROJECT)

.PHONY: register
register: doc
	$(PYTHON) setup.py register --strict

.PHONY: upload
upload: .git-no-changes register
	$(PYTHON) setup.py sdist upload
	$(PYTHON) setup.py bdist_wheel upload
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

# System Installation ##########################################################

.PHONY: develop
develop:
	$(SYS_PYTHON) setup.py develop

.PHONY: install
install:
	$(SYS_PYTHON) setup.py install

.PHONY: download
download:
	pip install $(PROJECT)
