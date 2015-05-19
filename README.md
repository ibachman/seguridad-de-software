# tarea-seguridad-de-software
Hola! Nuestra aplicación es un sistema de reservas de moteles. Para correrla se necesita python 2.7, django 1.8.1 y sqlite3.

Para installar django y los widgets necesarios para correr la aplicación en ubuntu trusty o linux mint primero debes tener pip (sudo apt-get install python-pip). Luego para continuar tienes dos opciones:

1.- Ejecutar en consola "pip install -r requirements.txt" usando el archivo requirements.txt en el repositorio

2.- Ejecutar "pip install django" y "pip install django-datetime-widget"

Para clonar el proyecto:
git clone https://github.com/ibachman/seguridad-de-software.git

o también se puede simplemente descomprimir el proyecto que subimos a u-cursos ;)

Luego de clonar, en la carpeta del proyecto:
python manage.py runserver

Para poder observar el comportamiento de la base de datos es necesario que el atriburo DEBUG en settings.py sea True, además la aplicación NO VA A CORRER sin este cambio, pues para ello necesitariamos un sitio host el cual no tenemos, por favor poner DEBUG=True. 

En caso de que tuviesemos un host, DEBUG debe ser False para evitar que usuarios puedan ver errores internos.

La base de datos está poblada y su super usuarios es 
usuario:admin
password:123456
