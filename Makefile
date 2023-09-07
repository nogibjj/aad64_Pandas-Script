#venv:
#	python3 -m venv venv

install: venv
	pip install --upgrade pip -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py

format:
	black *.py

lint:
#	pylint --disable=R,C --ignore-patterns=test_.*?py *.py
	ruff check *.py

run:
	python main.py

all: venv install lint format test
