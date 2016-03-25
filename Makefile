PIP=$(shell which pip3 || which pip)

build:
	./setup.py sdist bdist_wheel

test:
	py.test --benchmark-skip

benchmark:
	py.test --benchmark-only --benchmark-autosave --benchmark-warmup
	find .benchmarks -iname "*.json" -exec perl -pe 'END { print "\n"; }' {} \;

pre-test:
	$(PIP) install -e '.[test]'
