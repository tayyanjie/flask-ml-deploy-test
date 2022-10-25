install:
	python3 -m pip install --upgrade pip
	pip3 install -r requirements.txt

format:
	black *.py
	black app/*.py

lint:
	pylint --disable=R,C *.py
	pylint app/*.py

test:
	python -m pytest -vv test.py
	python -m pytest -vv app/test_app.py

all: install lint test
