# Project settings
PROJECT := {{cookiecutter.project_name}}
PACKAGE := {{cookiecutter.package_name}}
REPOSITORY := {{cookiecutter.github_username}}/{{cookiecutter.github_repo}}
DIRECTORIES := $(PACKAGE) tests
FILES := Makefile setup.py $(shell find $(DIRECTORIES) -name '*.py')

# Python settings
ifndef TRAVIS
ifndef APPVEYOR
	PYTHON_MAJOR ?= {{cookiecutter.python_major_version}}
	PYTHON_MINOR ?= {{cookiecutter.python_minor_version}}
endif
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
RST2HTML := $(PYTHON) $(BIN_)rst2html.py
PDOC := $(PYTHON) $(BIN_)pdoc
MKDOCS := $(BIN_)mkdocs
PEP8 := $(BIN_)pep8
PEP8RADIUS := $(BIN_)pep8radius
PEP257 := $(BIN_)pep257
PYLINT := $(BIN_)pylint
PYREVERSE := $(BIN_)pyreverse
NOSE := $(BIN_)nosetests
PYTEST := $(BIN_)py.test
COVERAGE := $(BIN_)coverage
COVERAGE_SPACE := $(BIN_)coverage.space
SNIFFER := $(BIN_)sniffer
HONCHO := PYTHONPATH=$(PWD) $(ACTIVATE) && $(BIN_)honcho

# Flags for PHONY targets
INSTALLED_FLAG := $(ENV)/.installed
DEPENDS_CI_FLAG := $(ENV)/.depends-ci
DEPENDS_DOC_FLAG := $(ENV)/.depends-doc
DEPENDS_DEV_FLAG := $(ENV)/.depends-dev
ALL_FLAG := $(ENV)/.all

# Main Targets #################################################################

.PHONY: all
all: depends doc $(ALL_FLAG)
$(ALL_FLAG): $(FILES)
	make check
	@ touch $@  # flag to indicate all setup steps were successful

.PHONY: ci
ci: check test ## Run all targets that determine CI status

.PHONY: watch
watch: depends .clean-test ## Continuously run all CI targets when files chanage
	@ rm -rf $(FAILED_FLAG)
	$(SNIFFER)

# Development Installation #####################################################

.PHONY: env
env: $(PIP) $(INSTALLED_FLAG)
$(INSTALLED_FLAG): Makefile setup.py requirements.txt
	VIRTUAL_ENV=$(ENV) $(PYTHON) setup.py develop
	@ touch $@  # flag to indicate package is installed

$(PIP):
{%- if cookiecutter.python_major_version == "3" and cookiecutter.python_minor_version >= "3"  %}
	$(SYS_PYTHON) -m venv --clear $(ENV)
{%- else %}
	$(SYS_VIRTUALENV) --python $(SYS_PYTHON) $(ENV)
{%- endif %}
	$(PYTHON) -m pip install --upgrade pip setuptools


# Tools Installation ###########################################################

.PHONY: depends
depends: depends-ci depends-doc depends-dev ## Install all project dependnecies

.PHONY: depends-ci
depends-ci: env Makefile $(DEPENDS_CI_FLAG)
$(DEPENDS_CI_FLAG): Makefile
	$(PIP) install --upgrade pep8 pep257 pylint coverage coverage.space
		{%- if cookiecutter.test_runner == "nose" %} nose nose-cov expecter
		{%- elif cookiecutter.test_runner == "pytest" %} pytest pytest-describe pytest-expecter pytest-cov pytest-random
		{%- endif %}
	@ touch $@  # flag to indicate dependencies are installed

.PHONY: depends-doc
depends-doc: env Makefile $(DEPENDS_DOC_FLAG)
$(DEPENDS_DOC_FLAG): Makefile
	$(PIP) install --upgrade pylint docutils readme pdoc mkdocs pygments
	@ touch $@  # flag to indicate dependencies are installed

.PHONY: depends-dev
depends-dev: env Makefile $(DEPENDS_DEV_FLAG)
$(DEPENDS_DEV_FLAG): Makefile
	$(PIP) install --upgrade pip pep8radius wheel sniffer honcho
ifdef WINDOWS
	$(PIP) install --upgrade pywin32
else ifdef MAC
	$(PIP) install --upgrade pync MacFSEvents==0.4
else ifdef LINUX
	$(PIP) install --upgrade pyinotify
endif
	@ touch $@  # flag to indicate dependencies are installed

# Documentation ################################################################

.PHONY: doc
doc: uml pdoc mkdocs ## Run all documentation targets

