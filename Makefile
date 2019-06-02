PIP=python -m pip
PYR=python -m pipenv
PRINT=python -c "import sys; print(str(sys.argv[1]))"

help:
	$(PRINT) "Usage:"
	$(PRINT) "    help          show this message"
	$(PRINT) "    setup         create virtual environment and install dependencies"
	$(PRINT) "    setup_dev     create virtual environment and install development dependencies"
	$(PRINT) "    run           run mindefuse application"
	$(PRINT) "    dist          package application for distribution"
    $(PRINT) "    test_lite     run the lite test suite"
	$(PRINT) "    test_nightly  run a longer test suite"
	$(PRINT) "    evaluation    run mindefuse evaluation tests"
	$(PRINT) "    clean         remove the project dependencies and environment"

setup:
	$(PIP) install pipenv
	$(PYR) install --three

setup_dev:
	$(PIP) install pipenv
	$(PYR) install --three --dev

dist:
	$(PYR) run python setup.py bdist_wheel

run:
	$(PYR) run python -m mindefuse

clean:
	$(PYR) --rm

test_lite:
	$(PYR) run python -m pytest -m lite

test_nightly:
	$(PYR) run python -m pytest -m "not custom"

evaluation:
	$(PYR) run python -m evaluation

.PHONY: run setup setup_dev dist clean test_lite test_nightly evaluation
