.PHONY: pre-commit_update clean

virtualenv_run: requirements.txt requirements-dev.txt
	bin/venv-update venv= -p python3.5 virtualenv_run install= -r requirements-dev.txt

pre-commit_update: virtualenv_run
	virtualenv_run/bin/pre-commit autoupdate

clean:
	rm -rf virtualenv_run/
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
