## Despliegue en Heroku

Para realizar el despliegue, se deben añadir los siguientes archivos:

- [Procfile](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/Procfile):

```
web: gunicorn plucoapp.wsgi --log-file -
```

Este fichero indica a Heroku qué es lo que debe ejecutar. Usamos [gunicorn](http://docs.gunicorn.org/en/stable/run.html) para poder ejecutar la aplicación en Heroku.

- [requirements.txt](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/requirements.txt):

```
MySQL-python==1.2.3
Django==1.8.5
nose==1.3.7
gunicorn==19.3.0
pillow==3.1.0
```

Este fichero instalará aquellos paquetes que necesite la app pero que no estén instalados en Heroku.

Y tras habernos registrado en Heroku, ejecutamos `make heroku`, que hace lo siguiente:

```
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh   # descargar herramienta heroku CLI
heroku login
heroku create
git add .
git commit -m "despliegue en heroku"
git push heroku master
heroku ps:scale web=1
heroku open
``` 

Esto instala el cinturón de herramientas de Heroku, nos loguea, crea la app en Heroku a partir del repositorio de git, y envía el push a la rama de heroku, para finalizar arrancando la aplicación en el servidor web. 

Esta es la aplicación ya desplegada en Heroku: [https://pluco-db.herokuapp.com/](https://pluco-db.herokuapp.com/)

### Integración contínua en Heroku

Ahora vamos a añadir un proceso de integración contínua para que cada vez que hagamos "push" a nuestro repositorio, se realice el despliegue automático en Heroku. Esta configuración se puede hacer desde el mismo Heroku o con Snap CI.

**Con HEROKU:**

Conectamos la app con GitHub desde la propia web de Heroku con la siguiente configuración:

![Integracion continua Heroku](http://i628.photobucket.com/albums/uu6/romilgildo/appHerokuGithub_zpskissoi5r.png~original)

**Con SNAP CI:**

Realizamos la siguiente configuración desde la interfaz web de Snap CI:

![Configuracion Snap 3](http://i628.photobucket.com/albums/uu6/romilgildo/herokupluco3_zpsft62am70.png~original)

Y ya tenemos la integración contínua que actualiza la aplicación en Heroku al hacer git push a nuestro repositorio de GitHub, siempre que esta pase los tests.

[Volver atrás](https://github.com/romilgildo/IV-PLUCO-RMH#despliegue-en-un-paas-heroku)
