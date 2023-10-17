install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py
	ruff check *.py

test:
	python -m pytest -vv --cov=main test_*.py
	pytest --nbval test.ipynb

deploy:
	#deploy goes here

setup_package: 
	python setup.py develop

databricks-query:
	databricks-query

all: install lint deploy format test setup_package databricks-cli