Universidad Icesi

Christian Cárdenas

A00212740

Sistemas Operativos

Prof. Daniel Barragán

Repositorio: http://github.com/cdcardenas/so-exam2/

Parcial 2: Flask y Swagger


1. El script background.py se encarga de ejecutar los comandos correspondientes para capturar la información de uso de memoria RAM, CPU, disco duro y estado del servicio httpd, como el requerimiento pide que este script se ejecute en segundo plano cada 60 segundos, se utilizo crontab para solucionar el problema.

crontab es un servicio del sistema operativo que permite agendar la ejecucion de trabajos o jobs por usuario en este caso se uso el comando:

	$ crontab -u check_user -e

este comando permite editar el archivo de configuración de crontab en donde introducimos las lineas :
      
* * * * * python ~/repositories/so-exam2/A00212740/background.py > ~/repositories/so-exam2/A00212740/dblocal.txt
* * * * * python ~/repositories/so-exam2/A00212740/consultas.py

la primera linea le indica a crontab que queremos que se ejecute cada el script background.py cada 60 segundos y que la salida que esta generando el scripot sea almacenada en el archivo de texto dblocal.txt
la segunda linea ejecuta el script consultas.py cada 60 segundos y almacena en la base de datos test.db por medio de sqliteAlchemy

código fuente del script background.py: 

![][1]

![][2]


código fuente del script consultas.py y del modelo de base de datos llamado modelo.py

![][8]

![][9]

2. Para el despliegue del API se utilizo Flask y SwaggerUI con el siguiente código fuente:

![][3]

Esta API permite mediante una peticion tipo GET mostrarle al usuario el consumo de recursos del equipo. La documentación de la API se realizo con  flask restplus y SwaggerUI que permiten generar documentación de forma ordenada.

A la documentación se puede acceder mediante la url: Dirección_IP:Puerto 

![][6]

![][4]

![][5]

Para los comandos usados para obtener la información del sistema fueron:

RAM: 

	$ vmstat -s -S m 
HDD: 

	$ df /dev/mapper/cl-root -h awk {print $4}
CPU: 

	$ sar 1 1 |  awk {print $5}
Servicio: 

	$ /usr/sbin/service httpd status | awk -F  ‘Active:’ {print $2}

![][7]

3. Anexos

se adjuntan los codifos fuentes para el aplicativo Flask, el script de consultas en segundo plano y el modelo de base de datos.



[1]: images/1.png
[2]: images/2.png
[3]: images/3.png
[4]: images/4.png
[5]: images/5.png
[6]: images/6.png
[7]: images/7.png
[8]: images/db1.png
[9]: images/db2.png

