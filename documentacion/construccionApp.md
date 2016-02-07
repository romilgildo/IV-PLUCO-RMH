## Herramienta de construcción con Make

Mediante esta herramienta podremos ejecutar las opciones de limpieza, realización de tests, ejecución del servidor y opciones de despliegue.

Para ejecutar la herramienta de construcción, simplemente debemos escribir en la terminal el comando **make** seguido de la opción que queramos ejecutar (clean, test, run...).

Aquí un ejemplo de su funcionamiento:

![Ejemplo de make](http://i628.photobucket.com/albums/uu6/romilgildo/testPluco_zps40wctlgf.png)

Mi [Makefile](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/Makefile) contiene lo siguiente:

```
clean:
	sudo rm -i -rf *~* && find . -name '*.pyc' -exec rm {} \;
	
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
	wget https://releases.hashicorp.com/vagrant/1.8.1/vagrant_1.8.1_x86_64.deb
	sudo dpkg -i vagrant_1.8.1_x86_64.deb
	rm vagrant_1.8.1_x86_64.deb
	vagrant plugin install vagrant-azure
	sudo apt-get install -y python-pip
	sudo pip install --upgrade pip
	sudo pip install paramiko PyYAML jinja2 httplib2 ansible
	sudo vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box --force
	cd despliegueMySQL && sudo vagrant up --provider=azure

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

docker_Local:
	sudo apt-get update
	sudo apt-get install -y docker.io
	sudo docker pull romilgildo/pluco
	sudo docker run -p 8000:8000 -t -i romilgildo/pluco /bin/bash

docker_Azure:
	sudo apt-get install -y fabric
	sudo apt-get install -y virtualbox virtualbox-dkms
	wget https://releases.hashicorp.com/vagrant/1.8.1/vagrant_1.8.1_x86_64.deb
	sudo dpkg -i vagrant_1.8.1_x86_64.deb
	rm vagrant_1.8.1_x86_64.deb
	vagrant plugin install vagrant-azure
	sudo vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box --force
	cd despliegueDocker && sudo vagrant up --provider=azure
	cd ..
	fab -p PlucoDB1# -H pluco@pruebas-pluco.cloudapp.net montar_docker
	
azure:
	sudo apt-get install -y fabric
	sudo apt-get install -y virtualbox virtualbox-dkms
	wget https://releases.hashicorp.com/vagrant/1.8.1/vagrant_1.8.1_x86_64.deb
	sudo dpkg -i vagrant_1.8.1_x86_64.deb
	rm vagrant_1.8.1_x86_64.deb
	vagrant plugin install vagrant-azure
	sudo apt-get install -y python-pip
	sudo pip install --upgrade pip
	sudo pip install paramiko PyYAML jinja2 httplib2 ansible
	sudo vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box --force
	cd despliegueAzure && sudo vagrant up --provider=azure
	
push:
	sudo git add -A .
	git status
	sudo despliegueAzure/escribirCommit.sh
	git push
	fab -p PlucoDB1# -H pluco@pluco-iv.cloudapp.net actualizar
	sudo python manage.py syncdb

```

Con la orden `make clean` limpiaremos los directorios en local de archivos temporales que no influyen en el correcto funcionamiento de la aplicación.

Con `make install` se instalan los paquetes necesarios para el correcto funcionamiento de la app. 

La orden `make mysql` crea las bases de datos oportunas en una máquina virtual de Azure independiente.

El comando `make test` realizará los tests que tengamos en el archivo destinado para ello. Indica dónde se encuentra el settings de Django y ejecuta nosetests.

Con `make run` ejecutamos la aplicación por el puerto 8000.

La orden `make heroku` sirve para desplegar la aplicación en Heroku.

El comando `make docker_Local` crea un contenedor Docker en nuestro ordenador con la app instalada dentro.

Con `make docker_Azure` creamos un contenedor Docker en una máquina de Azure con la aplicación instalada en éĺ y la ejecuta automáticamente.

Si ejecutamos `make azure` se realizará el despliegue en una máquina virtual de Azure, quedando la aplicación accesible de manera online.

El comando `make push` actualiza el repositorio y luego entra en nuestra máquina de Azure para actualizar la aplicación y así quede actualizada en la web.

[Volver atrás](https://github.com/romilgildo/IV-PLUCO-RMH#herramienta-de-construcción-con-make)
