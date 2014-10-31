# match default value of project_name from cookiecutter.json
COOKIE := template-python

all: ci

$(COOKIE):
	cookiecutter . --no-input

.PHONY: ci
ci: $(COOKIE)
	cd $(COOKIE); make ci

.PHONY: clean
clean:
	rm -r $(COOKIE)
