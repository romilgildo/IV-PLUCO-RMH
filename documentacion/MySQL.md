## Instalación de MySQL en Azure

Para esta instalación he seguido los siguientes pasos:

Crear una máquina virtual, y abrir puertos para http, ssh y mysql dentro de Azure.

![Extremos configurados en Azure](http://i628.photobucket.com/albums/uu6/romilgildo/extremosAzure_zpsefcyvxtm.png)

Conectar por ssh a la máquina de azure con: `ssh romi@pluco-db.cloudapp.net`

Una vez dentro de la máquina virtual, instalar MySQL con: `sudo apt-get install mysql-server mysql-client`

Editamos el fichero [settings.py](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/plucoapp/settings.py) de nuestra app para que conecte con la base de datos: 

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

Modificamos la "bind address" a 0.0.0.0 dentro del fichero */etc/mysql/my.cnf*

Añadimos la linea "mysqld: all" al fichero */etc/hosts.allow* para permitir entrada desde cualquier ordenador

Reiniciamos MySQL con: `sudo /etc/init.d/mysql restart`

Para acabar, comprobamos que tenemos acceso con: `mysql -h pluco-db.cloudapp.net -u root -p`

![MySQL funcionando](http://i628.photobucket.com/albums/uu6/romilgildo/0375f97c-a62d-4f35-8ca3-069f0678b9d9_zpspxekpivl.png)
