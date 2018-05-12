
PYTHON=`which python`
NAME=`python setup.py --name`

all: test

test:
	@echo Running unittests
	@$(PYTHON) -m unittest src/tests/testbadchrheuristics.py