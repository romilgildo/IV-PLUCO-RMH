#PLATAFORMA UNIVERSITARIA DE COMPARTICIÓN DE CONOCIMIENTOS: PLUCO

###Introducción

Se trata de una plataforma académica de compartición de archivos de la Universidad de Granada, que permite la colaboración en grupo entre los usuarios del sistema. Además ofrecerá servicios de mensajería y foros, potenciando la interacción de los usuarios, y agrupando a los mismos por grupos, por ejemplo de asignaturas o cursos.

###Seguridad

En cuanto a la seguridad de nuestra plataforma los objetivos son: Permitir tener un sistema seguro en el que se separen datos sensibles y credenciales de los usuarios, y por otra parte archivos de los mismos. Por otro lado tendremos una web con foros que si es atacada no compremete la privacidad de los usuarios ni sus archivos.

###Infraestuctura

En mi infraestructura, realizaré un despliegue de un sistema de organización y gestión de datos de los usuarios, que los tendremos alojados en otro servidor independiente con las bases de datos en SQL. Estas bases de datos deberá contener información sobre las asignaturas matriculadas e información personal del usuario, y dicho acceso a datos tendrá sus respectivos permisos. 
Consistirá en una base de datos instalada sobre una máquina virtual que actúa como servidor, y que tendrá acceso a la información almacenada mediante una página web, cuyo servidor web podría estar alojado en un servidor distinto al de la base de datos.

El resto de mis compañeros deberán crear: 

1. Un sistema web/red social de foros y dudas similar a Stackoverflow. Tendría detrás un servidor web para alojar las páginas y otro servidor para la base de datos de los usuarios.

2. Un sistema de almacenamiento sftp de recursos en la nube, que se usaraá para la organización, administración y compartición de archivos. Todo esto irá implementado en otro servidor que usaremos de Cloud Storage, además de un sistema de acceso a los datos y recursos por parte de los usuarios.

Al final del proyecto, deberemos enlazar en conjunto las tres partes del proyecto, y realizar el despliegue correcto.
