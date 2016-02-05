## Entorno de pruebas con Docker

Para crear la imagen, Docker usa un fichero dentro del código de la aplicación llamado [Dockerfile](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/Dockerfile) para la construcción de la imagen, que en mi caso contiene lo siguiente:

```
# Sistema operativo
FROM ubuntu:14.04

# Autor
MAINTAINER Ruben Martin Hidalgo <rubenmartin1991@gmail.com>

# Instalacion de paquetes basicos
RUN sudo apt-get update
RUN sudo apt-get install -y git
RUN sudo apt-get install -y build-essential

# Descarga repositorio de la app
RUN sudo git clone https://github.com/romilgildo/IV-PLUCO-RMH.git

# Instalacion de la app y sus dependencias
RUN cd IV-PLUCO-RMH && git pull
RUN cd IV-PLUCO-RMH && make install
```

Luego en la web de [Docker Hub](https://hub.docker.com/), creamos un "Automated Build" sobre el repositorio de nuestro proyecto, lo cual comenzará a crear la imagen. 

![Creando automated build](http://i628.photobucket.com/albums/uu6/romilgildo/createAutomatedBuild_zpszisdsuir.png~original)

[Esta](https://hub.docker.com/r/romilgildo/pluco/) es la imagen Docker y aquí teneis una captura de la construcción automática de la imagen funcionando:

![Automated Build Docker](http://i628.photobucket.com/albums/uu6/romilgildo/automatedbuildDocker_zpsh8ttavhh.png~original)

A partir de ahora, todos los cambios realizados sobre el código del repositorio, se integran en tiempo real y de manera totalmente automatizada mediante Docker Hub, que rehará el build por su cuenta cada vez que hagamos "git push".

### Creación del entorno de pruebas en Azure

Para la instalación en una máquina virtual de Azure debemos ejecutar `make docker_Azure` que hará lo siguiente:

```
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
```

Instala todo lo necesario para crear el contenedor en Azure, con Vagrant y Ansible crea la máquina virtual y luego con Fabric crea el contenedor en dicha máquina. La función de Fabric usada es la siguiente:

```
def montar_docker():
	run('sudo apt-get update')
	run('sudo apt-get install -y docker.io')
	run('sudo docker pull romilgildo/pluco')
	run('sudo docker run -p 8000:8000 -t -i romilgildo/pluco sh -c "cd IV-PLUCO-RMH && make run"')
```

Esto instala Docker, se descarga la imagen de nuestro repositorio y arranca el contenedor, además de ejecutar la aplicación de manera automatizada. 

Aquí tenemos desplegado el contenedor Docker instalado en una máquina de Azure y disponible de manera online: [http://pluco-db.cloudapp.net:8000/](http://pruebas-pluco.cloudapp.net)

### Creación del entorno de pruebas en local

Para crear el entorno de pruebas en nuestro ordenador, se debe ejecutar el comando:

 `make docker_Local`

Esto hará lo siguiente: 

```
$ sudo apt-get update
$ sudo apt-get install -y docker.io
$ sudo docker pull romilgildo/pluco
$ sudo docker run -p 8000:8000 -t -i romilgildo/pluco /bin/bash
```

Es decir, instala Docker, crea el contenedor con la aplicación instalada en él, y arranca el entorno de pruebas. En la última orden le indicamos que el puerto 8000 del contenedor corresponderá al 8000 de la máquina virtual, de forma que podamos tener acceso a él. 

![Contenedor creado](http://i628.photobucket.com/albums/uu6/romilgildo/dockerenAzure_zpsszr0hu3b.png)

Una vez estemos dentro del contenedor, bastará con hacer `make run` en el directorio de la aplicación para ejecutar nuestra app como si estuviera localmente y así poder probar su correcto funcionamiento.

Aquí una muestra de nuestra app funcionando dentro del contenedor local, donde accedemos introduciendo la IP del contenedor Docker en el navegador del sistema anfitrión:

![Cogemos la ip del contenedor](http://i628.photobucket.com/albums/uu6/romilgildo/ipDockerLocal_zpsfmgomfwl.png)

![Pluco funcionando en Docker](http://i628.photobucket.com/albums/uu6/romilgildo/plucoenDocker_zps6tmscobl.png~original)

[Volver atrás](https://github.com/romilgildo/IV-PLUCO-RMH#entorno-de-pruebas-con-docker)
