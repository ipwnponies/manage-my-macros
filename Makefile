.PHONY: development clean

virtualenv_run: requirements.txt requirements-dev.txt
	bin/venv-update venv= -p python3.5 virtualenv_run install= -r requirements-dev.txt

development: virtualenv_run
	virtualenv_run/bin/pre-commit autoupdate
	virtualenv_run/bin/pre-commit install


clean:
	rm -rf virtualenv_run/
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
