build:
	./setup.py sdist bdist_wheel

test:
	py.test

pre-test:
	pip install -e '.[test]'
