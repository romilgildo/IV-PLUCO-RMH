## Despliegue en un PaaS: [Heroku](https://www.heroku.com/)

Para realizar el despliegue, se deben añadir los siguientes archivos:

[Procfile](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/Procfile):

```
web: gunicorn plucoapp.wsgi --log-file -
```

[requirements.txt](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/requirements.txt):

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

Ahora añadimos un proceso de integración contínua para que cada vez que hagamos "push" a nuestro repositorio, se realice el despliegue automático. Esta configuración se puede hacer desde el mismo Heroku o con [Snap CI](https://snap-ci.com/).

Con HEROKU:

Conectamos la app de Heroku con GitHub con la siguiente configuración:

![Integracion continua Heroku](http://i628.photobucket.com/albums/uu6/romilgildo/appHerokuGithub_zpskissoi5r.png)

Con SNAP CI:

Realizamos la siguiente configuración desde la interfaz web:

![Configuracion Snap 1](http://i628.photobucket.com/albums/uu6/romilgildo/herokupluco1_zpsypnuxm5w.png)

![Configuracion Snap 2](http://i628.photobucket.com/albums/uu6/romilgildo/herokupluco2_zpsqgme34c8.png)

![Configuracion Snap 3](http://i628.photobucket.com/albums/uu6/romilgildo/herokupluco3_zpsft62am70.png)

Y ya tenemos la integración contínua que despliega la aplicación al hacer git push a nuestro repositorio de GitHub, siempre que esta pase los tests.

![Snap CI funcionando](http://i628.photobucket.com/albums/uu6/romilgildo/herokuplucoFunciona_zpsqldqyeza.png)
