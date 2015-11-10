#Makefile

clean:
	rm -rf *~* && find . -name '*.pyc' -exec rm {} \;
	
install:
	sudo apt-get update 
	sudo apt-get install libmysqlclient-dev
	sudo apt-get install python-dev
	sudo apt-get install python-pip
	sudo pip install --upgrade pip
	sudo pip install -r requirements.txt

test: 
	export DJANGO_SETTINGS_MODULE=plucoapp.settings && nosetests
	
run:
	python manage.py runserver 0.0.0.0:8000
	
deploy:
	wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh   # descargar herramienta heroku CLI
	heroku login
	heroku create
	git add .
	git commit -m "despliegue en heroku"
	git push heroku master
	heroku ps:scale web=1
	heroku open
