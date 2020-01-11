LINT_DIRS := interact/

install:
	pip install -r requirements.txt

install-dev: install
	pip install -e ".[dev]"

lint:
	flake8 $(LINT_DIRS)
	black --target-version py36 --check $(LINT_DIRS)

black:
	black --target-version py36 $(LINT_DIRS)

freeze:
	CUSTOM_COMPILE_COMMAND="make freeze" pip-compile --no-index --output-file requirements.txt setup.py

freeze-upgrade:
	CUSTOM_COMPILE_COMMAND="make freeze" pip-compile --no-index --upgrade --output-file requirements.txt setup.py

.PHONY: install install-dev lint black freeze freeze-upgrade
