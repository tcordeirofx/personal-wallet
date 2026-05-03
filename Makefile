.PHONY: install run test

PYTHON := .venv/bin/python
PIP    := .venv/bin/pip

install:
	test -d .venv || python3 -m venv .venv
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) -m uvicorn app.main:app --reload

test:
	$(PYTHON) -m pytest
