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

$(COOKIE): Makefile cookiecutter.json $(CC_FILES)
ifeq ($(TEST_RUNNER),nose)
	sed "s/pytest/nose/g" cookiecutter.json > tmp && mv tmp cookiecutter.json
else ifeq ($(TEST_RUNNER),pytest)
	sed "s/nose/pytest/g" cookiecutter.json > tmp && mv tmp cookiecutter.json
endif
ifeq ($(TRAVIS_PYTHON_VERSION),3.3)
	sed "s/2,/3,/g" cookiecutter.json > tmp && mv tmp cookiecutter.json
	sed "s/7/3/g" cookiecutter.json > tmp && mv tmp cookiecutter.json
else ifeq ($(TRAVIS_PYTHON_VERSION),3.4)
	sed "s/2,/3,/g" cookiecutter.json > tmp && mv tmp cookiecutter.json
	sed "s/7/4/g" cookiecutter.json > tmp && mv tmp cookiecutter.json
else ifeq ($(TRAVIS_PYTHON_VERSION),3.5)
	sed "s/2,/3,/g" cookiecutter.json > tmp && mv tmp cookiecutter.json
	sed "s/7/5/g" cookiecutter.json > tmp && mv tmp cookiecutter.json
endif
	cat cookiecutter.json
	cookiecutter . --no-input

.PHONY: watch
watch:
	pip install sniffer MacFSEvents
	sniffer

.PHONY: clean
clean:
	rm -rf $(COOKIE)
