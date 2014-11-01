# match default value of project_name from cookiecutter.json
COOKIE := Foobar

.PHONY: all
all: $(COOKIE)
	cd $(COOKIE); make

.PHONY: ci
ci: $(COOKIE)
	cd $(COOKIE); make ci

$(COOKIE):
	cookiecutter . --no-input

.PHONY: clean
clean:
	rm -r $(COOKIE)
