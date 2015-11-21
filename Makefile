#Makefile

clean:
	rm -rf *~* && find . -name '*.pyc' -exec rm {} \;
	
install:
	sudo apt-get update 
	sudo apt-get install -y libmysqlclient-dev
	sudo apt-get install -y python-dev
	sudo apt-get install -y python-pip
	sudo pip install --upgrade pip
	sudo pip install -r requirements.txt

test: 
	export DJANGO_SETTINGS_MODULE=plucoapp.settings && nosetests
	
run:
	python manage.py runserver 0.0.0.0:8000
	
heroku:
	wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh   # descargar herramienta heroku CLI
	heroku login
	heroku create
	git add .
	git commit -m "despliegue en heroku"
	git push heroku master
	heroku ps:scale web=1
	heroku open

docker:
	sudo apt-get update
	sudo apt-get install -y docker.io
	sudo docker pull romilgildo/pluco
	sudo docker run -t -i romilgildo/pluco /bin/bash
