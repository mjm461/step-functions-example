.DEFAULT_GOAL := all

build.init.dir:
	@mkdir -p ../.eggs
	@ln -sf ../.eggs

bundle:

lambci:

build: build.init.dir
	python setup.py build

clean:
	@rm -rf src/*.egg-info/ temp .pytest_cache/ .tox .coverage

all: build test

test: build.init.dir
	python setup.py test
