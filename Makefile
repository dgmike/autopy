PYTHON=`which python3`
PYTHON3=./venv/bin/python3
PIP=./venv/bin/pip

setup: virtualenv requiriments

virtualenv:
	virtualenv -p ${PYTHON} venv

requiriments:
	${PIP} install -r ./requiriments.txt

clean:
	rm -rf ./venv

run:
	${PYTHON3} ./manage.py runserver
