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
	run('sudo docker run -p 8000:8000 -t -i romilgildo/pluco /bin/bash')
	
def crear_mysql():
	run('mysql -u root -p')   # acceder a mysql
	run('CREATE DATABASE plucodb;')
	run('use mysql;')   # usa base de datos concreta
	run('GRANT ALL PRIVILEGES ON *.* TO admin@"%" IDENTIFIED BY 'manager' WITH GRANT OPTION;')  
	run('FLUSH PRIVILEGES;')   # refresca privilegios
	run('quit;')
	run('cd IV-PLUCO-RMH && git pull')
	run('cd IV-PLUCO-RMH && python manage.py migrate')

	
