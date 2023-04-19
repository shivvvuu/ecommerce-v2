.PHONY: run
run:
	 python manage.py runserver

.PHONY: makemigrations
makemigrations:
	 python manage.py load-fixtures

.PHONY: test
test:
	 pytest

	