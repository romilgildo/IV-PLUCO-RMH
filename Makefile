#Makefile

clean:
	rm -rf *~* && find . -name '*.pyc' -exec rm {} \;
	
install:
	sudo apt-get update 
	sudo apt-get install libmysqlclient-dev
	sudo apt-get install python-dev
	sudo pip install --upgrade pip
	sudo pip install -r requirements.txt

test: 
	export DJANGO_SETTINGS_MODULE=plucoapp.settings && nosetests
	
runlocal:
	python manage.py runserver 0.0.0.0:8000

runserver:
	python manage.py runserver
