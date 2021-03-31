serve:
	python3 manage.py runserver

shell:
	python3 manage.py shell

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser

