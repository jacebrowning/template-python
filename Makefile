# match default value of project_name from cookiecutter.json
COOKIE := PythonTemplateDemo

BASE_CC := {{cookiecutter.project_name}}
CC_FILES := $(BASE_CC)/* $(BASE_CC)/*/* $(BASE_CC)/*/*/*

.PHONY: all
all: $(COOKIE)
	cd $(COOKIE); make

.PHONY: ci
ci: $(COOKIE)
	cd $(COOKIE); make ci

_COOKIECUTTER_INPLACE = cookiecutter.json > tmp && mv tmp cookiecutter.json

$(COOKIE): Makefile cookiecutter.json $(CC_FILES)
ifeq ($(TEST_RUNNER),nose)
	sed "s/pytest/nose/g" $(_COOKIECUTTER_INPLACE)
else ifeq ($(TEST_RUNNER),pytest)
	sed "s/nose/pytest/g" $(_COOKIECUTTER_INPLACE)
endif
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
	sed "s/master/python2-pytest/g" $(_COOKIECUTTER_INPLACE)
	cat cookiecutter.json
	cookiecutter . --no-input --overwrite-if-exists
	sed "s/python2-pytest/master/g" $(_COOKIECUTTER_INPLACE)

.PHONY: watch
watch:
	pip install sniffer MacFSEvents
	sniffer

.PHONY: clean
clean:
	rm -rf $(COOKIE)
