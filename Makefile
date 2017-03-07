.PHONY: help
help:
	@echo help - this help message
	@echo run CLIENT_ID=<id> CLIENT_SECRET=<secret> - run the module
	@echo gather_keys_oauth2 - get script
	@echo virtualenv_run - create virtual env
	@echo development - setup develpoment environment
	@echo clean - clean

.PHONY: run
run: virtualenv_run gather_keys_oauth2.py
	virtualenv_run/bin/python gather_keys_oauth2.py $(CLIENT_ID) $(CLIENT_SECRET)

gather_keys_oauth2.py: virtualenv_run
	wget https://raw.githubusercontent.com/orcasgit/python-fitbit/master/gather_keys_oauth2.py

virtualenv_run: requirements.txt requirements-dev.txt
	bin/venv-update venv= -p python2.7 virtualenv_run install= -r requirements-dev.txt

.PHONY: development
development: virtualenv_run
	virtualenv_run/bin/pre-commit autoupdate
	virtualenv_run/bin/pre-commit install

.PHONY: clean
clean:
	rm -rf virtualenv_run/
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
