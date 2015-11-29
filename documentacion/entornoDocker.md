## Entorno de pruebas: [Docker](https://www.docker.com/)

Para crear la imagen, Docker usa un fichero dentro del código de la aplicación llamado [Dockerfile](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/Dockerfile) para la construcción de la imagen, que en mi caso contiene lo siguiente:

```
FROM ubuntu:14.04
MAINTAINER Ruben Martin Hidalgo <rubenmartin1991@gmail.com>

RUN sudo apt-get update
RUN sudo apt-get install -y git
RUN sudo apt-get install -y build-essential
RUN sudo git clone https://github.com/romilgildo/IV-PLUCO-RMH.git
RUN cd IV-PLUCO-RMH && git pull
RUN cd IV-PLUCO-RMH && make install
```

Luego en la web de [Docker Hub](https://hub.docker.com/), creamos un "Automated Build" sobre el repositorio de nuestro proyecto, lo cual comenzará a crear la imagen. 

[Esta](https://hub.docker.com/r/romilgildo/pluco/) es la imagen Docker y aquí teneis una captura de la construcción automática de la imagen funcionando:

![Automated Build Docker](http://i628.photobucket.com/albums/uu6/romilgildo/dockerFuncionando_zpsulkp8xbi.png)

A partir de ahora, todos los cambios realizados cobre el código del repositorio, se integran en tiempo real y de manera totalmente automatizada mediante Docker Hub, que rehará el build por su cuenta cada vez que hagamos "git push".

Para crear el entorno de pruebas en nuestro ordenador, se debe ejecutar el comando:

`make docker`

Esto hará lo siguiente: 

```
$ sudo apt-get update
$ sudo apt-get install -y docker.io
$ sudo docker pull romilgildo/pluco
$ sudo docker run -t -i romilgildo/pluco /bin/bash
```

Es decir, instala Docker, crea el contenedor con la aplicación instalada en él, y arranca el entorno de pruebas. Dentro de este bastará con hacer `make run` en el directorio de la aplicación para ejecutar nuestra app como si estuviera localmente y así poder probar su correcto funcionamiento.

Aquí una muestra del funcionamiento de nuestra app dentro del contenedor, donde accedemos introduciendo la IP del contenedor Docker en el navegador del sistema anfitrión:

![Pluco funcionando en Docker](http://i628.photobucket.com/albums/uu6/romilgildo/plucoenDocker_zps32fcyw8u.png)
