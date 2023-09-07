install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py

format:
	black *.py

lint:
	generated-members=pandas.*
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

run:
	python main.py

all: install lint format test
