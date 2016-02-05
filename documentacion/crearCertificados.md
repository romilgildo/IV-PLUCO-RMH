## Creación de certificado para Azure

Para poder conectar con Azure desde línea de comandos o desde otros programas como Ansible o Juju, debemos realizar una serie de tareas.

Primero empezamos instalando los tres siguientes paquetes:

```
sudo apt-get install nodejs-legacy
sudo apt-get install npm
sudo npm install -g azure-cli
```

Ahora vamos a conectar con nuestra cuenta de Azure:

- Antes de todo deberíamos de hacer `azure config mode asm`

- Nos logueamos con `azure login`

- Creamos la configuración pública para nuestra cuenta: `azure account download`

![Creación de claves Azure](http://i628.photobucket.com/albums/uu6/romilgildo/creacionClavesAzure_zpsccrqzinn.png)

- Descargamos el archivo de credenciales desde el enlace de la captura anterior:

![Obtención de claves Azure](http://i628.photobucket.com/albums/uu6/romilgildo/clavesAzure_zpsrjeihqcs.png~original)

- Importamos el pase de Azure que nos hemos descargado: `azure account import file_location`. En "file_location" ponemos la ubicación del archivo descargado.

![Importar pase de Azure](http://i628.photobucket.com/albums/uu6/romilgildo/ImportamospaseAzure_zpsauod82ho.png)

- Ahora generamos el certificado necesario para que conectar con Azure con los siguientes comandos:

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout azure.pem -out azure.pem
openssl x509 -inform pem -in azure.pem -outform der -out azure.cer
chmod 600 azure.pem
```

Esto nos creará dos ficheros, uno "azure.cer" y otro "azure.pem". Ahora vamos a subir el nuevo certificado a nuestra cuenta de Azure. 

En el portal de Azure, pinchamos en Configuración > Certificados de administración > Cargar:

![Subir certificado a Azure](http://i628.photobucket.com/albums/uu6/romilgildo/cargar_certificadoAzure_zps09k2qqrl.png~original)

Y seleccionamos el archivo "azure.cer". Ya habremos terminado.

![Certificado cargado](http://i628.photobucket.com/albums/uu6/romilgildo/certificadoAzureVagrant_zpsvc2noghr.png)
