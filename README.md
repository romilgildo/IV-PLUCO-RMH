#PLATAFORMA UNIVERSITARIA DE COMPARTICIÓN DE CONOCIMIENTOS: PLUCO

Autor: Rubén Martín Hidalgo

[![Travis](https://secure.travis-ci.org/romilgildo/IV-PLUCO-RMH.png)](http://travis-ci.org/romilgildo/IV-PLUCO-RMH) [![Shippable](https://img.shields.io/shippable/561d708d1895ca44741d9f63.svg)](https://app.shippable.com/projects/561d708d1895ca44741d9f63)

[![Heroku](https://www.herokucdn.com/deploy/button.png)](http://pluco-db.herokuapp.com/)

[Apuntado en el proyecto de software libre de la oficina OSL](http://osl.ugr.es/bases-de-los-premios-a-proyectos-libres-de-la-ugr/)

### Introducción

Se trata de una plataforma académica de compartición de archivos de la Universidad de Granada, que permite la colaboración en grupo entre los usuarios del sistema. Ofrece servicios de almacenamiento de archivos en la nube, y de mensajería y foros para la resolución de dudas, potenciando la interacción de los usuarios, y agrupando a los mismos por grupos, por ejemplo de asignaturas o cursos.

### Seguridad

En cuanto a la seguridad de nuestra plataforma los objetivos son: Permitir tener un sistema seguro en el que se separen datos sensibles y credenciales de los usuarios, y por otra parte archivos de los mismos. Además tendremos una web con foros que si es atacada no compremete la privacidad de los usuarios ni sus archivos.

### Infraestuctura

En mi infraestructura, realizaré un despliegue sobre Azure de un sistema de organización y gestión de datos de los usuarios de la plataforma, y que permitirá recuperar la información de los usuarios, consultar sus datos asociados, modificar los datos, además de los procesos asociados a dar de alta o baja a los usuarios. 

Irá instalado sobre una máquina virtual que actúa como servidor, y que tendrá acceso a la información almacenada mediante una página web, cuyo servidor web podría estar alojado en un servidor distinto al de la base de datos, con el objetivo de repartir la carga y dar mayor seguridad a la infraestructura. 

La base de datos usada será MySQL y que deberá contener información sobre las asignaturas matriculadas e información personal de los usuarios. 

Como lenguaje de programación se usará Python. Además utilizaremos Django como framework para agilizar el desarrollo web.  

El resto de mis compañeros deberán crear: 

1. Un sistema web/red social de foros y dudas similar a Stackoverflow. Tendría detrás un servidor web para alojar las páginas y otro servidor para la base de datos de los usuarios.

2. Un sistema de almacenamiento sftp de recursos en la nube, que se usará para la organización, administración y compartición de archivos. Todo esto irá implementado en otro servidor que usaremos de Cloud Storage, además de un sistema de acceso a los datos y recursos por parte de los usuarios.

Al final del proyecto, deberemos enlazar en conjunto las tres partes del proyecto, y realizar el despliegue correcto sobre cualquier infraestructura virtual.

### Instalación de MySQL en Azure

Para poder tener disponible desde cualquier lugar nuestra base de datos, he decidido instalar y configurar la app con MySQL en una máquina virtual independiente dentro de Azure. Para ello he seguido los siguientes pasos:

1. Crear una máquina virtual, y abrir puertos para http, ssh y mysql dentro de Azure.

2. Conectar por ssh a la máquina de azure con: *ssh romi@pluco-db.cloudapp.net*  

3. Instsalar MySQL con: *sudo apt-get install mysql-server mysql-client* 

4. Editamos fichero *settings.py* de nuestra app para que conecte con la base de datos: 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql',
        'USER': 'root',
        'PASSWORD': '****',
        'HOST': 'pluco-db.cloudapp.net',
        'PORT': '3306',
    }
}
```

5. Modificamos la "bind address" a 0.0.0.0 dentro de */etc/mysql/my.cnf*

6. Añadimos la linea "mysqld: all" al fichero */etc/hosts.allow* para permitir entrada desde cualquier ordenador

7. Reiniciamos MySQL con: *sudo /etc/init.d/mysql restart*

8. Comprobamos que tenemos acceso con: *mysql -h pluco-db.cloudapp.net -u root -p*

### Instalación local de la app

Para ejecutar la aplicación en nuestro propio ordenador, ejecutamos los siguientes comandos:

```
$ git clone https://github.com/romilgildo/IV-PLUCO-RMH.git
$ cd IV-PLUCO-RMH/
$ make install
$ make run
```

### Sistema de pruebas: [Nose](https://nose.readthedocs.org/en/latest/)

Para la realización de tests que permitan comprobar que el código creado funciona correctamente, he usado para mi código escrito en Python, el sistema de pruebas Nose, que está basado en funciones de [Unittest](https://docs.python.org/2/library/unittest.html). Existen otras alternativas para Python como pueden ser [Tox](https://testrun.org/tox/latest/) y [Pytest](http://pytest.org/latest/), pero he escogido Nose por ser el más conocido.

El código que he creado por ahora, pero que podrá ir creciendo conforme vaya avanzando el proyecto es este:

```
from models import Estudiante
from models import Profesor
from models import Asignatura
from nose.tools import assert_equal

# Create your tests here.

class Test:
	def testCrearEstudiante(self):
		usuario = Estudiante(nombre='nuevoE', dni='12345678A')
		assert_equal(usuario.nombre, 'nuevoE')
		assert_equal(usuario.dni, '12345678A')
		
	def testCrearProfesor(self):
		usuario = Profesor('nuevoP')
		response = usuario.nombre
		assert_equal(response, 'nuevoP') 
		
	def testCrearAsignatura(self):
		asig = Asignatura('nuevaA')
		response = asig.nombre
		assert_equal(response, 'nuevaA') 
```

El archivo actualizado está [aquí](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/plucoapp/tests.py), dentro del repositorio.

Para ejecutar los tests localmente, hacer *make test*.

Aquí vemos como la aplicación pasa el test de prueba:

![Ejecucion Nosetest](https://www.dropbox.com/s/uaqyie3raze79ib/nosetest.png?dl=1)

### Herramienta de construcción

He creado un Makefile con las opciones de limpieza, realización de tests y ejecución del servidor. El contenido del archivo es el siguiente:

```
clean:
	rm -rf *~* && find . -name '*.pyc' -exec rm {} \;

test: 
	export DJANGO_SETTINGS_MODULE=plucoapp.settings && nosetests
	
run:
	python manage.py runserver 0.0.0.0:8000

```

Y [este](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/Makefile) el archivo actualizado en el repositorio.

Para ejecutar la herramienta de construcción, simplemente debemos escribir en la terminal el comando *make* seguido de la opción que queramos (clean, test, run...).

El siguiente paso es elegir un sistema de integración contínua de modo que cada cambio realizado en el repositorio, implique una ejecución de los tests anteriores comprobando y asegurandonos de que el programa sigue funcionando.

En mi caso, estoy haciendo la integración contínua con Shippable y Travis, ya que me parecieron muy sencillo su manejo y muy completos, aunque también se podrían usar otros sistemas iguales de buenos como puede ser [Jenkins](https://jenkins-ci.org/). 

### Integración contínua: [Shippable](https://www.shippable.com/)

Para que nuestro sistema de CI funcione, debemos crear primero el fichero en formato YML correspondiente dentro del repositorio, llamado "shippable.yml" y que en mi caso sería este:

```
# Distribucion de desarrollo
build_environment: Ubuntu 14.04

# Lenguaje de programacion
language: python

# Version Python
python:
  - "2.7"

# Provisionamiento de la maquina
install:  
  - sudo apt-get install libmysqlclient-dev
  - sudo apt-get install python-dev
  - pip install MySQL-python
  - pip install Django 
  - pip install nose
  
# Ejecucion de pruebas
script:
 - make test
```
 
El fichero shippable.yml actualizado se encuentra [aquí](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/shippable.yml).
 
Aquí tenemos una captura de como está funcionando correctamente la integración contínua:
 
![Integracion Continua Shippable](https://www.dropbox.com/s/s02yu9vycleuogg/ShippableCI.PNG?dl=1)

### Integración contínua: [Travis](https://travis-ci.org/)

Con este sistema hacemos lo mismo que con el anterior, crear el fichero YML que en este caso se llamará ".travis.yml", con el siguiente contenido:

```
# Selección del lenguaje, en nuestro caso python. 
language: python   

python:
  - "2.7" 

install:   # Instalación de dependencias
  - sudo apt-get install libmysqlclient-dev
  - sudo apt-get install python-dev
  - pip install --upgrade pip
  - pip install MySQL-python
  - pip install Django 
  - pip install nose  

script:       # El script que ejecutaremos para que nuestro código funcione y corra los test.
  - make test

branches:     # decidimos que TravisCI solo compruebe los test del master de github.
  - only:
    - master

notifications:   # Notificamos los resultados de los test por correo
  recipients:
    - rubenmartin1991@gmail.com
  email:
    on_success: change
    on_failure: always

```

[Aquí](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/.travis.yml) teneis el fichero actualizado.

Y por último una captura con la última modificación hecha al código del repositorio y que hizo pasar los test en Travis:

![Integracion Continua Travis](https://www.dropbox.com/s/gtt7w9vrilja1wr/TravisCI.PNG?dl=1)

### Despliegue en un PaaS: [Heroku](https://www.heroku.com/)

Nos decantamos por Heroku, debido a que funciona realmente bien y es bastante sencillo de hacer que nuestra aplicación funcione desde primera hora. Se deben añadir los siguientes archivos:

Procfile:

```
web: gunicorn plucoapp.wsgi --log-file -
```

requirements.txt:

```
MySQL-python==1.2.3
Django==1.8.5
nose==1.3.7
gunicorn==19.3.0
```

Y tras habernos registrado en Heroku, ejecutamos *make deploy* dentro de nuestra app, que hace lo siguiente:

```
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh   
heroku login
heroku create
git add .
git commit -m "despliegue en heroku"
git push heroku master
heroku ps:scale web=1
heroku open
``` 

Esta es la aplicación ya desplegada en Heroku: [https://pluco-db.herokuapp.com/](https://pluco-db.herokuapp.com/)

Ahora añadimos un proceso de integración contínua junto al despliegue automático mediante [Snap CI](https://snap-ci.com/).

Realizamos la siguiente configuración desde la interfaz web:

![Configuracion Snap 1](https://www.dropbox.com/s/r9amrlau1zoapyp/herokupluco1.PNG?dl=1)

![Configuracion Snap 2](https://www.dropbox.com/s/3hm99md20w60boj/herokupluco2.PNG?dl=1)

![Configuracion Snap 3](https://www.dropbox.com/s/c9y6eri9b9585bg/herokupluco3.PNG?dl=1)

Y ya tenemos la integración contínua que despliega la aplicación al hacer git push a nuestro repositorio de GitHub, siempre que esta pase los tests.

![Snap CI funcionando](https://www.dropbox.com/s/p7pibp4axd9x6p8/herokuplucoFunciona.PNG?dl=1)
