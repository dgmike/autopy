PYTHON=`which python3`
PYTHON3=./venv/bin/python3
PIP=./venv/bin/pip

MANAGE=${PYTHON3} ./manage.py

run:
	${MANAGE} runserver

setup: virtualenv requiriments migrate

virtualenv:
	virtualenv -p ${PYTHON} venv

requiriments:
	${PIP} install -r ./requiriments.txt
	bower install

migrate:
	${MANAGE} migrate

clean:
	rm -rf ./venv ./bower_components

test: pytest

pytest:
	${MANAGE} test

shell:
	${MANAGE} shell
