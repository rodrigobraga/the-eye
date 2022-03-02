#!/bin/bash
.PHONY: default
.SILENT:


default:

bash:
	docker compose run --rm web bash

shell:
	docker compose run --rm web python manage.py shell_plus

migrate:
	docker compose run --rm web python manage.py migrate --noinput

makemigrations:
	docker compose run --rm web python manage.py makemigrations $(app)

runserver:  # running the server in development mode
	docker compose run --rm --service-ports -e COMMAND=development web

runworker:  # running the celery worker in development mode
	docker compose run --rm worker celery -A api worker -l INFO


logs:
	docker compose logs --follow

createsuperuser:
	docker compose run --rm web python manage.py createsuperuser

generatetoken:
	docker compose run --rm --no-deps web python manage.py get_tokens_for_user $(email)

dependencies:
	docker compose run --rm --no-deps web pip list --outdated format columns

manage:
	docker compose run --rm web python manage.py $(args)


# Test and Code Quality
# -----------------------------------------------------------------------------
load-test:
	docker compose up loadtest

test:
	docker compose run --rm web pytest

test-matching:
	docker compose run --rm web pytest -n 0 -s --pdbcls=IPython.core.debugger:Pdb -k $(k)

_isort:
	docker compose run --rm --no-deps web isort --diff --check-only .

_isort_fix:
	docker compose run --rm --no-deps web isort .

_black:
	docker compose run --rm --no-deps web black --check .

_black_fix:
	docker compose run --rm --no-deps web black .

_mypy:
	docker compose run --rm --no-deps web mypy . --exclude migrations

lint: _isort _black _mypy

format-code: _isort_fix _black_fix
