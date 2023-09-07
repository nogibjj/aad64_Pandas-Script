venv:
	python3 -m venv venv

install: venv
	venv/bin/pip install --upgrade pip -r requirements.txt

test:
	venv/bin/python -m pytest -vv --cov=main test_*.py

format:
	venv/bin/black *.py

lint:
	venv/bin/pylint --disable=R,C --ignore-patterns=test_.*?py *.py

run:
	python main.py

all: venv install lint format test
