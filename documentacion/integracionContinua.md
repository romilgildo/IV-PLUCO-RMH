## Integración contínua con Shippable

Para que nuestro sistema de CI funcione, debemos crear primero el fichero en formato YML correspondiente dentro del repositorio, llamado [shippable.yml](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/shippable.yml) y que en mi caso sería este:

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
  - sudo apt-get update
  - sudo apt-get install libmysqlclient-dev
  - sudo apt-get install python-dev
  - sudo apt-get install python-pip
  - pip install --upgrade pip
  - pip install -r requirements.txt
  
# Ejecucion de pruebas
script:
 - make test
```
 
Aquí tenemos una captura de como está funcionando correctamente la integración contínua:
 
![Integracion Continua Shippable](http://i628.photobucket.com/albums/uu6/romilgildo/ShippableCI2_zpsgdonu1yz.png~original)

## Integración contínua con Travis

Con este sistema hacemos lo mismo que con el anterior, crear el fichero YML que en este caso se llamará [.travis.yml](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/.travis.yml), con el siguiente contenido:

```
# Distribucion de desarrollo
build_environment: Ubuntu 14.04

# Selección del lenguaje, en nuestro caso python. 
language: python   

python:
  - "2.7" 

install:   # Instalación de dependencias
  - sudo apt-get update
  - sudo apt-get install libmysqlclient-dev
  - sudo apt-get install python-dev
  - sudo apt-get install python-pip
  - pip install --upgrade pip
  - pip install -r requirements.txt 

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

Aquí una captura pasando los test en Travis:

![Integracion Continua Travis](http://i628.photobucket.com/albums/uu6/romilgildo/TravisCI2_zpsx92hhjuw.png~original)

## Integración contínua con Snap-CI

Una gran ventaja que nos aporta este sistema, es que cada vez que hagamos "push" en nuestro repositorio, además de ejecutar los respectivos tests, da la opción de desplegar automáticamente a Heroku.

Para configurar la ejecución de tests se debe hacer desde la interfaz web siguiendo los siguientes pasos:

Añadir repositorio:

![Añadir repositorio](http://i628.photobucket.com/albums/uu6/romilgildo/repositoriosSnap_zpsenw20nub.png~original)

Nos vamos a "Configuration" y luego pinchamos en "Edit" donde vamos a configurar el "Build Pipeline".

![Editar Build Pipeline](http://i628.photobucket.com/albums/uu6/romilgildo/herokupluco1_zpsrsskfguf.png~original)

Ahora damos en "Add Stage", elegimos en la columna de la izquierda "Build/Test" > "Python" y editamos las órdenes del test a la derecha:

![Editar test en Snap](http://i628.photobucket.com/albums/uu6/romilgildo/herokupluco2_zpsdmj934ev.png~original)

Finalmente guardamos y ya tenemos nuestra integración con Snap-CI funcionando:

![Snap-CI funcionando](http://i628.photobucket.com/albums/uu6/romilgildo/SnapTests_zpsg8ue4ynt.png~original)

Como podéis ver, yo estoy usando otro paso más en la integración para desplegar en Heroku. Esa configuración la podéis ver [aquí](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/documentacion/despliegueHeroku.md).

[Volver atrás](https://github.com/romilgildo/IV-PLUCO-RMH#herramientas-de-integración-contínua)
