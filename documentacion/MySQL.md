## Instalación de MySQL en Azure

Para ello, basta con ejecutar `make mysql` y automáticamente se crearán las bases de datos en una máquina independiente en Azure.

Dicho comando hace lo siguiente:

```
	sudo apt-get install -y virtualbox virtualbox-dkms
	wget https://releases.hashicorp.com/vagrant/1.8.1/vagrant_1.8.1_x86_64.deb
	sudo dpkg -i vagrant_1.8.1_x86_64.deb
	rm vagrant_1.8.1_x86_64.deb
	vagrant plugin install vagrant-azure
	sudo apt-get install -y python-pip
	sudo pip install --upgrade pip
	sudo pip install paramiko PyYAML jinja2 httplib2 ansible
	sudo vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box --force
	cd despliegueMySQL && sudo vagrant up --provider=azure
```

Instala **Virtualbox** para la creación de máquinas virtuales, instala **Vagrant** y su plugin de Azure para la configuración de dicha máquina y luego instala **Ansible** para provisionarla.

En los dos últimos comandos añade la caja de Azure a Vagrant y crea la máquina virtual en Azure provisionándola con MySQL. El fichero [Vagrantfile](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/despliegueMySQL/Vagrantfile) que ejecuta contiene lo siguiente:

```
VAGRANTFILE_API_VERSION = '2'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = 'azure'
  config.vm.network "public_network"
  config.vm.define "localhost" do |l|
	l.vm.hostname = "localhost"
  end
    
  config.vm.provider :azure do |azure|
    azure.mgmt_certificate = File.expand_path('~/azure.pem')
    azure.mgmt_endpoint = 'https://management.core.windows.net'
    azure.subscription_id = 'a5c45913-5302-4f3e-9ac2-77b0c0883196'
    azure.vm_image = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_3-LTS-amd64-server-20151218-en-us-30GB'
    azure.vm_name = 'pluco-db'
    azure.vm_user = 'pluco'
    azure.vm_password = 'PlucoDB1#'
    azure.vm_location = 'Central US' 
    azure.cloud_service_name = 'pluco-db'
    azure.ssh_port = '22'
    azure.tcp_endpoints = '3306:3306'
  end
  
  config.ssh.username = 'pluco' 
  config.ssh.password = 'PlucoDB1#'

  config.vm.provision "ansible" do |ansible|
	ansible.sudo = true
    ansible.playbook = "crearMySQL.yml"
	ansible.verbose = "v"
	ansible.host_key_checking = false 
  end
end
```

Esto creará la máquina usando nuestro certificado. Para usar el vuestro, deberéis añadir vuestra *subscription_id* y la ubicación del certificado en vuestro ordenador, que por defecto la he puesto en el home del usuario con nombre "azure.pem".

Como podéis ver, le damos el nombre a la web con "cloud_service_name" y abrimos el puerto para MySQL con "tcp_endpoints".

En la parte de Ansible, usamos el fichero [crearMySQL.yml](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/despliegueMySQL/crearMySQL.yml) con el siguiente contenido:

```
---
- hosts: localhost
  sudo: yes
  remote_user: pluco
  tasks:
  - name: Actualizar sistema base
    apt: update_cache=yes upgrade=dist 
  - name: Instalar paquetes necesarios
    action: apt pkg={{ item }} state=installed
    with_items:
      - mysql-server
      - git
      - make
  - name: Clonar repositorio desde git
    git: repo=https://github.com/romilgildo/IV-PLUCO-RMH.git dest=IV-PLUCO-RMH clone=yes force=yes
  - name: Configurar fichero my.cnf
    shell: cd IV-PLUCO-RMH/despliegueMySQL && sudo cp my.cnf /etc/mysql/
  - name: Configurar fichero hosts.allow
    shell: cd IV-PLUCO-RMH/despliegueMySQL && sudo cp hosts.allow /etc/
  - name: Matar proceso mysqld
    shell: sudo killall mysqld
  - name: Reiniciar servidor mysql
    shell: sudo /etc/init.d/mysql restart
  - name: Crear usuario admin
    shell: cd IV-PLUCO-RMH/despliegueMySQL && mysql -u root < usuarioMySQL
  - name: Instalar requisitos para la BD
    shell: cd IV-PLUCO-RMH && make install
  - name: Preparar modelos base de datos
    shell: cd IV-PLUCO-RMH && python manage.py makemigrations plucoapp
  - name: Crear tablas base de datos
    shell: cd IV-PLUCO-RMH && python manage.py migrate
```

Esto instala paquetes básicos, descarga el repositorio y modifica los ficheros necesarios para poder conectar a las bases de datos:

- Modifica la "bind address" a 0.0.0.0 dentro del fichero **/etc/mysql/my.cnf**.

- Añade la linea "mysqld: all" al fichero **/etc/hosts.allow** para permitir entrada desde cualquier ordenador.

Reinicia MySQL para que reconozca los cambios.

También crea un usuario "admin" con pass "manager" para poder acceder a MySQL. Estas credenciales las podéis cambiar en el fichero [usuarioMySQL](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/despliegueMySQL/usuarioMySQL)

Por último crea las tablas respecto a los modelos de la aplicación y realiza las migraciones oportunas. 

Podemos comprobar que tenemos acceso a las bases de datos con: `mysql -h pluco-db.cloudapp.net -u admin -p`. Si funciona debe salirnos algo como lo siguiente:

![MySQL funcionando](http://i628.photobucket.com/albums/uu6/romilgildo/0375f97c-a62d-4f35-8ca3-069f0678b9d9_zpspxekpivl.png)

Para que la app conecte con dicha base de datos, el fichero [settings.py](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/plucoapp/settings.py) de nuestra app contiene esta parte: 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql',
        'USER': 'admin',
        'PASSWORD': 'manager',
        'HOST': 'pluco-db.cloudapp.net',
        'PORT': '3306',
    }
}
```

Ahí deberemos meter las credenciales que hayamos puesto en el usuario de MySQL y el host de nuestra máquina creada.

[Volver atrás](https://github.com/romilgildo/IV-PLUCO-RMH#instalación-de-mysql-en-azure)
