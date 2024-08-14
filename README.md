# Django E-Learning Platform

Este es el cuarto proyecto del libro *Django 5 By Example: Build powerful and reliable Python web applications from scratch (English Edition)*. Este proyecto abarca los siguientes capítulos y alcances:

## Capítulos del Libro

### Capítulo 12: Construyendo una Plataforma de E-Learning
Te guiará en la creación de una plataforma de e-learning. Añadirás fixtures a tu proyecto y crearás modelos iniciales para el sistema de gestión de contenido. Utilizarás herencia de modelos para crear modelos de datos para contenido polimórfico. Aprenderás a crear campos de modelos personalizados construyendo un campo para ordenar objetos. También implementarás vistas de autenticación para el CMS.

### Capítulo 13: Creando un Sistema de Gestión de Contenidos
Te enseñará a crear un CMS usando vistas basadas en clases y mixins. Utilizarás el sistema de grupos y permisos de Django para restringir el acceso a las vistas e implementarás formsets para editar el contenido de los cursos. Además, crearás una funcionalidad de arrastrar y soltar para reordenar los módulos de los cursos y su contenido utilizando JavaScript y Django.

### Capítulo 14: Renderizando y Cacheando Contenido
Te mostrará cómo implementar las vistas públicas para el catálogo de cursos. Crearás un sistema de registro de estudiantes y gestionarás la inscripción de estudiantes en los cursos. Implementarás la funcionalidad para renderizar diferentes tipos de contenido para los módulos de los cursos. Aprenderás a cachear contenido utilizando el framework de caché de Django y configurar los backends de caché Memcached y Redis para tu proyecto. Finalmente, aprenderás a monitorear Redis usando el sitio de administración.

### Capítulo 15: Construyendo una API
Explora la construcción de una API RESTful para tu proyecto utilizando Django REST framework. Aprenderás a crear serializers para tus modelos y construir vistas de API personalizadas. Manejarás la autenticación de la API e implementarás permisos para las vistas de la API. Aprenderás a construir viewsets y routers de API. El capítulo también te enseñará cómo consumir tu API utilizando la biblioteca Requests.

### Capítulo 16: Construyendo un Servidor de Chat
Explica cómo usar Django Channels para crear un servidor de chat en tiempo real para los estudiantes. Aprenderás a implementar funcionalidades que dependen de la comunicación asincrónica a través de WebSockets. Crearás un consumidor de WebSocket con Python e implementarás un cliente de WebSocket con JavaScript. Utilizarás Redis para configurar una capa de canal y aprenderás a hacer tu consumidor de WebSocket totalmente asincrónico. También implementarás un historial de chat persistiendo mensajes de chat en la base de datos.

### Capítulo 17: Poniéndolo en Producción
Te mostrará cómo crear configuraciones para múltiples entornos y cómo configurar un entorno de producción utilizando PostgreSQL, Redis, uWSGI, NGINX y Daphne con Docker Compose. Aprenderás a servir tu proyecto de forma segura a través de HTTPS y utilizar el framework de verificación del sistema de Django. El capítulo también te enseñará a construir un middleware personalizado y crear comandos de gestión personalizados.

## Puesta en Marcha

### Prerrequisitos

### Instalación de Dependencias

1. **Clonar el repositorio:**

    ```sh
    git clone https://github.com/tomasrpita/django-e-learnig-platform.git
    
    ```

2. **Crear un entorno virtual e instalar las dependencias de Python:**

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

### Configuración de Docker

1. **Iniciar los servicios con Docker Compose:**

    ```sh
    docker-compose up -d
    ```

### Configuración de la Aplicación Django

1. **Ejecutar las migraciones de la base de datos:**

    ```sh
    python ./educa/manage.py migrate
    ```

2. **Crear un superusuario:**

    ```sh
    python ./educa/manage.py createsuperuser
    ```

3. **Cargar datos iniciales (si aplica):**

    ```sh
    python ./mysite/manage.py loaddata initial_data.json
    ```

### Iniciar el Servidor de Desarrollo

1. **Iniciar el servidor de desarrollo de Django:**

    ```sh
    python ./educa/manage.py runserver 0.0.0.0:8000
    ```

### Acceso a la Aplicación

- La aplicación estará disponible en `http://localhost:8000`.
- La interfaz de administración de Django estará en `http://localhost:8000/admin`.
