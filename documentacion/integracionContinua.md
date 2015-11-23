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
  - sudo apt-get install libmysqlclient-dev
  - sudo apt-get install python-dev
  - pip install MySQL-python
  - pip install Django 
  - pip install nose
  
# Ejecucion de pruebas
script:
 - make test
```
 
Aquí tenemos una captura de como está funcionando correctamente la integración contínua:
 
![Integracion Continua Shippable](http://i628.photobucket.com/albums/uu6/romilgildo/ShippableCI_zpsa4v35zyr.png)

## Integración contínua con Travis

Con este sistema hacemos lo mismo que con el anterior, crear el fichero YML que en este caso se llamará [.travis.yml](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/.travis.yml), con el siguiente contenido:

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

Y por último una captura con la última modificación hecha al código del repositorio y que hizo pasar los test en Travis:

![Integracion Continua Travis](http://i628.photobucket.com/albums/uu6/romilgildo/TravisCI_zpsrnjbk0vt.png)
