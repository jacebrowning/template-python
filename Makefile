SOURCE_FILES = Makefile cookiecutter.json {{cookiecutter.project_name}}/* {{cookiecutter.project_name}}/*/*

GENERATED_PROJECT := TemplateDemo

# MAIN #########################################################################

.PHONY: all
all: $(GENERATED_PROJECT)
	make $@ -C $<

.PHONY: doctor
doctor: $(GENERATED_PROJECT)
	make $@ -C $<

.PHONY: ci
ci: $(GENERATED_PROJECT)
	make $@ -C $<

.PHONY: watch
watch: clean
	sniffer

# BUILD ########################################################################

_COOKIECUTTER_INPLACE = cookiecutter.json > tmp && mv tmp cookiecutter.json

.PHONY: build
build: $(GENERATED_PROJECT)
$(GENERATED_PROJECT): $(SOURCE_FILES)

# Update template for selected test runner
ifeq ($(TEST_RUNNER),nose)
	sed "s/pytest/nose/g" $(_COOKIECUTTER_INPLACE)
else ifeq ($(TEST_RUNNER),pytest)
	sed "s/nose/pytest/g" $(_COOKIECUTTER_INPLACE)
endif

# Update template for selected Python on Travis CI
ifeq ($(TRAVIS_PYTHON_VERSION),3.3)
	sed "s/2,/3,/g" $(_COOKIECUTTER_INPLACE)
	sed "s/7/3/g" $(_COOKIECUTTER_INPLACE)
else ifeq ($(TRAVIS_PYTHON_VERSION),3.4)
	sed "s/2,/3,/g" $(_COOKIECUTTER_INPLACE)
	sed "s/7/4/g" $(_COOKIECUTTER_INPLACE)
else ifeq ($(TRAVIS_PYTHON_VERSION),3.5)
	sed "s/2,/3,/g" $(_COOKIECUTTER_INPLACE)
	sed "s/7/5/g" $(_COOKIECUTTER_INPLACE)
endif

# Update template for selected Python on Appveyor
ifeq ($(PYTHON_MAJOR),3)
	sed "s/2,/3,/g" $(_COOKIECUTTER_INPLACE)
endif
ifeq ($(PYTHON_MINOR),3)
	sed "s/7/3/g" $(_COOKIECUTTER_INPLACE)
else ifeq ($(PYTHON_MINOR),4)
	sed "s/7/4/g" $(_COOKIECUTTER_INPLACE)
else ifeq ($(PYTHON_MINOR),5)
	sed "s/7/5/g" $(_COOKIECUTTER_INPLACE)
endif

# Generate a project from the template
	sed "s/master/python2-pytest/g" $(_COOKIECUTTER_INPLACE)
	cat cookiecutter.json
	cookiecutter . --no-input --overwrite-if-exists
	sed "s/python2-pytest/master/g" $(_COOKIECUTTER_INPLACE)
	@ touch $(GENERATED_PROJECT)

# CLEANUP ######################################################################

.PHONY: clean
clean:
	rm -rf $(GENERATED_PROJECT)
