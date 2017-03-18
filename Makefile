ifndef CI
	PIP=$(shell which pip3 || which pip)
else
	PIP=pip
endif

build: mixedmartialtail
	./setup.py sdist bdist_wheel

develop:
	./setup.py develop --user

test:
	py.test --benchmark-skip

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
