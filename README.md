Proyecto API con FastAPI y Docker

Este proyecto es una API desarrollada con FastAPI, diseñada para ser escalable y fácilmente convertible a un sistema basado en microservicios. Utiliza PostgreSQL como base de datos, Nginx como proxy reverso, y Docker para su despliegue e infraestructura.

Características

Framework: FastAPI (rápido y moderno)

Base de datos: PostgreSQL

Proxy reverso: Nginx

Modularidad: Preparado para escalar con microservicios

Contenedores: Configuración lista con Docker y Docker Compose

Fácil despliegue: Compatible con VPS o AWS

Requisitos previos

Docker y Docker Compose instalados

Python 3.10+ para desarrollo local

Configurar un archivo .env (ver Configuración)

Instalación y Configuración

1. Clonar el repositorio

git clone https://github.com/harold2tg/MDT-para-fastapi
cd proyecto-api

2. Configurar variables de entorno

Crea un archivo .env en la raíz del proyecto con el siguiente contenido:

# Variables para PostgreSQL
DATABASE_HOST=aqui la ip del servidor
POSTGRES_USER= aqui va el usuario
POSTGRES_PASSWORD=aqui va la password
POSTGRES_DB=aqui va el nombre del base de datos

# Variables para pgAdmin
PGADMIN_DEFAULT_EMAIL=el correo 
PGADMIN_DEFAULT_PASSWORD= la password

3. Construir los contenedores

docker-compose build

4. Levantar los servicios

docker-compose up -d

5. Acceder a la aplicación

API principal: http://localhost:8000

Documentación automática:

Swagger UI: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc

Nginx (proxy reverso): http://localhost

pgAdmin: http://localhost:16543

Usuario: admin@admin.com

Contraseña: admin

6. Detener los servicios

docker-compose down

7. Verificar variables de entorno

Para asegurarte de que las variables de entorno se cargaron correctamente en los contenedores, usa el siguiente comando:

docker exec -it postgres env

Esto mostrará todas las variables de entorno activas en el contenedor postgres.

