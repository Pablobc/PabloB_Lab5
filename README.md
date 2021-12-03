# PabloB_Lab5
##Requisitos
Esta api hace uso de los paquetes Flask, Flask Cors y el conector Mysql para python 3. Además de hacer uso de npm para el frontend.

Para instalar Flask:

```
pip install Flask
```
Para instalar Flask cors:

```
pip install -U flask-cors
```
Para instalar el conector Mysql:

```
pip install mysql-connector-python
```

Para instalar npm y nodejs:

```
sudo apt update
sudo apt install nodejs
sudo apt install npm
```
##Para configurar la base de datos

Primero se ingresan los siguientes comandos:

```
sudo apt-get update
sudo apt-get install mysql-server
```

Ingresar a mysql como root:

```
sudo mysql_secure_installation
```

Continuar con los pasos siguientes a la instalación, 
poner una clave deseada para ingresar como root y después borrar
todos los usuarios de prueba que mysql genera.

Posteriormente, ingresar a mysql:
```
sudo mysql -u root
Enter password:
<tucontraseña>
```

Crear base de datos y tablas, ejecutando el código de la siguiente forma:
```
source /<path-to-file>/CREATE_USER.sql
CONNECT pdfdatos;
source /<path-to-file>/DDL.sql
```

Una vez teniendo todo sin errores, la base de datos estará lista para usar.

##Instalacion del frontend
Con una terminal dentro de la carpeta client.
Ejecutar:
```
npm install --save
```
Luego para ejecutar el frontend, dentro de la misma carpeta, usar
```
npm run serve
```
##Para configurar el quick start de flask, con una terminal dentro de la carpeta apiPDF ejecutar:

```
export FLASK_APP=app.py
```
Luego para ejecutar el backend usar
```
flask run
```
##Para usar la api
Al momento de ejecutar tanto backend como frontend, se podran hacer llamdas a la api, y poder ver los cambios en la base de datos en la direccion que otorga el frontend.
La direccion del frontend es http://127.0.0.1:8080/
La direccion del backend es http://127.0.0.1:5000/

Para poder mandar datos a la api, se debe usar un navegador o un curl que tenga configurado un user agent. La llamada es de la siguiente manera:
```
http://127.0.0.1:5000/api/load?psw=alguna password
```
De esta forma se guardará en la base de datos la ip del cliente, el sistema operativo, la version y la password entregada en la consulta.
Otra manera de hacerlo sería de la siguiente manera:
```
curl -X POST -d 'psw=alguna password' http://127.0.0.1:5000/api/load
```
Luego esto se vería reflejado en la parte del frontend.


