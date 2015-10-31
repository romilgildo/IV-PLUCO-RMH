#Makefile

clean:
	rm -rf *~*
	find . -name '*.pyc' -exec rm {} \;

test: 
	export DJANGO_SETTINGS_MODULE=plucoapp.settings
	nosetests
	
run:
	python manage.py runserver 0.0.0.0:8000
