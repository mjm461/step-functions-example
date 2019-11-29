.DEFAULT_GOAL := all


bundle:

lambci:

build:
	python setup.py build

clean:
	@rm -rf src/*.egg-info/ temp .pytest_cache/ .tox .coverage

all: build test

test:
	tox
