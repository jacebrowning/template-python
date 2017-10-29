# Project settings
PROJECT := {{cookiecutter.project_name}}
PACKAGE := {{cookiecutter.package_name}}
REPOSITORY := {{cookiecutter.github_username}}/{{cookiecutter.github_repo}}

# Project paths
PACKAGES := $(PACKAGE) tests
CONFIG := $(wildcard *.py)
MODULES := $(wildcard $(PACKAGE)/*.py)

# Virtual environment paths
export PIPENV_SHELL_COMPAT=true
export PIPENV_VENV_IN_PROJECT=true
export PIPENV_IGNORE_VIRTUALENVS=true
ENV := .venv

# MAIN TASKS ###################################################################

SNIFFER := pipenv run sniffer

.PHONY: all
all: install

.PHONY: ci
ci: check test ## Run all tasks that determine CI status

.PHONY: watch
watch: install .clean-test ## Continuously run all CI tasks when files chanage
	$(SNIFFER)

.PHONY: run ## Start the program
run: install
	pipenv run python $(PACKAGE)/__main__.py

# SYSTEM DEPENDENCIES ##########################################################

.PHONY: doctor
doctor:  ## Confirm system dependencies are available
	bin/verchew

# PROJECT DEPENDENCIES #########################################################

DEPENDENCIES := $(ENV)/.pipenv.($ shell bin/checksum Pipfile.lock)
METADATA := *.egg-info

.PHONY: install
install: $(DEPENDENCIES) $(METADATA)

$(DEPENDENCIES):
	pipenv install --dev
	@ touch $@

$(METADATA): setup.py
	pipenv run python setup.py develop
	@ touch $@

# CHECKS #######################################################################

PYLINT := pipenv run pylint
PYCODESTYLE := pipenv run pycodestyle
PYDOCSTYLE := pipenv run pydocstyle

.PHONY: check
check: pylint pycodestyle pydocstyle ## Run linters and static analysis

.PHONY: pylint
pylint: install
	$(PYLINT) $(PACKAGES) $(CONFIG) --rcfile=.pylint.ini

.PHONY: pycodestyle
pycodestyle: install
	$(PYCODESTYLE) $(PACKAGES) $(CONFIG) --config=.pycodestyle.ini

.PHONY: pydocstyle
pydocstyle: install
	$(PYDOCSTYLE) $(PACKAGES) $(CONFIG)

# TESTS ########################################################################

{% if cookiecutter.test_runner == "nose" -%}
NOSE := pipenv run nosetests
{%- elif cookiecutter.test_runner == "pytest" -%}
PYTEST := pipenv run py.test
{%- endif %}
COVERAGE := pipenv run coverage
COVERAGE_SPACE := pipenv run coverage.space

RANDOM_SEED ?= $(shell date +%s)
{% if cookiecutter.test_runner == "nose" %}
NOSE_OPTIONS := --with-doctest
ifndef DISABLE_COVERAGE
NOSE_OPTIONS += --with-coverage --cover-package=$(PACKAGE) --cover-html --cover-html-dir=htmlcov --cover-branches
endif

.PHONY: test
test: test-all ## Run unit and integration tests

.PHONY: test-unit
test-unit: install .clean-test
	$(NOSE) $(PACKAGE) $(NOSE_OPTIONS)
	$(COVERAGE_SPACE) $(REPOSITORY) unit

.PHONY: test-int
test-int: install .clean-test
	$(NOSE) tests $(NOSE_OPTIONS)
	$(COVERAGE_SPACE) $(REPOSITORY) integration

.PHONY: test-all
test-all: install .clean-test
	$(NOSE) $(PACKAGES) $(NOSE_OPTIONS)
	$(COVERAGE_SPACE) $(REPOSITORY) overall
{% elif cookiecutter.test_runner == "pytest" -%}
FAILURES := .cache/v/cache/lastfailed
REPORTS ?= xmlreport

PYTEST_CORE_OPTIONS := -ra -vv
PYTEST_COV_OPTIONS := --cov=$(PACKAGE) --no-cov-on-fail --cov-report=term-missing:skip-covered --cov-report=html
PYTEST_RANDOM_OPTIONS := --random --random-seed=$(RANDOM_SEED)

PYTEST_OPTIONS := $(PYTEST_CORE_OPTIONS) $(PYTEST_RANDOM_OPTIONS)
ifndef DISABLE_COVERAGE
PYTEST_OPTIONS += $(PYTEST_COV_OPTIONS)
endif
PYTEST_RERUN_OPTIONS := $(PYTEST_CORE_OPTIONS) --last-failed --exitfirst

.PHONY: test
test: test-all ## Run unit and integration tests

.PHONY: test-unit
test-unit: install
	@- mv $(FAILURES) $(FAILURES).bak
	$(PYTEST) $(PYTEST_OPTIONS) $(PACKAGE) --junitxml=$(REPORTS)/unit.xml
	@- mv $(FAILURES).bak $(FAILURES)
	$(COVERAGE_SPACE) $(REPOSITORY) unit

.PHONY: test-int
test-int: install
	@ if test -e $(FAILURES); then $(PYTEST) $(PYTEST_RERUN_OPTIONS) tests; fi
	@ rm -rf $(FAILURES)
	$(PYTEST) $(PYTEST_OPTIONS) tests --junitxml=$(REPORTS)/integration.xml
	$(COVERAGE_SPACE) $(REPOSITORY) integration

.PHONY: test-all
test-all: install
	@ if test -e $(FAILURES); then $(PYTEST) $(PYTEST_RERUN_OPTIONS) $(PACKAGES); fi
	@ rm -rf $(FAILURES)
	$(PYTEST) $(PYTEST_OPTIONS) $(PACKAGES) --junitxml=$(REPORTS)/overall.xml
	$(COVERAGE_SPACE) $(REPOSITORY) overall
{% endif %}
.PHONY: read-coverage
read-coverage:
	bin/open htmlcov/index.html

# DOCUMENTATION ################################################################

PYREVERSE := pipenv run pyreverse
MKDOCS := pipenv run mkdocs

MKDOCS_INDEX := site/index.html

.PHONY: doc
doc: uml mkdocs ## Generate documentation

.PHONY: uml
uml: install docs/*.png
docs/*.png: $(MODULES)
	$(PYREVERSE) $(PACKAGE) -p $(PACKAGE) -a 1 -f ALL -o png --ignore tests
	- mv -f classes_$(PACKAGE).png docs/classes.png
	- mv -f packages_$(PACKAGE).png docs/packages.png

.PHONY: mkdocs
mkdocs: install $(MKDOCS_INDEX)
$(MKDOCS_INDEX): mkdocs.yml docs/*.md
	ln -sf `realpath README.md --relative-to=docs` docs/index.md
	ln -sf `realpath CHANGELOG.md --relative-to=docs/about` docs/about/changelog.md
	ln -sf `realpath CONTRIBUTING.md --relative-to=docs/about` docs/about/contributing.md
	ln -sf `realpath LICENSE.md --relative-to=docs/about` docs/about/license.md
	$(MKDOCS) build --clean --strict

.PHONY: mkdocs-live
mkdocs-live: mkdocs
	eval "sleep 3; bin/open http://127.0.0.1:8000" &
	$(MKDOCS) serve

# BUILD ########################################################################

PYINSTALLER := pipenv run pyinstaller
PYINSTALLER_MAKESPEC := pipenv run pyi-makespec

DIST_FILES := dist/*.tar.gz dist/*.whl
EXE_FILES := dist/$(PROJECT).*

.PHONY: dist
dist: install $(DIST_FILES)
$(DIST_FILES): $(MODULES) README.rst CHANGELOG.rst
	rm -f $(DIST_FILES)
	pipenv run python setup.py check --restructuredtext --strict --metadata
	pipenv run python setup.py sdist
	pipenv run python setup.py bdist_wheel

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

TWINE := pipenv run twine

.PHONY: register
register: dist ## Register the project on PyPI
	@ echo NOTE: your project must be registered manually
	@ echo https://github.com/pypa/python-packaging-user-guide/issues/263
	# TODO: switch to twine when the above issue is resolved
	# $(TWINE) register dist/*.whl

.PHONY: upload
upload: .git-no-changes register ## Upload the current version to PyPI
	$(TWINE) upload dist/*.*
	bin/open https://pypi.python.org/pypi/$(PROJECT)

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
