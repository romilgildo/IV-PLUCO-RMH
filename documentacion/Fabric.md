## Despliegue remoto con Fabric

[Fabric](http://www.fabfile.org/) es un biblioteca de Python que se usa para automatizar tareas de administración o despliegues de aplicaciones a través de SSH.

Se puede instalar con `sudo apt-get install fabric`.

Mediante un fichero llamado [fabfile.py](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/fabfile.py), se describen las distintas tareas de administración y despliegue que se quieran realizar de manera remota.

Este es el contenido de mi fichero:

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
	run('cd IV-PLUCO-RMH && sudo git pull')

#Ejecucion de test
def test():
	run('cd IV-PLUCO-RMH && make test')

#Ejecucion de la aplicacion
def ejecutar():
	run('cd IV-PLUCO-RMH && make run')

#Instalacion de docker, descarga de la imagen y ejecucion
def montar_docker():
	run('sudo apt-get update')
	run('sudo apt-get install -y docker.io')
	run('sudo docker pull romilgildo/pluco')
	run('sudo docker run -p 8000:8000 -t -i romilgildo/pluco sh -c "cd IV-PLUCO-RMH && make run"')
```

Los siguientes comandos con Fabric, siempre se ejecutan desde nuestra máquina anfitriona.

Para ver que funciona vamos a empezar usando uno de los comandos que hemos metido en el fabfile:

 `fab -p mipassword -H romi@pluco-db.cloudapp.net informacion`

Con dicho comando le estamos diciendo que conecte por ssh a nuestra maquina de Azure metida tras la opción -H, con la password tras la opción -p, y que ejecute la función "informacion" del fabfile. Nos debería mostrar algo como esto:

![Mostrar infomracion del host](http://i628.photobucket.com/albums/uu6/romilgildo/infoHost_zpsaxaizyqm.png)

[Volver atrás](https://github.com/romilgildo/IV-PLUCO-RMH#administración-remota-con-fabric)
