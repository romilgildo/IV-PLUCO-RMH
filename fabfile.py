from fabric.api import run, local, hosts, cd
from fabric.contrib import django
import time

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
	run('sudo docker run -p 8000:8000 -t -i romilgildo/pluco /bin/bash')
	
def crear_mysql():
	run('sudo apt-get update') # actualizamos repositorios
	run('sudo apt-get install -y mysql-server mysql-client')   # instalar mysql
	run('sudo apt-get install -y git')
	run('sudo apt-get install -y make')
	run('sudo git clone https://github.com/romilgildo/IV-PLUCO-RMH.git')
	run('cd IV-PLUCO-RMH && make install')
	run('cd IV-PLUCO-RMH/despliegueMySQL && sudo cp my.cnf /etc/mysql/')
	run('cd IV-PLUCO-RMH/despliegueMySQL && sudo cp hosts.allow /etc/')
	run('sudo /etc/init.d/mysql restart')
	run('cd IV-PLUCO-RMH && sudo python manage.py syncdb')
	
