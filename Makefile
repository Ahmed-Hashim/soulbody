run: 
	python manage.py runserver

m:
	python manage.py migrate

mm:
	python manage.py makemigrations

user:
	python manage.py createsuperuser
	
collect :
	python manage.py collectstatic --noinput
sca : 
	celery -A project worker -B --loglevel=INFO
newenv : 
	python3 -m venv env
venv : 
	source env/bin/activate
req : 
	pip install -r requirements.txt