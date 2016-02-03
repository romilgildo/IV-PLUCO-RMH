# PLATAFORMA UNIVERSITARIA DE COMPARTICIÓN DE CONOCIMIENTOS: PLUCO

Autor: Rubén Martín Hidalgo

[![Travis](https://secure.travis-ci.org/romilgildo/IV-PLUCO-RMH.png)](http://travis-ci.org/romilgildo/IV-PLUCO-RMH) 
[<img src="https://api.shippable.com/projects/561d708d1895ca44741d9f63/badge/master" alt="Shippable" height=20>](https://app.shippable.com/projects/561d708d1895ca44741d9f63)
[![Snap CI](https://snap-ci.com/romilgildo/IV-PLUCO-RMH/branch/master/build_image)](https://snap-ci.com/romilgildo/IV-PLUCO-RMH/branch/master)

[![Heroku](https://www.herokucdn.com/deploy/button.png)](http://pluco-db.herokuapp.com/) 
[<img src="http://azuredeploy.net/deploybutton.png" alt="Azure" height=32>](http://pluco-iv.cloudapp.net/) 
[<img src="http://i628.photobucket.com/albums/uu6/romilgildo/dockericon_zpswj3ifwrw.png" alt="Docker" height=32>](https://hub.docker.com/r/romilgildo/pluco/)

[Apuntado en el proyecto de software libre de la oficina OSL](http://osl.ugr.es/bases-de-los-premios-a-proyectos-libres-de-la-ugr/)

## Introducción

Se trata de una plataforma académica de compartición de archivos de la Universidad de Granada, que permite la colaboración en grupo entre los usuarios del sistema. Ofrece servicios de almacenamiento de archivos en la nube, y de mensajería y foros para la resolución de dudas, potenciando la interacción de los usuarios, y agrupando a los mismos por grupos, por ejemplo de asignaturas o cursos.

## Seguridad

En cuanto a la seguridad de nuestra plataforma los objetivos son: Permitir tener un sistema seguro en el que se separen datos sensibles y credenciales de los usuarios, y por otra parte archivos de los mismos. Además tendremos una web con foros que si es atacada no compremete la privacidad de los usuarios ni sus archivos.

## Infraestuctura

En mi infraestructura, se realiza un despliegue sobre **Azure** de un sistema de organización y gestión de datos de los usuarios de la plataforma, permitiendo recuperar la información de los usuarios, consultar sus datos asociados, modificar los datos, además de los procesos asociados a dar de alta o baja a los usuarios. 

Va instalado sobre una máquina virtual que actúa como servidor, disponiendo de acceso a la información almacenada mediante una página web, cuyo servidor web está alojado en un servidor distinto al de la base de datos, con el objetivo de repartir la carga y dar mayor seguridad a la infraestructura. 

La base de datos usada es **MySQL** y contiene información sobre las asignaturas matriculadas e información personal de los usuarios. 

Como lenguaje de programación se usa **Python**. Además utilizamos **Django** como framework para agilizar el desarrollo web.  

El resto de mis compañeros han creado: 

1. Un [sistema web/red social](https://github.com/rafaellg8/IV-PLUCO-RLG) de foros y dudas similar a Stackoverflow. Lleva detrás un servidor web para alojar las páginas y otro servidor para la base de datos de los usuarios.

2. Un sistema de almacenamiento sftp de recursos en la nube, que se usará para la organización, administración y compartición de archivos. Todo esto irá implementado en otro servidor que usaremos de Cloud Storage, además de un sistema de acceso a los datos y recursos por parte de los usuarios.

Al final del proyecto, deberemos enlazar en conjunto las tres partes del proyecto, y realizar el despliegue correcto sobre cualquier infraestructura virtual.

## Herramienta de construcción con Make

Para la construcción automática de la app, he usado [Make](https://www.gnu.org/software/make/). Para su funcionamiento, he creado un [Makefile](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/Makefile) con las distintas opciones.

Para ejecutar la herramienta de construcción, simplemente debemos escribir en la terminal el comando **make** seguido de la opción que queramos ejecutar (clean, test, run...).

[Más información](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/documentacion/construccionApp.md)

## Integración contínua

La integración contínua consiste en hacer integraciones automáticas de un proyecto lo más a menudo posible para así poder detectar fallos cuanto antes. Este proceso conlleva la compilación y ejecución de pruebas del proyecto.

### Realización de tests con Nose

Para la realización de tests que permitan comprobar que el código creado funciona correctamente, he usado para mi código escrito en Python, el sistema de pruebas [Nose](https://nose.readthedocs.org/en/latest/), que está basado en funciones de [Unittest](https://docs.python.org/2/library/unittest.html). Existen otras alternativas para Python como pueden ser [Tox](https://testrun.org/tox/latest/) y [Pytest](http://pytest.org/latest/), pero he escogido Nose por ser el más conocido.

Aquí está el archivo [tests.py](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/plucoapp/tests.py) actualizado con los tests correspondientes para manejar los modelos de la app.

Para ejecutar los tests localmente, hacer `make test`.

Aquí vemos como la aplicación pasa el test de pruebas inicial:

![Ejecucion Nosetest](http://i628.photobucket.com/albums/uu6/romilgildo/nosetest_zpsa0tx2byz.png)

### Herramientas de integración contínua

El siguiente paso es elegir un sistema de integración contínua de modo que cada cambio realizado en el repositorio, implique una ejecución de los tests anteriores comprobando y asegurandonos de que el programa sigue funcionando.

En mi caso, estoy haciendo la integración contínua con [Shippable](https://www.shippable.com/), [Travis](https://travis-ci.org/) y [Snap-CI](https://snap-ci.com/)

[Más información](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/documentacion/integracionContinua.md)

## Descarga de la app

Para realizar cualquiera de las funcionalidades que vienen en esta documentación, necesitaremos antes descargar antes la aplicación en nuestro ordenador, y a partir de ahí podremos realizar tests, desplegar la app o simplemente arrancarla localmente. 

Para ello ejecutamos los siguientes comandos:

```
$ sudo apt-get install git
$ sudo apt-get install make
$ git clone https://github.com/romilgildo/IV-PLUCO-RMH.git
$ cd IV-PLUCO-RMH/
``` 

## Instalación local de la app

Para ejecutar la aplicación en nuestro propio ordenador, ejecutamos los siguientes comandos:

```
$ make install
$ make run
```

Si todo ha ido bien, ya podremos acceder a nuestra app introduciendo `localhost:8000` en nuestro navegador web.

## Despliegue de la app

Si queremos realizar el despliegue en Azure y poner en marcha toda la app en la web de manera totalemente automatizada, basta con ejecutar lo siguiente:

 `sudo ./desplegarPLUCO.sh`
 
Dicho script instalará todo lo necesario, crea las bases de datos y despliega la aplicación en Azure con los siguientes comandos:

```
make install
make mysql
make azure
```
 
### Instalación de MySQL en Azure

Para poder tener disponible desde cualquier lugar nuestra base de datos, he decidido instalar y configurar la app con MySQL en una máquina virtual independiente dentro de Azure. 

Para ello, bastará con ejecutar `make mysql` y automáticamente se crearán las bases de datos en una máquina independiente en Azure.

[Más información](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/documentacion/MySQL.md)

### Entorno de pruebas con Docker

[Docker](https://www.docker.com/) es una plataforma que automatiza el despliegue de aplicaciones dentro de contenedores software, permitiendo probarla en un entorno aislado para posteriormente desplegarla a producción rápidamente.

El repositorio de mi app en Docker se actualiza automáticamente cada vez que hago un 'push' de git. La Automated Build de mi app es [esta](https://hub.docker.com/r/romilgildo/pluco/).

Aquí está funcionando el entorno de pruebas instalado en Azure: [http://pruebas-pluco.cloudapp.net](http://pruebas-pluco.cloudapp.net)

Para crear dicho entorno, se debe ejecutar el siguiente comando en local:

 `make docker`

[Más información](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/documentacion/entornoDocker.md)

### Despliegue en un PaaS: Heroku

Nos decantamos por [Heroku](https://www.heroku.com/), debido a que funciona realmente bien y es bastante sencillo de hacer que nuestra aplicación funcione desde primera hora en ella.

Gracias a Snap-CI, tenemos un proceso de integración contínua en la que se actualiza la aplicación en Heroku cada vez que actualizamos el repositorio en GitHub. 

Esta es la aplicación ya desplegada en Heroku: [https://pluco-db.herokuapp.com/](https://pluco-db.herokuapp.com/)

[Más información](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/documentacion/despliegueHeroku.md)

### Despliegue en un IaaS: Azure

Para el despliegue en un IaaS, he usado Azure. La aplicación se despliega automáticamente con solo ejecutar `make azure` usando Vagrant y Ansible.

Con el comando `make push` podemos actualizar al mismo tiempo los archivos en el repositorio de Git y luego en nuestra máquina de Azure.

Si el crédito de Azure no se ha agotado, tendré la aplicación web totalmente actualizada funcionando en esta dirección: [http://pluco-iv.cloudapp.net/](http://pluco-iv.cloudapp.net/)

[Más información](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/documentacion/despliegueAzure.md)

## Administración remota con Fabric

Si queremos realizar una administración remota del despliegue de manera automática, podemos usar [Fabric](http://www.fabfile.org/). 

[Más información](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/documentacion/Fabric.md)
