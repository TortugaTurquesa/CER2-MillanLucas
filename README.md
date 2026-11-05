Que tal estimado usuario, aqui una pequeña guia para iniciar el servidor (Se asume en este documento que se utlizara como sistema operativo a Windows) :

Instalar python:

- Entra a https://www.python.org/ 
- Entra a sección de descarga y descarga la versión de Windows
- Cuando el ejecutable haya sido descargado, debera instalarlo abriendolo y siguiendo las indicaciones del asistente de instalación

Instalar las dependencias:
- Abra "CMD"
- ejecute el siguiente comando para instalar las dependencias necesarias: "pip install -r requirements.txt"

Aplicar las migraciones de la base de datos:
- Ahora deberá dirigerse a la carpeta donde se encuentra el archivo "manage.py", cuando lo encuentre, desde CMD ejecute el comando "cd ..." remplazando los puntos por la dirección del archivo.
- Una vez cambiado el directorio en el CMD ejecute el siguiente comando en CMD "python manage.py makemigrations" y posteriomente el siguiente comando "python manage.py migrate"

____________________________
Ahora su dispositivo podra correr el servidor, sin embargo ahora veremos como hacerlo además de otras herramientas utiles para gestionar el proyecto

Ejecutar el servido:
- Como en el paso anterior, el directorio del CMD deberá estar apuntando a la ubicación del archivo "manage.py", cuando se encuentre allí, ejecute el comando "python manage.py runserver"

Crear un superusuario (para acceder al panel de gestión):
 Un super usuario, dentro del proyecto tiene la capacidad de funciones privilegiadas, tales como agregar, editar y quitar lugares de interes, para no tener que modificar la base de datos directamente desde los archivos se facilita este metodo dentro del proyecto, pero debera crear el super usuario, esto se hace de la siguietne manera
 - Mientras el CMD apunta hacia la carpeta que contiene "manage.py" se debera ejecutar el comando "python manage.py createsuperuser"
 - Una vez ejecutado el comando, CMD le indicara los siguientes datos en el siguiente orden: Nombre de Usuario - correo electronico - contraseña - confirmación de contraseña; 
 - Complete los campos indicados
 - Cuando lo cree, debera ejecutar el servidor, dentro del mismo, en el formulario de inicio de sesion agrege los datos que usted puso en el super usuario, y alli podra acceder a un menu especial llamado gestion



Paso opcional y recomendado:

Crear y activar el entorno virtual:
este paso, de cierta forma es opcional, sin embargo es una buena practica para mantener orden y evitar errores
- Abrir CMD 
- Ejecutar el comando "python -m venv venv"
- Despues debera activar el entorno virtual, para ello debera escribri en el CMD "..\venv\Scripts\activate"

__________________________________
Paso final: Disfrute


