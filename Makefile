# Makefile for running Django development server

.PHONY: run migrate makemigrations createsuperuser test

PYTHON=python3
MANAGE=manage.py

# run django server
run:
	$(PYTHON) $(MANAGE) runserver

makemigrations:
	$(PYTHON) $(MANAGE) makemigrations

migrate:
	$(PYTHON) $(MANAGE) migrate

createsuperuser:
	$(PYTHON) $(MANAGE) createsuperuser

test:
	$(PYTHON) $(MANAGE) test
