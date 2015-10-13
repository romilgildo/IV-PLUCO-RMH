#PLATAFORMA UNIVERSITARIA DE COMPARTICIÓN DE CONOCIMIENTOS: PLUCO

###Introducción

Se trata de una plataforma académica de compartición de archivos de la Universidad de Granada, que permite la colaboración en grupo entre los usuarios del sistema. Ofrece servicios de almacenamiento de archivos en la nube, y de mensajería y foros para la resolución de dudas, potenciando la interacción de los usuarios, y agrupando a los mismos por grupos, por ejemplo de asignaturas o cursos.

###Seguridad

En cuanto a la seguridad de nuestra plataforma los objetivos son: Permitir tener un sistema seguro en el que se separen datos sensibles y credenciales de los usuarios, y por otra parte archivos de los mismos. Además tendremos una web con foros que si es atacada no compremete la privacidad de los usuarios ni sus archivos.

###Infraestuctura

En mi infraestructura, realizaré un despliegue sobre Azure de un sistema de organización y gestión de datos de los usuarios de la plataforma, y que permitirá recuperar la información de los usuarios, consultar sus datos asociados, modificar los datos, además de los procesos asociados a dar de alta o baja a los usuarios. 

Irá instalado sobre una máquina virtual que actúa como servidor, y que tendrá acceso a la información almacenada mediante una página web, cuyo servidor web podría estar alojado en un servidor distinto al de la base de datos, con el objetivo de repartir la carga y dar mayor seguridad a la infraestructura. 

La base de datos usada será MySQL y que deberá contener información sobre las asignaturas matriculadas e información personal de los usuarios. 

Como lenguaje de programación se usará Python. Además utilizaremos Django como framework para agilizar el desarrollo web.  

El resto de mis compañeros deberán crear: 

1. Un sistema web/red social de foros y dudas similar a Stackoverflow. Tendría detrás un servidor web para alojar las páginas y otro servidor para la base de datos de los usuarios.

2. Un sistema de almacenamiento sftp de recursos en la nube, que se usará para la organización, administración y compartición de archivos. Todo esto irá implementado en otro servidor que usaremos de Cloud Storage, además de un sistema de acceso a los datos y recursos por parte de los usuarios.

Al final del proyecto, deberemos enlazar en conjunto las tres partes del proyecto, y realizar el despliegue correcto sobre cualquier infraestructura virtual.

[Apuntados en el proyecto de software libre de la oficina OSL](http://osl.ugr.es/bases-de-los-premios-a-proyectos-libres-de-la-ugr/)
