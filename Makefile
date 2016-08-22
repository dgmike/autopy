PYTHON=`which python3`
PYTHON3=./venv/bin/python3
PIP=./venv/bin/pip

run:
	${PYTHON3} ./manage.py runserver

setup: virtualenv requiriments migrate

virtualenv:
	virtualenv -p ${PYTHON} venv

requiriments:
	${PIP} install -r ./requiriments.txt
	bower install

migrate:
	${PYTHON3} ./manage.py migrate

clean:
	rm -rf ./venv ./bower_components

test: pytest

pytest:
	${PYTHON3} ./manage.py test

shell:
	${PYTHON3} ./manage.py shell
