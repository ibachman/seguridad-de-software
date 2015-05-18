# tarea-seguridad-de-software
Hola! Nuestra aplicación es un sistema de reservas de moteles. Para correrla se necesita python 2.7, django 1.8.1 y sqlite3.

Para installar django en ubuntu trusty o linux mint:
sudo apt-get install python-pip 
pip install django

Para clonar el proyecto:
git clone https://github.com/ibachman/seguridad-de-software.git

o también se puede simplemente descomprimir el proyecto que subimos a u-cursos ;)

Luego de clonar, en la carpeta del proyecto:
python manage.py runserver

Para poder observar el comportamiento de la base de datos es necesario que el atriburo DEBUG en settings.py sea True.
La base de datos está poblada y su super usuarios es 
usuario:admin
password:123456
