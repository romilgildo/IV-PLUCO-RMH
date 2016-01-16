## Instalación de MySQL en Azure

Para esta instalación he seguido los siguientes pasos:

Crear una máquina virtual y abrir puertos para http, ssh y mysql dentro de Azure como expliqué [aquí](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/documentacion/crearAzure.md).

![Extremos configurados en Azure](http://i628.photobucket.com/albums/uu6/romilgildo/extremosAzure_zpsefcyvxtm.png)

Conectar por ssh a la máquina de azure que acabamos de crear: `ssh romi@pluco-db.cloudapp.net`

En mi caso voy a instalar phpmyadmin para tener un control más detallado de mi base de datos, pero si queremos usar solamente MySQL, bastaría con hacer `sudo apt-get install mysql-server mysql-client`.

Entonces instalamos los siguientes paquetes:
```
sudo apt-get update   # actualizamos repositorios
sudo apt-get install apache2   # instalar apache
sudo apt-get install mysql-server mysql-client   # instalar mysql
sudo mysql_secure_installation   # asegurar mysql
sudo apt-get install libapache2-mod-php5 php5 php5-mcrypt   # instalamos php
sudo php5enmod mcrypt
sudo service apache2 restart   # reiniciar apache
sudo apt-get install phpmyadmin   # instalar phpmyadmin
```

Modificamos la "bind address" a 0.0.0.0 dentro del fichero */etc/mysql/my.cnf*.

Añadimos la linea "mysqld: all" al fichero */etc/hosts.allow* para permitir entrada desde cualquier ordenador.

Reiniciamos MySQL con: `sudo /etc/init.d/mysql restart`

Para acabar, comprobamos que tenemos acceso con: `mysql -h pluco-db.cloudapp.net -u root -p`

![MySQL funcionando](http://i628.photobucket.com/albums/uu6/romilgildo/0375f97c-a62d-4f35-8ca3-069f0678b9d9_zpspxekpivl.png)

Una vez empecemos a programar con Django, tendremos que editar el fichero [settings.py](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/plucoapp/settings.py) de nuestra app para que conecte con la base de datos: 

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
