#Makefile

clean:
	rm -rf *~* && find . -name '*.pyc' -exec rm {} \;
	
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
	sudo apt-get install -y fabric
	sudo apt-get install -y nodejs-legacy
	sudo apt-get install -y npm
	sudo npm install -g azure-cli
	azure config mode asm
	azure login
	azure site create --location "Central US" pluco-db
	azure vm create pluco-db b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_3-LTS-amd64-server-20151218-en-us-30GB pluco PlucoDB2# --location "Central US" --ssh
	azure vm start pluco-db
	azure vm endpoint create pluco-db 3306 3306
	fab -p PlucoDB2# -H pluco@pluco-db.cloudapp.net crear_mysql

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
	azure config mode asm
	azure login
	azure site create --location "North Europe" pruebas-pluco
	azure vm create pruebas-pluco b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_3-LTS-amd64-server-20151218-en-us-30GB pluco PlucoDB2# --location "North Europe" --ssh
	azure vm start pruebas-pluco
	azure vm endpoint create pruebas-pluco 8000 80
	fab -p PlucoDB2# -H pluco@pruebas-pluco.cloudapp.net montar_docker
	
azure:
	sudo apt-get install -y fabric
	sudo apt-get install -y virtualbox virtualbox-dkms
	sudo apt-get install -y vagrant
	vagrant plugin install vagrant-azure
	sudo apt-get install -y nodejs-legacy
	sudo apt-get install -y npm
	sudo npm install -g azure-cli
	sudo apt-get install -y python-pip
	sudo pip install --upgrade pip
	sudo pip install paramiko PyYAML jinja2 httplib2 ansible
	cd despliegueAzure && sudo vagrant up --provider=azure
	
push:
	git push
	fab -H pluco@pluco-iv.cloudapp.net actualizar
