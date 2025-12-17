

# Proyecto de prueba: Docker + Python + MySQL

Este proyecto es un **entorno de prueba con Docker** que demuestra la conexión de una aplicación Python a una base de datos MySQL utilizando contenedores.

Se utilizan **tres servicios** orquestados con Docker Compose:

- **MySQL**: base de datos relacional.
- **phpMyAdmin**: administrador web de MySQL.
- **Python**: cliente que se conecta a la base de datos y ejecuta operaciones SQL.

---

## Requisitos

- Docker
- Docker Compose

---

## Estructura del proyecto

```text
.
├── docker-compose.yml
├── Dockerfile
└── app
    └── main.py

## Descripción de los componentes
docker-compose.yml

Define tres servicios:

mysql
Contenedor de la base de datos MySQL.

phpmyadmin
Interfaz web para administrar la base de datos MySQL.

python_client
Contenedor Python que se construye a partir del Dockerfile y se conecta a MySQL.

## Dockerfile

Utiliza la imagen oficial python:3.10.

Instala la librería mysql-connector-python.

Copia el código de la aplicación al contenedor.

## app/main.py

El script Python realiza las siguientes acciones:

Se conecta a la base de datos MySQL.

Crea una tabla de ejemplo (si no existe).

Ejecuta el comando SHOW TABLES.

Muestra por consola las tablas existentes en la base de datos.

## Ejecución del proyecto
1. Levantar los contenedores
docker compose up -d


Este comando inicia todos los servicios en segundo plano.

2. Ejecutar el cliente Python
docker exec -it python_client python3 /app/main.py


Ejecuta el script Python dentro del contenedor y muestra el resultado de la conexión y las consultas SQL.

3. Acceder a phpMyAdmin (opcional)

Desde el navegador, ingresar a:

http://localhost:8080


Usar las credenciales configuradas en el archivo docker-compose.yml.

4. Detener y limpiar el entorno

Cuando finalices las pruebas:

docker compose down -v


Este comando detiene los contenedores y elimina los volúmenes asociados a la base de datos.

## Objetivo del proyecto

Este proyecto tiene fines educativos y de prueba, y sirve como base para:

- Aprender Docker Compose.

- Probar la comunicación entre contenedores.

- Conectar Python con MySQL.

- Ejecutar scripts SQL desde una aplicación containerizada.
