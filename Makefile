.PHONY: clean

virtualenv_run: requirements.txt
	bin/venv-update venv= -p python3.5 virtualenv_run install= -r requirements.txt

clean:
	rm -rf virtualenv_run/