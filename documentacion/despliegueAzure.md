## Despliegue en un IaaS: Azure

Para realizar el despliegue en una máquina de Azure, voy a usar [Vagrant](https://www.vagrantup.com/) para la creación de la máquina virtual, y luego [Ansible](http://www.ansible.com/) para provisionar la máquina y desplegar la app.

Lo primero que debemos hacer es crear los certificados necesarios para conectar con Azure. El proceso de cómo hacerlo lo tienes [aqui](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/documentacion/crearCertificados.md).

Una vez hecho eso, el único comando que se debe ejecutar para realizar el despliegue es:

 `make azure`
 
Esta orden hace automáticamente lo siguiente:

```
sudo apt-get install nodejs-legacy
sudo apt-get install npm
sudo npm install -g azure-cli
sudo pip install paramiko PyYAML jinja2 httplib2 ansible
sudo apt-get install -y vagrant
sudo apt-get install -y virtualbox virtualbox-dkms
vagrant plugin install vagrant-azure
sudo vagrant up --provider=azure
```

Es decir, instala paquetes necesarios para el funcionamiento de Vagrant, Ansible y Azure. Y luego inicia la creación de la máquina virtual en Azure mediante el fichero [Vagrantfile](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/Vagrantfile).

**Vagrantfile**

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
    azure.vm_name = 'pluco-iv'
    azure.vm_user = 'pluco'
    azure.vm_password = 'PlucoDB#'
    azure.vm_location = 'Central US' 
    azure.cloud_service_name = 'pluco-iv'
    azure.ssh_port = '22'
    azure.tcp_endpoints = '8000:80'
  end
  
  config.ssh.username = 'pluco' 
  config.ssh.password = 'PlucoDB#'

  config.vm.provision "ansible" do |ansible|
	ansible.sudo = true
    ansible.playbook = "desplieguePLUCO.yml"
	ansible.verbose = "v"
	ansible.host_key_checking = false 
  end
end
``` 

En este fichero le estamos indicando en el primer bloque que queremos una máquina de azure, que tenga acceso desde Internet mediante una red pública, y por último le aplicaremos "localhost" como hostname para que Ansible pueda conectar con la máquina.

En el segundo bloque, configuramos las propiedades de nuestro servicio en Azure. En él hay que poner el certificado creado anteriormente, el "endpoint" usad el mismo que he puesto, la ID de vuestra suscripción, y luego datos como el sistema operativo de la máquina, el usuario, localización del servidor, etc. En este apartado hay que tener en cuenta que lo que pongamos en "cloud_service_name" será luego el nombre de dominio de nuestra aplicación web (A esto le añade además .cloudapp.net). Y que en "tcp_endpoints" debemos poner el puerto privado a la izquierda y el público a la derecha.

Y para finalizar en la parte de provisión, se ejecuta el "playbook" de Ansible llamado [desplieguePLUCO.yml](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/desplieguePLUCO.yml).

**desplieguePLUCO.yml**

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
      - python-setuptools
      - python-dev
      - build-essential
      - git
      - make
  - name: Clonar repositorio desde git
    git: repo=https://github.com/romilgildo/IV-PLUCO-RMH.git dest=IV-PLUCO-RMH clone=yes force=yes
  - name: Instalar requisitos para la app
    shell: cd IV-PLUCO-RMH && make install
  - name: Ejecutar aplicacion
    command: chdir=IV-PLUCO-RMH nohup python manage.py runserver 0.0.0.0:8000
```

En este fichero empezamos poniendo como host el "localhost", ya que esto se ejecutará dentro de la máquina de Azure. En "tasks", actualizamos repositorios, instalamos una lista de paquetes necesarios, clonamos el repositorio de la app, instalamos requisitos y dependencias, y por último ejecutamos la aplicación. Hay que destacar que en la ejecución usamos "nohup" que permite que se siga ejecutando la aplicación al salir de la terminal.

Tras varios minutos de espera, al final tendremos nuestra [aplicación desplegada y funcionando](http://pluco-iv.cloudapp.net/) como en mi caso:

![Pluco funcionando en Azure](http://i628.photobucket.com/albums/uu6/romilgildo/plucoAzure_zpsgoj0dimp.png~original)