.PHONY: uml
uml: depends-doc docs/*.png ## Generate UML diagrams for classes and packages
docs/*.png: $(FILES)
	$(PYREVERSE) $(PACKAGE) -p $(PACKAGE) -a 1 -f ALL -o png --ignore tests
	- mv -f classes_$(PACKAGE).png docs/classes.png
	- mv -f packages_$(PACKAGE).png docs/packages.png

.PHONY: pdoc
pdoc: depends-doc pdoc/$(PACKAGE)/index.html  ## Generate API documentaiton from the code
pdoc/$(PACKAGE)/index.html: $(FILES)
	$(PDOC) --html --overwrite $(PACKAGE) --html-dir docs/apidocs

.PHONY: mkdocs
mkdocs: depends-doc site/index.html ## Build the documentation with mkdocs
site/index.html: mkdocs.yml docs/*.md
	$(MKDOCS) build --clean --strict

.PHONY: mkdocs-live
mkdocs-live: depends-doc ## Launch and continuously rebuild the mkdocs site
	eval "sleep 3; open http://127.0.0.1:8000" &
	$(MKDOCS) serve

# Static Analysis ##############################################################

.PHONY: check
check: pep8 pep257 pylint ## Run all static analysis targets

.PHONY: pep8
pep8: depends-ci ## Check for convention issues
	$(PEP8) $(DIRECTORIES) --config=.pep8rc

.PHONY: pep257
pep257: depends-ci ## Check for docstring issues
	$(PEP257) $(DIRECTORIES)

.PHONY: pylint
pylint: depends-ci ## Check for code issues
	$(PYLINT) $(DIRECTORIES) --rcfile=.pylintrc

.PHONY: fix
fix: depends-dev
	$(PEP8RADIUS) --docformatter --in-place

# Testing ######################################################################

RANDOM_SEED ?= $(shell date +%s)
{% if cookiecutter.test_runner == "nose" %}
NOSE_OPTS := --with-doctest --with-cov --cov=$(PACKAGE) --cov-report=html

.PHONY: test
test: test-all

.PHONY: test-unit
test-unit: depends-ci .clean-test ## Run the unit tests
	$(NOSE) $(PACKAGE) $(NOSE_OPTS)
ifndef TRAVIS
ifndef APPVEYOR
	$(COVERAGE) report --show-missing --fail-under=$(UNIT_TEST_COVERAGE)
endif
endif

.PHONY: test-int
test-int: depends-ci .clean-test ## Run the integration tests
	$(NOSE) tests $(NOSE_OPTS)
ifndef TRAVIS
ifndef APPVEYOR
	$(COVERAGE) report --show-missing --fail-under=$(INTEGRATION_TEST_COVERAGE)
endif
endif

.PHONY: test-all
test-all: depends-ci .clean-test ## Run all the tests
	$(NOSE) $(DIRECTORIES) $(NOSE_OPTS) -xv
ifndef TRAVIS
ifndef APPVEYOR
	$(COVERAGE) report --show-missing --fail-under=$(COMBINED_TEST_COVERAGE)
endif
endif
{% elif cookiecutter.test_runner == "pytest" %}
PYTEST_CORE_OPTS := --doctest-modules -r xXw -vv
PYTEST_COV_OPTS := --cov=$(PACKAGE) --no-cov-on-fail --cov-report=term-missing --cov-report=html
PYTEST_RANDOM_OPTS := --random --random-seed=$(RANDOM_SEED)

PYTEST_OPTS := $(PYTEST_CORE_OPTS) $(PYTEST_COV_OPTS) $(PYTEST_RANDOM_OPTS)
PYTEST_OPTS_FAILFAST := $(PYTEST_OPTS) --last-failed --exitfirst

FAILURES := .cache/v/cache/lastfailed

.PHONY: test
test: test-all

.PHONY: test-unit
test-unit: depends-ci ## Run the unit tests
	@- mv $(FAILURES) $(FAILURES).bak
	$(PYTEST) $(PYTEST_OPTS) $(PACKAGE)
	@- mv $(FAILURES).bak $(FAILURES)
ifndef TRAVIS
ifndef APPVEYOR
	$(COVERAGE_SPACE) $(REPOSITORY) unit
endif
endif

.PHONY: test-int
test-int: depends-ci ## Run the integration tests
	@ if test -e $(FAILURES); then $(PYTEST) $(PYTEST_OPTS_FAILFAST) tests; fi
	$(PYTEST) $(PYTEST_OPTS) tests
ifndef TRAVIS
ifndef APPVEYOR
	$(COVERAGE_SPACE) $(REPOSITORY) integration
endif
endif

.PHONY: test-all
test-all: depends-ci ## Run all the tests
	@ if test -e $(FAILURES); then $(PYTEST) $(PYTEST_OPTS_FAILFAST) $(DIRECTORIES); fi
	$(PYTEST) $(PYTEST_OPTS) $(DIRECTORIES)
ifndef TRAVIS
ifndef APPVEYOR
	$(COVERAGE_SPACE) $(REPOSITORY) overall
endif
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
	find $(DIRECTORIES) -name '*.pyc' -delete
	find $(DIRECTORIES) -name '__pycache__' -delete
	rm -rf $(INSTALLED_FLAG) *.egg-info

.PHONY: .clean-doc
.clean-doc:
	rm -rf README.rst docs/apidocs *.html docs/*.png site

.PHONY: .clean-test
.clean-test:
	rm -rf .cache .pytest .coverage htmlcov

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
register-test: README.rst CHANGELOG.rst ## Register the project on the test PyPI
	$(PYTHON) setup.py register --strict --repository https://testpypi.python.org/pypi

.PHONY: register
register: README.rst CHANGELOG.rst ## Register the project on PyPI
	$(PYTHON) setup.py register --strict

.PHONY: upload-test
upload-test: register-test ## Upload the current version to the test PyPI
	$(PYTHON) setup.py sdist upload --repository https://testpypi.python.org/pypi
	$(PYTHON) setup.py bdist_wheel upload --repository https://testpypi.python.org/pypi
	$(OPEN) https://testpypi.python.org/pypi/$(PROJECT)

.PHONY: upload
upload: .git-no-changes register ## Upload the current version to PyPI
	$(PYTHON) setup.py check --restructuredtext --strict --metadata
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

%.rst: %.md
	pandoc -f markdown_github -t rst -o $@ $<

# System Installation ##########################################################

.PHONY: develop
develop:
	$(SYS_PYTHON) setup.py develop

.PHONY: install
install:
	$(SYS_PYTHON) setup.py install

.PHONY: download
download:
	$(SYS_PYTHON) -m pip install $(PROJECT)

# Help #########################################################################

.PHONY: help
help: all
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
