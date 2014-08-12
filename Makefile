# Python settings
PYTHON_MAJOR := 3
PYTHON_MINOR := 4

# Project settings (automatically detected from files/directories)
PROJECT := $(patsubst ./%.sublime-project,%, $(shell find . -type f -name '*.sublime-p*'))
PACKAGE := $(patsubst ./%/__init__.py,%, $(shell find . -maxdepth 2 -name '__init__.py'))
SOURCES := Makefile setup.py $(shell find $(PACKAGE) -name '*.py')
EGG_INFO := $(subst -,_,$(PROJECT)).egg-info

# System paths (automatically detected from the system Python)
PLATFORM := $(shell python -c 'import sys; print(sys.platform)')
ifneq ($(findstring win32, $(PLATFORM)), )
	SYS_PYTHON_DIR := C:\\Python$(PYTHON_MAJOR)$(PYTHON_MINOR)
	SYS_PYTHON := $(SYS_PYTHON_DIR)\\python.exe
	SYS_VIRTUALENV := $(SYS_PYTHON_DIR)\\Scripts\\virtualenv.exe
	# https://bugs.launchpad.net/virtualenv/+bug/449537
	export TCL_LIBRARY=$(SYS_PYTHON_DIR)\\tcl\\tcl8.5
else
	SYS_PYTHON := python$(PYTHON_MAJOR)
	SYS_VIRTUALENV := virtualenv
endif

# virtualenv paths (automatically detected from the system Python)
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
PEP257 := $(BIN)/pep257
PYLINT := $(BIN)/pylint
PYREVERSE := $(BIN)/pyreverse
NOSE := $(BIN)/nosetests

# Flags for PHONY targets
DEPENDS_CI := $(ENV)/.depends-ci
DEPENDS_DEV := $(ENV)/.depends-dev
ALL := $(ENV)/.all

# Main Targets ###############################################################

.PHONY: all
all: depends doc $(ALL)
$(ALL): $(SOURCES)
	$(MAKE) check
	touch $(ALL)  # flag to indicate all setup steps were successful

.PHONY: ci
ci: pep8 pep257 test tests

# Development Installation ###################################################

.PHONY: env
env: .virtualenv $(EGG_INFO)
$(EGG_INFO): Makefile setup.py
	$(PYTHON) setup.py develop
	touch $(EGG_INFO)  # flag to indicate package is installed

.PHONY: .virtualenv
.virtualenv: $(PIP)
$(PIP):
	$(SYS_VIRTUALENV) --python $(SYS_PYTHON) $(ENV)

.PHONY: depends
depends: .depends-ci .depends-dev

.PHONY: .depends-ci
.depends-ci: env Makefile $(DEPENDS_CI)
$(DEPENDS_CI): Makefile
	$(PIP) install --upgrade pep8 pep257 nose coverage
	touch $(DEPENDS_CI)  # flag to indicate dependencies are installed

.PHONY: .depends-dev
.depends-dev: env Makefile $(DEPENDS_DEV)
$(DEPENDS_DEV): Makefile
	$(PIP) install --upgrade docutils pdoc pylint wheel
	touch $(DEPENDS_DEV)  # flag to indicate dependencies are installed

# Documentation ##############################################################

.PHONY: doc
doc: readme apidocs uml

.PHONY: readme
readme: .depends-dev docs/README-github.html docs/README-pypi.html
docs/README-github.html: README.md
	pandoc -f markdown_github -t html -o docs/README-github.html README.md
	cp -f docs/README-github.html docs/README.html  # default format is GitHub
docs/README-pypi.html: README.rst
	$(RST2HTML) README.rst docs/README-pypi.html
README.rst: README.md
	pandoc -f markdown_github -t rst -o README.rst README.md

.PHONY: apidocs
apidocs: .depends-dev apidocs/$(PACKAGE)/index.html
apidocs/$(PACKAGE)/index.html: $(SOURCES)
	$(PDOC) --html --overwrite $(PACKAGE) --html-dir apidocs

.PHONY: uml
uml: .depends-dev docs/*.png
docs/*.png: $(SOURCES)
	$(PYREVERSE) $(PACKAGE) -p $(PACKAGE) -f ALL -o png --ignore test
	- mv -f classes_$(PACKAGE).png docs/classes.png
	- mv -f packages_$(PACKAGE).png docs/packages.png

.PHONY: read
read: doc
	$(OPEN) apidocs/$(PACKAGE)/index.html
	$(OPEN) docs/README-pypi.html
	$(OPEN) docs/README-github.html

# Static Analysis ############################################################

.PHONY: check
check: pep8 pep257 pylint

.PHONY: pep8
pep8: .depends-ci
	$(PEP8) $(PACKAGE) --ignore=E501

.PHONY: pep257
pep257: .depends-ci
	$(PEP257) $(PACKAGE) --ignore=E501

.PHONY: pylint
pylint: .depends-dev
	$(PYLINT) $(PACKAGE) --rcfile=.pylintrc

# Testing ####################################################################

.PHONY: test
test: .depends-ci
	$(NOSE) --config=.noserc

.PHONY: tests
tests: .depends-ci
	TEST_INTEGRATION=1 $(NOSE) --config=.noserc --cover-package=$(PACKAGE) -xv

# Cleanup ####################################################################

.PHONY: clean
clean: .clean-dist .clean-test .clean-doc .clean-build
	rm -rf $(ALL)

.PHONY: clean-all
clean-all: clean .clean-env

.PHONY: .clean-env
.clean-env:
	rm -rf $(ENV)

.PHONY: .clean-build
.clean-build:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	rm -rf *.egg-info

.PHONY: .clean-doc
.clean-doc:
	rm -rf README.rst apidocs docs/*.html docs/*.png

.PHONY: .clean-test
.clean-test:
	rm -rf .coverage

.PHONY: .clean-dist
.clean-dist:
	rm -rf dist build

# Release ####################################################################

.PHONY: .git-no-changes
.git-no-changes:
	@if git diff --name-only --exit-code;         \
	then                                          \
		echo Git working copy is clean...;        \
	else                                          \
		echo ERROR: Git working copy is dirty!;   \
		echo Commit your changes and try again.;  \
		exit -1;                                  \
	fi;

.PHONY: dist
dist: check doc test tests
	$(PYTHON) setup.py sdist
	$(PYTHON) setup.py bdist_wheel
	$(MAKE) read

.PHONY: upload
upload: .git-no-changes doc
	$(PYTHON) setup.py register sdist upload
	$(PYTHON) setup.py bdist_wheel upload

# System Installation ########################################################

.PHONY: develop
develop:
	$(SYS_PYTHON) setup.py develop

.PHONY: install
install:
	$(SYS_PYTHON) setup.py install

.PHONY: download
download:
	pip install $(PROJECT)
