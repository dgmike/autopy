PYTHON=`which python3`
PIP=./venv/bin/pip

setup: virtualenv requiriments

virtualenv:
	virtualenv -p ${PYTHON} venv

requiriments:
	${PIP} install -r ./requiriments.txt

clean:
	rm -rf ./venv

