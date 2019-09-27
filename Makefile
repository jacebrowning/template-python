SOURCE_FILES = Makefile cookiecutter.json {{cookiecutter.project_name}}/* {{cookiecutter.project_name}}/*/*
GENERATED_PROJECT := TemplateDemo

ENV := .venv

# MAIN #########################################################################

.PHONY: all
all: install

.PHONY: ci
ci: build
	make doctor -C $(GENERATED_PROJECT)
	make install -C $(GENERATED_PROJECT)
	make ci -C $(GENERATED_PROJECT)

.PHONY: watch
watch: install clean
	poetry run sniffer

# DEPENDENCIES #################################################################

.PHONY: install
install: $(ENV)
$(ENV): pyproject.toml poetry.lock
	@ poetry config virtualenvs.in-project true
ifdef CI
	poetry install --no-dev
else
	poetry install
endif
	@ touch $@

# BUILD ########################################################################

.PHONY: build
build: install $(GENERATED_PROJECT)
$(GENERATED_PROJECT): $(SOURCE_FILES)
	cat cookiecutter.json
	poetry run cookiecutter . --no-input --overwrite-if-exists
	cd $(GENERATED_PROJECT) && poetry lock
	@ touch $(GENERATED_PROJECT)

# CLEANUP ######################################################################

.PHONY: clean
clean:
	rm -rf $(GENERATED_PROJECT)

.PHONY: clean-all
clean-all: clean
	rm -rf $(ENV)
