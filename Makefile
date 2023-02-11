all:
	install lint

install:
	pip install --upgrade pip
	pip install -r requirements.txt

lint:
	pylint --disable=R,C,W1203,W0702 app.py