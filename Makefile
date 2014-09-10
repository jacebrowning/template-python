# match default value of project_name from cookiecutter.json
COOKIE := Foobar

all: test

.PHONY:
cutter:
	@if ! hash cookiecutter &> /dev/null; \
	then                                  \
		pip install cookiecutter;         \
	fi;

$(COOKIE): cutter
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
