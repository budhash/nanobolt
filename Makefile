#!/usr/bin/make -f

.PHONY: setup setup-pip setup-test setup-release tests lint-code lint-yaml lint package build clean

setup:
	@echo "[Setup]: ..."
	@make setup-pip
	@make setup-dev
	@make setup-test
	@make setup-release

setup-pip:
	@echo "[Setup]: Upgrading pip ..."
	python -m pip install --upgrade pip

setup-dev:
	@echo "[Setup]: requirements.txt ..."
	pip install -r requirements.txt

setup-test:
	@echo "[Setup]: requirements.test.txt ..."
	if [ -f requirements.test.txt ]; then pip install -r requirements.test.txt; fi

setup-release:
	@echo "[Setup]: requirements.release.txt ..."
	if [ -f requirements.release.txt ]; then pip install -r requirements.release.txt; fi

tests:
	@echo "[Tests]: ..."
	@pytest -c pytest.ini

lint-code:
	@echo "[Lint]: Code ..."
	@flake8 .

lint-yaml:
	@echo "[Lint]: Yaml ..."
	@yamllint .

lint: 
	@echo "[Lint]: ..."
	@make lint-code
	@make lint-yaml

package:
	@echo "[Build]: Packaging ..."
	@changelog2version --changelog_file CHANGELOG.md --version_file nanobolt/version.py --version_file_type py --debug
	@python setup.py sdist
	@[ -f dist/*.orig ] && rm -f dist/*.orig
	@echo "[Build]: Checking ..."
	@twine check dist/*

clean:
	# Remove .pytest_cache directory
	@rm -rf .pytest_cache
	# Remove __pycache__ directories
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	# Remove dist directory
	@rm -rf dist
	# Remove directories with *.egg-info
	@find . -type d -name '*.egg-info' -exec rm -rf {} +
	# Remove MANIFEST file
	@rm -f MANIFEST
	# Remove output directory
	@rm -rf output
	# Remove .coverage file
	@rm -f .coverage

build:
	@make clean
	@make test
	@make package
