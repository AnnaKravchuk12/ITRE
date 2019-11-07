.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	@pipenv --python 3.7
	@pipenv install pytest
	@pipenv install ntplib

test:
	@echo "Start tests."
	@pipenv run pytest tests/tests.py

run:
	@echo "Run Python app."
	@pipenv run python app.py

deploy:
	@echo "Adding and Committing results.txt to git."
	@git add results.txt
	@git commit -m "lab2 add results.txt"
	@git push origin master
