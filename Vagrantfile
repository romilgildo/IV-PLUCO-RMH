VAGRANTFILE_API_VERSION = '2'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = 'azure'
  config.vm.network "public_network"
  config.vm.network "private_network",ip: "192.168.56.10", virtualbox__intnet: "vboxnet0"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.define "localhost" do |l|
	l.vm.hostname = "localhost"
  end
    
  config.vm.provider :azure do |azure|
    azure.mgmt_certificate = File.expand_path('~/azure.pem')
    azure.mgmt_endpoint = 'https://management.core.windows.net'
    azure.subscription_id = 'a5c45913-5302-4f3e-9ac2-77b0c0883196'
    azure.vm_image = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_3-LTS-amd64-server-20151218-en-us-30GB'
    azure.vm_name = 'pruebaiv-pluco'
    azure.vm_user = 'pluco'
    azure.vm_password = 'PlucoDB#'
    azure.vm_location = 'Central US' 
    azure.ssh_port = '22'
    azure.tcp_endpoints = '8000:8000'
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
