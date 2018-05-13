
PYTHON=`which python`
NAME=`python setup.py --name`

all: test

test:
	@echo Running unittests
	@$(PYTHON) -m unittest discover --start-directory src/tests