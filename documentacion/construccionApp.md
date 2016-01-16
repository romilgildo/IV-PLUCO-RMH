## Herramienta de construcción con Make

Mediante esta herramienta podremos ejecutar las opciones de limpieza, realización de tests, ejecución del servidor y opciones de despliegue.

Para ejecutar la herramienta de construcción, simplemente debemos escribir en la terminal el comando **make** seguido de la opción que queramos ejecutar (clean, test, run...).

Aquí un ejemplo de su funcionamiento:

![Ejemplo de make](http://i628.photobucket.com/albums/uu6/romilgildo/testPluco_zps40wctlgf.png)

Mi [Makefile](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/Makefile) contiene lo siguiente:

```
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
	sudo docker run -p 8000:8000 -t -i romilgildo/pluco /bin/bash
	
azure:
	sudo apt-get update
	sudo apt-get install nodejs-legacy
	sudo apt-get install npm
	sudo npm install -g azure-cli
	sudo pip install paramiko PyYAML jinja2 httplib2 ansible
	sudo apt-get install -y vagrant
	sudo apt-get install -y virtualbox virtualbox-dkms
	sudo apt-get install -y fabric
	vagrant plugin install vagrant-azure
	sudo vagrant up --provider=azure
	
push:
	git push
	fab -H pluco@pluco-iv.cloudapp.net actualizar

```

Con la orden `make clean` limpiaremos los directorios en local de archivos temporales que no influyen en el correcto funcionamiento de la aplicación.

Con `make install` se instalan los paquetes necesarios para el correcto funcionamiento de la app. 

El comando `make test` realizará los tests que tengamos en el archivo destinado para ello. Indica dónde se encuentra el settings de Django y ejecuta nosetests.

Con `make run` ejecutamos la aplicación por el puerto 8000.

La orden `make heroku` sirve para desplegar la aplicación en Heroku.

Con `make docker` creamos un contenedor en docker con la aplicación instalada en eĺ y entramos en dicho contenedor automáticamente.

Si ejecutamos `make azure` se realizará el despliegue en una máquina virtual de Azure, quedando la aplicación accesible de manera online.

El comando `make push` actualiza el repositorio y luego entra en nuestra máquina de Azure para actualizar la aplicación y así quede actualizada mediante web.
