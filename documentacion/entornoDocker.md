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

### Creación del entorno de pruebas en local

Para crear el entorno de pruebas en nuestro ordenador, se debe ejecutar el comando:

`make docker`

Esto hará lo siguiente: 

```
$ sudo apt-get update
$ sudo apt-get install -y docker.io
$ sudo docker pull romilgildo/pluco
$ sudo docker run -p 8000:8000 -t -i romilgildo/pluco /bin/bash
```

Es decir, instala Docker, crea el contenedor con la aplicación instalada en él, y arranca el entorno de pruebas. En la última orden le indicamos que el puerto 8000 del contenedor corresponderá al 8000 de la máquina virtual, de forma que podamos tener acceso a él. 

Una vez estemos dentro del contenedor, bastará con hacer `make run` en el directorio de la aplicación para ejecutar nuestra app como si estuviera localmente y así poder probar su correcto funcionamiento.

Aquí una muestra del funcionamiento de nuestra app dentro del contenedor local, donde accedemos introduciendo la IP del contenedor Docker en el navegador del sistema anfitrión:

![Cogemos la ip del contenedor](http://i628.photobucket.com/albums/uu6/romilgildo/ipDockerLocal_zpsfmgomfwl.png)

![Pluco funcionando en Docker](http://i628.photobucket.com/albums/uu6/romilgildo/plucoenDocker_zps6tmscobl.png~original)

### Creación del entorno de pruebas en Azure

Para la instalación en una máquina virtual de Azure debemos seguir los siguientes pasos:

1. Crear la máquina virtual en Azure y añadir el puerto 8000 a los extremos. Puedes consultar más detalles de este paso [aquí](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/documentacion/crearAzure.md).

2. Conectar a la máquina por SSH: `ssh romi@pluco-db.cloudapp.net`

3. Instalar paquetes necesarios: `sudo apt-get update && sudo apt-get install -y git && sudo apt-get install -y build-essential`

4. Clonar el repositorio de la aplicación: `sudo git clone https://github.com/romilgildo/IV-PLUCO-RMH.git`

5. Entrar en el directorio y preparar el contenedor: `cd IV-PLUCO-RMH && make docker`

Contenedor creado en Azure:

![Pluco funcionando en Azure](http://i628.photobucket.com/albums/uu6/romilgildo/dockerenAzure_zpsszr0hu3b.png)

Puertos abiertos en Azure:

![Puertos abiertos en Azure](http://i628.photobucket.com/albums/uu6/romilgildo/puertosAbiertosAzure_zpswdzdpte8.png)

Una vez arrancado el contenedor y estemos dentro, ya solo falta entrar al directorio de la app y arrancar el servidor. 

 `cd IV-PLUCO-RMH && make run`

Aquí tenemos desplegado el contenedor Docker instalado en una máquina de Azure y disponible de manera online: [http://pluco-db.cloudapp.net:8000/](http://pluco-db.cloudapp.net:8000/)
