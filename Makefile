all: install test

install:
	python setup.py install

test:
	specloud tests

deps:
	@pip install -r requirements.txt

ci: deps test

