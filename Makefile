
PYTHON=`which python`
NAME=`python setup.py --name`

all: test

test:
	$(PYTHON) -m unittest discover -t .