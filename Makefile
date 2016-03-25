PIP=$(shell which pip3 || which pip)

build:
	./setup.py sdist bdist_wheel

test:
	py.test

pre-test:
	$(PIP) install -e '.[test]'
