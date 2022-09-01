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

all: install lint test