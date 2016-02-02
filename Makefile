#Makefile

clean:
	rm -i -rf *~* && find . -name '*.pyc' -exec rm {} \;
	
install:
	sudo apt-get update 
	sudo apt-get install -y libmysqlclient-dev
	sudo apt-get install -y python-dev
	sudo apt-get install -y libjpeg8-dev
	sudo apt-get install -y libtiff4-dev
	sudo apt-get install -y zlib1g-dev
	sudo apt-get install -y libfreetype6-dev
	sudo apt-get install -y liblcms1-dev
	sudo apt-get install -y libwebp-dev
	sudo apt-get install -y python-pip
	sudo pip install --upgrade pip
	sudo pip install -r requirements.txt
	
mysql:
	sudo apt-get install -y virtualbox virtualbox-dkms
	sudo apt-get install -y vagrant
	vagrant plugin install vagrant-azure
	sudo apt-get install -y python-pip
	sudo pip install --upgrade pip
	sudo pip install paramiko PyYAML jinja2 httplib2 ansible
	cd despliegueMySQL && sudo vagrant up --provider=azure
	cd ..	

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
	sudo apt-get install -y fabric
	sudo apt-get install -y virtualbox virtualbox-dkms
	sudo apt-get install -y vagrant
	vagrant plugin install vagrant-azure
	sudo apt-get install -y python-pip
	sudo pip install --upgrade pip
	sudo pip install paramiko PyYAML jinja2 httplib2 ansible
	cd despliegueDocker && sudo vagrant up --provider=azure
	cd ..
	fab -p PlucoDB1# -H pluco@pruebas-pluco.cloudapp.net montar_docker
	
azure:
	sudo apt-get install -y fabric
	sudo apt-get install -y virtualbox virtualbox-dkms
	sudo apt-get install -y vagrant
	vagrant plugin install vagrant-azure
	sudo apt-get install -y python-pip
	sudo pip install --upgrade pip
	sudo pip install paramiko PyYAML jinja2 httplib2 ansible
	cd despliegueAzure && sudo vagrant up --provider=azure
	cd ..
	ssh-copy-id -i ~/.ssh/id_rsa.pub pluco@pluco-iv.cloudapp.net
	
push:
	git add -A .
	git status
	sudo despliegueAzure/escribirCommit.sh
	git push
	fab -H pluco@pluco-iv.cloudapp.net actualizar
	python manage.py syncdb
