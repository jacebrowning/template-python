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
	sed -i '' "s/pytest/nose/g" cookiecutter.json
else ifeq ($(TEST_RUNNER),pytest)
	sed -i '' "s/nose/pytest/g" cookiecutter.json
endif
	cookiecutter . --no-input

.PHONY: clean
clean:
	rm -rf $(COOKIE)
