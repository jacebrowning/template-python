# match default value of project_name from cookiecutter.json
COOKIE := Foobar

all: test

$(COOKIE):
	cookiecutter . --no-input

.PHONY: test
test: $(COOKIE)
	cd $(COOKIE); make test

.PHONY: clean
clean:
	rm -r $(COOKIE)
