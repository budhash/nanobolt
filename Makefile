#!/usr/bin/make -f

DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY: setup setup-pip setup-dev setup-test setup-release tests lint-code lint-yaml lint package build clean check git-check matrix

setup-pip:
	@echo "[Setup]: Upgrading pip ..."
	@python -m pip install --upgrade pip

setup-dev: setup-pip
	@echo "[Setup]: requirements.txt ..."
	@pip install -r $(DIR)/requirements.txt

setup-test: setup-dev
	@echo "[Setup]: test-requirements.txt ..."
	if [ -f $(DIR)/test-requirements.txt ]; then pip install -r $(DIR)/test-requirements.txt; fi

setup-release: setup-dev
	@echo "[Setup]: release-requirements.txt ..."
	if [ -f $(DIR)/release-requirements.txt ]; then pip install -r $(DIR)/release-requirements.txt; fi

setup: setup-pip setup-dev setup-test setup-release
	@echo "[Setup]: ..."

tests: setup-test
	@echo "[Tests]: ..."
	@pytest -c $(DIR)/pyproject.toml

lint-code: setup-test
	@echo "[Lint]: Code ..."
	@ruff check . --config $(DIR)/pyproject.toml -v --fix --exit-non-zero-on-fix

lint-type: setup-test
	@echo "[Lint]: Type ..."
	@mypy --config-file $(DIR)/pyproject.toml

lint-yaml: setup-test
	@echo "[Lint]: Yaml ..."
	@yamllint -c $(DIR)/.yamllint .

lint: lint-code lint-type lint-yaml
	@echo "[Lint]: ..."

format: setup-test
	@echo "[Format]: Code ..."
	@black --config $(DIR)/pyproject.toml .

package:
	@echo "[Build]: Packaging ..."
	@changelog2version --changelog_file $(DIR)/CHANGELOG.md --version_file $(DIR)/nanobolt/version.py --version_file_type py --debug
	@python $(DIR)/setup.py sdist
	#@python $(DIR)/setup.py bdist_wheel
	@[ -f $(DIR)/dist/*.orig ] && rm -f $(DIR)/dist/*.orig
	@echo "[Build]: Checking ..."
	@twine check $(DIR)/dist/*

clean:
	# Remove .cache directory [.cache/ruff .cache/mypy .cache/pytest]
	@rm -rf $(DIR)/.cache
	# Remove __pycache__ directories
	@find $(DIR) -type d -name '__pycache__' -exec rm -rf {} +
	# Remove dist directory
	@rm -rf $(DIR)/dist
	# Remove directories with *.egg-info
	@find $(DIR) -type d -name '*.egg-info' -exec rm -rf {} +
	# Remove MANIFEST file
	@rm -f $(DIR)/MANIFEST
	# Remove output directory
	@rm -rf $(DIR)/output
	# Remove .coverage file
	@rm -f $(DIR)/.coverage

build: format lint tests package

rebuild: clean build

git-check:
	@pre-commit run --all-files

check: lint git-check

matrix:
	@python .github/commands/matrix metadata.json
