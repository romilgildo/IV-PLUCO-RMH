## Despliegue remoto: [Fabric](http://www.fabfile.org/)

Fabric es un biblioteca de Python que se usa para automatizar tareas de administración o despliegues de aplicaciones a través de SSH.

Se puede instalar con `sudo apt-get install fabric`.

En nuestro caso, vamos a realizar el despliegue en nuestra máquina virtual de Azure que creamos anteriormente [aquí](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/documentacion/crearAzure.md).

Pero antes de crear el contenedor, nos vamos a asegurar de que tenemos el puerto que usamos para la app abierto en Azure. Para ello ejecutamos:

 `azure vm endpoint create <nombre-MV> 8000 8000`
 
Donde pone <nombre-MV> ponemos el de nuestra máquina, que si no estamos seguro de como se llamaba podemos mirarlo con `azure vm list` que nos muestra las máquinas virtuales creadas.

![Abrir puerto para nuestra app](https://www.dropbox.com/s/i74lfgesu7m4l1k/abrirpuertosAzurePluco.PNG?dl=1)

En mi caso me dice que ya existe el puerto porque lo cree anteriormente.

### El rey del mambo: nuestro Fabfile

Mediante un fichero llamado [fabfile.py](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/fabfile.py), se describen las distintas tareas de administración y despliegue que se quieran realizar de manera remota.

Este es el contenido de dicho fichero:

```
from fabric.api import run, local, hosts, cd
from fabric.contrib import django

#Muestra infomacion del host
def informacion():
    run('uname -a')

#Descarga la aplicacion del repositorio git
def descargar():
	run('sudo apt-get update')
	run('sudo apt-get install -y git')
	run('sudo git clone https://github.com/romilgildo/IV-PLUCO-RMH.git')

#Instalacion con las dependencias necesarias
def instalar():
	run('cd IV-PLUCO-RMH && make install')

#Sincronizacion de la aplicacion
def actualizar():
	run('cd IV-PLUCO-RMH && git pull')

#Ejecucion de test
def test():
	run('cd IV-PLUCO-RMH && make test')

#Ejecucion de la aplicacion
def ejecutar():
	run('cd IV-PLUCO-RMH && make run')

#Ejecucion remota del docker
#Instalacion de docker, descarga de la imagen y ejecucion
def montar_docker():
	run('sudo apt-get update')
	run('sudo apt-get install -y docker.io')
	run('sudo docker pull romilgildo/pluco')
	run('sudo docker run -p 8000:8000 -t -i romilgildo/pluco /bin/bash')
```

Los siguientes comandos con Fabric, siempre se ejecutan desde nuestra máquina anfitriona.

Para ver que funciona vamos a empezar usando uno de los comandos que hemos metido en el fabfile:

 `fab -p mipassword -H romi@pluco-db.cloudapp.net informacion`

Con dicho comando le estamos diciendo que conecte por ssh a nuestra maquina de Azure metida tras la opción -H, con la password tras la opción -p, y que ejecute la función informacion del fabfile. Nos debería mostrar algo como esto:

![Mostrar infomracion del host](https://www.dropbox.com/s/19e38anvtx6v7dq/infoHost.PNG?dl=1)

Ahora procedemos a realizar el despliegue:

 `fab -p mipassword -H romi@pluco-db.cloudapp.net montar_docker`
 
Y una vez termine y estemos dentro del contenedor, ya solo falta entrar al directorio de la app y arrancar el servidor. 

 `cd IV-PLUCO-RMH && make run`
 
![Arrancar servidor python](https://www.dropbox.com/s/stj4lrn6fmw5lpf/ejecutarappDocker.PNG?dl=1)

[Aquí](http://pluco-db.cloudapp.net:8000/) podemos ver el contenedor Docker funcionando de modo online.
