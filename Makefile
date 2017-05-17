SOURCE_FILES = Makefile cookiecutter.json {{cookiecutter.project_name}}/* {{cookiecutter.project_name}}/*/*
GENERATED_PROJECT := TemplateDemo

ENV := .venv

# MAIN #########################################################################

.PHONY: all
all: install

.PHONY: ci
ci: build
	make doctor ci -C $(GENERATED_PROJECT)

.PHONY: watch
watch: install clean
	pipenv run sniffer

# DEPENDENCIES #################################################################

export PIPENV_SHELL_COMPAT=true
export PIPENV_VENV_IN_PROJECT=true

.PHONY: install
install: $(ENV)
$(ENV): Pipfile*
ifdef CI
	pipenv install
else
	pipenv install --dev
endif
	@ touch $@

# BUILD ########################################################################

_COOKIECUTTER_INPLACE = cookiecutter.json > tmp && mv tmp cookiecutter.json

.PHONY: build
build: install $(GENERATED_PROJECT)
$(GENERATED_PROJECT): $(SOURCE_FILES)

# Update template for selected test runner
ifeq ($(TEST_RUNNER),nose)
	sed "s/pytest/nose/g" $(_COOKIECUTTER_INPLACE)
else ifeq ($(TEST_RUNNER),pytest)
	sed "s/nose/pytest/g" $(_COOKIECUTTER_INPLACE)
endif

# Update template for selected Python on Travis CI
ifeq ($(TRAVIS_PYTHON_VERSION),3.6)
	sed "s/2,/3,/g" $(_COOKIECUTTER_INPLACE)
	sed "s/7/6/g" $(_COOKIECUTTER_INPLACE)
endif

# Update template for selected Python on Appveyor
ifeq ($(PYTHON_MAJOR),3)
	sed "s/2,/3,/g" $(_COOKIECUTTER_INPLACE)
endif
ifeq ($(PYTHON_MINOR),6)
	sed "s/7/6/g" $(_COOKIECUTTER_INPLACE)
endif

# Generate a project from the template
	sed "s/master/python2-pytest/g" $(_COOKIECUTTER_INPLACE)
	cat cookiecutter.json
	pipenv run cookiecutter . --no-input --overwrite-if-exists
	sed "s/python2-pytest/master/g" $(_COOKIECUTTER_INPLACE)
	@ touch $(GENERATED_PROJECT)

# CLEANUP ######################################################################

.PHONY: clean
clean:
	rm -rf $(GENERATED_PROJECT)

.PHONY: clean-all
clean-all: clean
	rm -rf $(ENV)
