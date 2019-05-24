#!/usr/bin/make -f

help:
	@echo "Usage:"
	@echo "    make help        show this message"
	@echo "    make setup       create virtual environment and install dependencies"
	@echo "    make setup_test  create virtual environment and install dependencies for development"
	@echo "    make activate    enter virtual environment"
	@echo "    make test_lite   run the test suite"
	@echo "    exit             leave virtual environment"

setup:
	python -m pip install --user pipenv
	python -m pipenv install

setup_dev:
	python -m pip install --user pipenv
	python -m pipenv install --dev

activate:
	python -m pipenv shell

test_lite:
	python -m pipenv run python -m pytest -m lite

test_nightly:
	python -m pipenv run python -m pytest -m "not custom"

evaluation:
	python -m pipenv run python -m evaluation

run:
	python -m pipenv run python -m mindefuse

.PHONY: help activate test test_lite test_nightly
