.PHONY: debug run pre-commit_update clean

run: virtualenv_run
	python src/OAuth2ResponseServer.py flask run

debug: virtualenv_run
	python -m pdb src/OAuth2ResponseServer.py

virtualenv_run: requirements.txt requirements-dev.txt
	bin/venv-update venv= -p python3.5 virtualenv_run install= -r requirements-dev.txt

pre-commit_update: virtualenv_run
	virtualenv_run/bin/pre-commit autoupdate

clean:
	rm -rf virtualenv_run/
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
