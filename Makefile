# match default value of project_name from cookiecutter.json
COOKIE := Foobar

BASE_CC := {{cookiecutter.project_name}}
CC_FILES := $(BASE_CC)/* $(BASE_CC)/*/* $(BASE_CC)/*/*/*

.PHONY: all
all: $(COOKIE)
	cd $(COOKIE); make

.PHONY: ci
ci: $(COOKIE)
	cd $(COOKIE); make ci

$(COOKIE): Makefile cookiecutter.json $(CC_FILES)
	cookiecutter . --no-input

.PHONY: clean
clean:
	rm -r $(COOKIE)
