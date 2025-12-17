# Python MySQL Docker Project

Este proyecto demuestra cómo conectar una aplicación Python con una base de datos MySQL utilizando Docker Compose, con phpMyAdmin como interfaz de administración opcional.

## 📋 Requisitos

- Docker
- Docker Compose

## 🏗️ Arquitectura del Proyecto

### Contenedor Python Client

Utiliza la imagen oficial `python:3.10` y realiza las siguientes acciones:

- Instala la librería `mysql-connector-python`
- Copia el código de la aplicación al contenedor
- Se conecta a la base de datos MySQL
- Ejecuta operaciones SQL

### app/main.py

El script Python realiza las siguientes acciones:

1. Se conecta a la base de datos MySQL
2. Crea una tabla de ejemplo (si no existe)
3. Ejecuta el comando `SHOW TABLES`
4. Muestra por consola las tablas existentes en la base de datos

## 🚀 Ejecución del Proyecto

### 1. Levantar los contenedores
```bash
docker compose up -d
```

Este comando inicia todos los servicios en segundo plano.

### 2. Ejecutar el cliente Python
```bash
docker exec -it python_client python3 /app/main.py
```

Ejecuta el script Python dentro del contenedor y muestra el resultado de la conexión y las consultas SQL.

### 3. Acceder a phpMyAdmin (opcional)

Desde el navegador, ingresar a:
```
http://localhost:8080
```

**Nota:** Usar las credenciales configuradas en el archivo `docker-compose.yml`.

### 4. Detener y limpiar el entorno

Cuando finalices las pruebas:
```bash
docker compose down -v
```

Este comando detiene los contenedores y elimina los volúmenes asociados a la base de datos.

## 🎯 Objetivo del Proyecto

Este proyecto tiene fines educativos y de prueba, y sirve como base para:

- Aprender Docker Compose
- Probar la comunicación entre contenedores
- Conectar Python con MySQL
- Ejecutar scripts SQL desde una aplicación containerizada

## 📁 Estructura del Proyecto
```
.
├── app/
│   └── main.py
├── docker-compose.yml
└── README.md
```

## 🛠️ Tecnologías Utilizadas

- **Python:** 3.10
- **MySQL:** Latest
- **phpMyAdmin:** Latest
- **Docker Compose:** v2+

## 📝 Notas Adicionales

- Los datos de la base de datos se almacenan en un volumen Docker para persistencia
- La red entre contenedores está configurada automáticamente por Docker Compose
- El contenedor Python espera a que MySQL esté listo antes de ejecutar el script
