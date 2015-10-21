#PLATAFORMA UNIVERSITARIA DE COMPARTICIÓN DE CONOCIMIENTOS: PLUCO

Autor: Rubén Martín Hidalgo

[Apuntado en el proyecto de software libre de la oficina OSL](http://osl.ugr.es/bases-de-los-premios-a-proyectos-libres-de-la-ugr/)

## Práctica 1

###Introducción

Se trata de una plataforma académica de compartición de archivos de la Universidad de Granada, que permite la colaboración en grupo entre los usuarios del sistema. Ofrece servicios de almacenamiento de archivos en la nube, y de mensajería y foros para la resolución de dudas, potenciando la interacción de los usuarios, y agrupando a los mismos por grupos, por ejemplo de asignaturas o cursos.

###Seguridad

En cuanto a la seguridad de nuestra plataforma los objetivos son: Permitir tener un sistema seguro en el que se separen datos sensibles y credenciales de los usuarios, y por otra parte archivos de los mismos. Además tendremos una web con foros que si es atacada no compremete la privacidad de los usuarios ni sus archivos.

###Infraestuctura

En mi infraestructura, realizaré un despliegue sobre Azure de un sistema de organización y gestión de datos de los usuarios de la plataforma, y que permitirá recuperar la información de los usuarios, consultar sus datos asociados, modificar los datos, además de los procesos asociados a dar de alta o baja a los usuarios. 

Irá instalado sobre una máquina virtual que actúa como servidor, y que tendrá acceso a la información almacenada mediante una página web, cuyo servidor web podría estar alojado en un servidor distinto al de la base de datos, con el objetivo de repartir la carga y dar mayor seguridad a la infraestructura. 

La base de datos usada será MySQL y que deberá contener información sobre las asignaturas matriculadas e información personal de los usuarios. 

Como lenguaje de programación se usará Python. Además utilizaremos Django como framework para agilizar el desarrollo web.  

El resto de mis compañeros deberán crear: 

1. Un sistema web/red social de foros y dudas similar a Stackoverflow. Tendría detrás un servidor web para alojar las páginas y otro servidor para la base de datos de los usuarios.

2. Un sistema de almacenamiento sftp de recursos en la nube, que se usará para la organización, administración y compartición de archivos. Todo esto irá implementado en otro servidor que usaremos de Cloud Storage, además de un sistema de acceso a los datos y recursos por parte de los usuarios.

Al final del proyecto, deberemos enlazar en conjunto las tres partes del proyecto, y realizar el despliegue correcto sobre cualquier infraestructura virtual.

## Práctica 2 [![Travis](https://secure.travis-ci.org/romilgildo/IV-PLUCO-RMH.png)](http://travis-ci.org/romilgildo/IV-PLUCO-RMH)

Para la realización de tests que permitan comprobar que el código creado funciona correctamente, he usado para mi código escrito en Python, el sistema de pruebas [Nose](https://nose.readthedocs.org/en/latest/), que está basado en funciones de [Unittest](https://docs.python.org/2/library/unittest.html). Existen otras alternativas para Python como pueden ser [Tox](https://testrun.org/tox/latest/) y [Pytest](http://pytest.org/latest/), pero he escogido Nose por ser el más conocido.

El código que he creado por ahora, pero que podrá ir creciendo conforme vaya avanzando el proyecto es este:

```
from models import Estudiante
from models import Profesor
from models import Asignatura
from nose.tools import assert_equal

# Create your tests here.

class Test:
	def calcularCuadrado(self, numero):
		return numero*numero
		
	def testCuadrado(self):
		cuadrado = Test()
		response = cuadrado.calcularCuadrado(4)
		assert_equal(response, 16)

	def testCrearEstudiante(self):
		usuario = Estudiante('nuevoE')
		response = usuario.nombre
		assert_equal(response, 'nuevoE') 
		
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

El siguiente paso es elegir un sistema de integración contínua de modo que cada cambio realizado en el repositorio, implique una ejecución de los tests anteriores comprobando y asegurandonos de que el programa sigue funcionando.

En mi caso, estoy haciendo la integración contínua con [Shippable](https://www.shippable.com/) ya que me pareció muy sencillo su manejo, pero existen otros sistemas iguales de buenos como [Travis](https://travis-ci.org/) o [Jenkins](https://jenkins-ci.org/). 

Para que nuestro sistema de CI funcione, debemos crear primero el fichero en formato YML correspondiente dentro del repositorio, que en mi caso sería este:

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
  
before_script:
  - export DJANGO_SETTINGS_MODULE=pluco.settings
  
# Ejecucion de pruebas
script:
 - nosetests
 ```
 
 El fichero shippable.yml actualizado se encuentra [aquí](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/shippable.yml).
 
 Aquí tenemos una captura de como está funcionando correctamente la integración contínua:
 
 ![Integracion Continua Shippable](https://www.dropbox.com/s/s02yu9vycleuogg/ShippableCI.PNG?dl=1)
 
 
