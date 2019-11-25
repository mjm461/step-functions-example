.DEFAULT_GOAL := all

clean:
	rm -fr .tox build dist

bundle:

build:
	python setup.py build

all: build test

test:
	tox
