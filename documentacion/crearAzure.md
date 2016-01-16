## Creación de máquina virtual en Azure

Lo primero que necesitamos tener es una cuenta en [Azure](https://azure.microsoft.com) y crédito en ella para utilizar sus servicios. 

Aquí tenéis los pasos a seguir para crear una máquina virtual con Ubuntu Server 14.04 en Azure. Hay varias formas de hacer esto, como vamos a ver a continuación:

### Mediante línea de órdenes

Primero empezamos instalando los tres siguientes paquetes:

```
sudo apt-get install nodejs-legacy
sudo apt-get install npm
sudo npm install -g azure-cli
```

Ahora vamos a conectar con nuestra cuenta de Azure:

- Antes de todo deberíamos de hacer `azure config mode asm`

- Creamos la configuración pública para nuestra cuenta: `azure account download`

![Creación de claves Azure](http://i628.photobucket.com/albums/uu6/romilgildo/creacionClavesAzure_zpsccrqzinn.png)

- Descargamos el archivo en el enlace de la captura anterior:

![Obtención de claves Azure](http://i628.photobucket.com/albums/uu6/romilgildo/clavesAzure_zpsrjeihqcs.png~original)

- Importamos el pase de Azure que nos hemos descargado: `azure account import file_location`. En "file_location" ponemos la ubicación del archivo descargado.

![Importar pase de Azure](http://i628.photobucket.com/albums/uu6/romilgildo/ImportamospaseAzure_zpsauod82ho.png)

- Creamos el sitio web con el comando `azure site create --location "West US" web_site`. En "web_site" ponemos el nombre que queremos que tenga la página que acceda a nuestra máquina virtual.

![Creación del sitio web](http://i628.photobucket.com/albums/uu6/romilgildo/creacionwebAzure_zpsikfsp3et.png)

Ya tenemos nuestra máquina en marcha:

![Acceso web a la máquina Azure](http://i628.photobucket.com/albums/uu6/romilgildo/sitiowebFuncionando_zpstzasx1u9.png~original)

Ahora vamos a instalar Ubuntu en ella:

- Buscamos la imagen que queremos de entre las disponibles: `azure vm image list westus ubuntuserver`

![Imágenes dispnibles en Azure](http://i628.photobucket.com/albums/uu6/romilgildo/imagenesAzure_zpsdyfa5kxh.png~original)

- Instalamos la imagen en la máquina virtual: `azure vm create <web site> b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_3-LTS-amd64-server-20151218-en-us-30GB <user> <password> --location "North Europe" --ssh`

![Maquina creada con Ubuntu](http://i628.photobucket.com/albums/uu6/romilgildo/maquinacreadaAzure_zpskx4h0fkh.png)

Ya podemos arrancarla con la orden `azure vm start pruebaiv-romi`:

![Arrancar máquina en Azure](http://i628.photobucket.com/albums/uu6/romilgildo/arrancarmaquinaAzure_zps1kw8qb4f.png)

Para abrir puertos en Azure desde línea de comandos, ejecutamos:

 `azure vm endpoint create nombre-VM 8000 8000`
 
Donde pone "nombre-VM" ponemos el de nuestra máquina, que si no estamos seguro de como se llamaba podemos mirarlo con `azure vm list` que nos muestra las máquinas virtuales creadas.

![Abrir puerto para nuestra app](http://i628.photobucket.com/albums/uu6/romilgildo/abrirpuertosAzurePluco_zps8pxbjzik.png~original)

En mi caso me dice que ya existe el puerto porque lo creé anteriormente.

### Mediante el panel de control web

Nos logueamos en [Portal](https://manage.windowsazure.com) de Azure, y en el panel de control de la izquierda selecciónamos "Máquinas virtuales", y luego damos en "Nuevo":

![Crear maquina virtual en Azure](http://i628.photobucket.com/albums/uu6/romilgildo/crearMVenAzure_zps03693mc0.png~original)

Elegimos el SO que queremos y rellenamos campos como el nombre de la máquina, el nombre de usuario y la suscripción de Azure:

![Elegir SO en Azure](http://i628.photobucket.com/albums/uu6/romilgildo/elegirSOenAzure_zpsovpjnktr.png~original)

En las siguientes pantallas elegimos procesadores, memoria ram, almacenamiento y red, hasta que llegamos al resumen donde aceptamos la máquina y empieza a crearla:

![Eleccion de nucleos](http://i628.photobucket.com/albums/uu6/romilgildo/NucleosAzure_zpsbqjxnkck.png~original)

![Resumen final de la máquina](http://i628.photobucket.com/albums/uu6/romilgildo/resumenMVenAzure_zpsy5c0ropw.png~original)

Con eso ya tenemos nuestra máquina lista, la cual podemos arrancar dando a "Iniciar" abajo:

![Iniciar maquina virtual](http://i628.photobucket.com/albums/uu6/romilgildo/iniciarMVenAzure_zpsgyvraxmz.png)

Si tenéis alguna duda, podéis seguir el [tutorial](https://azure.microsoft.com/es-es/documentation/articles/virtual-machines-linux-tutorial-portal-rm/) de Microsoft Azure.

Para abrir puertos en nuestra máquina virtual, debemos hacerlo como viene explicado [aquí](https://azure.microsoft.com/es-es/documentation/articles/virtual-machines-set-up-endpoints/).

### Mediante gestor de configuración con Vagrant

Esta parte la realizo a la hora de realizar el despliegue de la aplicación en Azure. La podéis ver [aquí](https://github.com/romilgildo/IV-PLUCO-RMH/blob/master/documentacion/despliegueAzure.md)
