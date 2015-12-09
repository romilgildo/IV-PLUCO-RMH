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

# Creación del entorno de pruebas en local

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

Aquí una muestra del funcionamiento de nuestra app dentro del contenedor local, donde accedemos introduciendo la IP del contenedor Docker en el navegador del sistema anfitrión:

![Pluco funcionando en Docker](http://i628.photobucket.com/albums/uu6/romilgildo/plucoenDocker_zps32fcyw8u.png)

# Creación del entorno de pruebas en Azure

Para la instalación en una máquina virtual de Azure, basta con crearla, por ejemplo desde el panel de control web (o mediante línea de comandos con la orden `azure  vm  create` que veremos más adelante) y luego conectar a ella por ssh, clonar el repositorio, y hacer `make docker` dentro del directorio de la app. También necesitamos abrir el puerto que usa el servidor de Python y el de Docker. Todo este proceso se automatizará en los próximos hitos, con scripts de automatización y provisionamiento de la máquina virtual. 

Contenedor creado en Azure:

![Pluco funcionando en Azure](http://i628.photobucket.com/albums/uu6/romilgildo/dockerenAzure_zpsszr0hu3b.png)

Puertos abiertos en Azure:

![Puertos abiertos en Azure](http://i628.photobucket.com/albums/uu6/romilgildo/puertosAbiertosAzure_zpscbqlzbb2.png)

He necesitado crear unos certificados para poder hacer uso de la extensión VM Docker de Azure, y así poder tener acceso a él desde internet.

Creo una carpeta local .docker y dentro de ella ejecutamos:

```
sudo rm ~/.rnd
openssl genrsa -aes256 -out ca-key.pem 4096
openssl req -new -x509 -days 365 -key ca-key.pem -sha256 -out ca.pem
openssl genrsa -out server-key.pem 4096
openssl req -subj "/CN=pluco-db.cloudapp.net" -sha256 -new -key server-key.pem -out server.csr
echo subjectAltName = IP:10.10.10.20,IP:127.0.0.1 > extfile.cnf
openssl x509 -req -days 365 -sha256 -in server.csr -CA ca.pem -CAkey ca-key.pem -CAcreateserial -out server-cert.pem -extfile extfile.cnf
openssl genrsa -out key.pem 4096
openssl req -subj '/CN=client' -new -key key.pem -out client.csr
echo extendedKeyUsage = clientAuth > extfile.cnf
openssl x509 -req -days 365 -sha256 -in client.csr -CA ca.pem -CAkey ca-key.pem -CAcreateserial -out cert.pem -extfile extfile.cnf
rm -v client.csr server.csr
base64 ca.pem > ca64.pem
base64 server-cert.pem > server-cert64.pem
base64 server-key.pem > server-key64.pem
```

Luego desde el portal de Azure, creamos la extensión de Docker como se puede ver en la imagen:

![Añadir extensión VM Docker](http://i628.photobucket.com/albums/uu6/romilgildo/antildeadirExtensionDocker_zps31gzpwsc.png)

Reiniciamos el demonio de Docker 

```
sudo rm /var/run/docker.pid
sudo docker -d &
```

Y ya vemos que la extensión de Docker en Azure funciona.

![Extensión creada](http://i628.photobucket.com/albums/uu6/romilgildo/extensionFunciona_zpshvazhnsn.png)

Comprobamos también que haya conexión con el contenedor Docker instalado en Azure con `docker --tls -H tcp://pluco-db.cloudapp.net:2376 info`

![Conexión correcta con el contendor](http://i628.photobucket.com/albums/uu6/romilgildo/conexionDockerAzure_zpsophi8bna.png)

Por último, para poder conectar a nuestra aplicación funcionando desde el contenedor Docker creado, solo debemos arrancar el contenedor de la siguiente forma:

`sudo docker run -p 8000:8000 -t -i romilgildo/pluco /bin/bash`

Donde le indicamos que el puerto 8000 del contenedor corresponderá al 8000 de la máquina virtual, de forma que podamos tener acceso a él. 

Ya solo entramos al directorio de la app y arrancamos el servidor. 

`cd IV-PLUCO-RMH && make run`

Aquí tenemos desplegado el contenedor Docker instalado en una máquina de Azure y disponible de manera online: [http://pluco-db.cloudapp.net:8000/](http://pluco-db.cloudapp.net:8000/)
