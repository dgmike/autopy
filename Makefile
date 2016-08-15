PYTHON=`which python3`
PYTHON3=./venv/bin/python3
PIP=./venv/bin/pip

run:
	${PYTHON3} ./manage.py runserver

setup: virtualenv requiriments

virtualenv:
	virtualenv -p ${PYTHON} venv

requiriments:
	${PIP} install -r ./requiriments.txt
	bower install

clean:
	rm -rf ./venv ./bower_components
