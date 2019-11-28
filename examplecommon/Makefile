.DEFAULT_GOAL := all

clean:
	@rm -rf src/*.egg-info/ temp .pytest_cache/ .tox .coverage

bundle:

build:
	python setup.py build

all: build test

test:
	tox
