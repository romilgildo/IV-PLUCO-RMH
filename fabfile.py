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
	sudo apt-get update   # actualizamos repositorios
	sudo apt-get install -y apache2   # instalar apache
	sudo apt-get install -y mysql-server mysql-client   # instalar mysql
	sudo apt-get install -y libapache2-mod-php5 php5 php5-mcrypt   # instalamos php
	sudo php5enmod mcrypt
	sudo service apache2 restart   # reiniciar apache
	sudo apt-get -y install phpmyadmin   # instalar phpmyadmin
	cp my.cnf /etc/mysql/my.cnf
	echo "mysqld: all" >> /etc/hosts.allow
	sudo /etc/init.d/mysql restart
	
