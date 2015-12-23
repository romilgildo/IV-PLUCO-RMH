## Creación de máquina virtual en Azure

Aquí tenéis los pasos a seguir para crear una máquina virtual con Ubuntu Server 14.04 en Azure. Hay dos formas de hacer esto, o mediante el panel de control web o por línea de órdenes. Lo primero que necesitamos tener es una cuenta en [Azure](https://azure.microsoft.com/es-es/) y crédito en ella para utilizar sus servicios. 

### Mediante línea de órdenes

Primero empezamos instalando los tres siguientes paquetes:

```
sudo apt-get install nodejs-legacy
sudo apt-get install npm
sudo npm install -g azure-cli
```

Ahora vamos a conectar con nuestra cuenta de Azure:

- Creamos la configuración pública para nuestra cuenta: `azure account download`

![Creación de claves Azure](https://www.dropbox.com/s/3lcu5ns8pkz28wm/creacionClavesAzure.PNG?dl=1)

- Descargamos el archivo en el enlace de la captura anterior:

![Obtención de claves Azure](https://www.dropbox.com/s/cxu5anvhz4f312s/clavesAzure.PNG?dl=1)

- Importamos el pase de Azure que nos hemos descargado: `azure account import <file location>`. En <file location> ponemos la ubicación del archivo descargado.

![Importar pase de Azure](https://www.dropbox.com/s/ofm30xuwoy5cwcf/ImportamospaseAzure.PNG?dl=1)

- Creamos el sitio web con el comando `azure site create --location "West US" <web site>`. En <web site> ponemos el nombre que queremos que tenga la página que acceda a nuestra máquina virtual.

![Creación del sitio web](https://www.dropbox.com/s/w5uysgzon8dd11i/creacionwebAzure.PNG?dl=1)

Ya tenemos nuestra máquina en marcha:

![Acceso web a la máquina Azure](https://www.dropbox.com/s/7l32ag6dmcwz8eq/sitiowebFuncionando.PNG?dl=1)

Ahora vamos a instalar Ubuntu en ella:

- Buscamos la imagen que queremos de entre las disponibles: `azure vm image list westus ubuntuserver`

![Imágenes dispnibles en Azure](https://www.dropbox.com/s/wxri8ctmgog25sz/imagenesAzure.PNG?dl=1)

- Instalamos la imagen en la máquina virtual: `azure vm create <web site> b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_3-LTS-amd64-server-20151218-en-us-30GB <user> <password> --location "North Europe" --ssh`

![Maquina creada con Ubuntu](https://www.dropbox.com/s/9kumm7jq9hg7y3x/maquinacreadaAzure.png?dl=1)

Ya podemos arrancarla con la orden `azure vm start pruebaiv-romi`:

![Arrancar máquina en Azure](https://www.dropbox.com/s/7z6jw3goxpn2npe/arrancarmaquinaAzure.PNG?dl=1)

### Mediante el panel de control web

Nos logueamos en [Portal](https://manage.windowsazure.com) de Azure, y en el panel de control de la izquierda selecciónamos Máquinas virtuales, y luego damos en Nuevo:

![Crear maquina virtual en Azure](https://www.dropbox.com/s/zjief2ttmheaw09/crearMVenAzure.PNG?dl=1)

Elegimos el SO que queremos y rellenamos campos como el nombre de la máquina, el nombre de usuario y la suscripción de Azure:

![Elegir SO en Azure](https://www.dropbox.com/s/2tnl39i89lf2cll/elegirSOenAzure.PNG?dl=1)

En las siguientes pantallas elegimos procesadores, memoria ram, almacenamiento y red, hasta que llegamos al resumen donde aceptamos la máquina y empieza a crearla:

![Eleccion de nucleos](https://www.dropbox.com/s/h7vme0o14whnx1i/NucleosAzure.PNG?dl=1)

![Resumen final de la máquina](https://www.dropbox.com/s/itnrr2t326qq0ft/resumenMVenAzure.PNG?dl=1)

Con eso ya tenemos nuestra máquina lista, la cual podemos arrancar dando a Iniciar:

![Iniciar maquina virtual](https://www.dropbox.com/s/5m274ivj72kvzjj/iniciarMVenAzure.PNG?dl=1)
