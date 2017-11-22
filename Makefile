ifndef CI
	PIP=$(shell which pip3 || which pip)
else
	PIP=pip
endif

build: mixedmartialtail
	./setup.py sdist bdist_wheel

clean:
	rm -rf build dist .tox

develop:
	$(PIP) install -e '.[dev]'
	./setup.py develop --user

test:
	tox

benchmark:
	py.test --benchmark-only --benchmark-autosave --benchmark-warmup
	find .benchmarks -iname "*.json" -exec perl -pe 'END { print "\n"; }' {} \;

pre-test:
	$(PIP) install -e '.[test]'

.PHONY: create-logs build-benchmark-logs

create-logs:
	$(MAKE) -C logs

logs.tar.lrz: create-logs
	lrztar -k logs

build-benchmark-logs: logs.tar.lrz
