# match default value of project_name from cookiecutter.json
COOKIE := template-python

all: test

$(COOKIE):
	cookiecutter . --no-input

.PHONY: test
test: $(COOKIE)
	cd $(COOKIE); make test

.PHONY: check
check: $(COOKIE)
	cd $(COOKIE); make check

.PHONY: clean
clean:
	rm -r $(COOKIE)
