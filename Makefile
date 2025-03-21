SOURCE_FILES = Makefile cookiecutter.json {{cookiecutter.project_name}}/* {{cookiecutter.project_name}}/*/*
GENERATED_PROJECT := TemplateDemo

ENV := .venv

# MAIN ########################################################################

.PHONY: all
all: build
	make all -C $(GENERATED_PROJECT)

.PHONY: dev
dev: install
	poetry run sniffer

# DEPENDENCIES ################################################################

.PHONY: bootstrap
bootstrap:
	asdf plugin add python || asdf plugin update python
	asdf plugin add poetry || asdf plugin update poetry
	asdf install

.PHONY: doctor
doctor:
	{{cookiecutter.project_name}}/bin/verchew

.PHONY: install
install: $(ENV)
$(ENV): poetry.lock
	@ poetry config virtualenvs.in-project true
ifdef CI
	poetry install --no-root --only=main
else
	poetry install --no-root
endif
	@ touch $@

ifndef CI
poetry.lock: pyproject.toml
	poetry lock
	@ touch $@
endif

# BUILD #######################################################################

.PHONY: build
build: install $(GENERATED_PROJECT)
$(GENERATED_PROJECT): $(SOURCE_FILES)
	cat cookiecutter.json
	poetry run cookiecutter . --no-input --overwrite-if-exists
ifndef CI
	mkdir -p $(GENERATED_PROJECT)/.git
	echo '[remote "origin"]\nurl = https://github.com/jacebrowning/template-python-demo' > $(GENERATED_PROJECT)/.git/config
endif
	cd $(GENERATED_PROJECT) && poetry lock
	@ touch $(GENERATED_PROJECT)

# CLEANUP #####################################################################

.PHONY: clean
clean:
	rm -rf $(GENERATED_PROJECT)
	rm -rf $(ENV)

.DEFAULT_GOAL := install
