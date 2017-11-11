SCR
================================

Este proyecto es una aplicación tipo SaaS, desarrollado bajo la arquitectura Multitenat para permitir en una sola instancia de la aplicación servir a muchos clientes (Modelo de maduración Nivel 3 "Configurable y eficiente"). Con respecto al modelo de datos elásticos se implemento base de datos compartidas (Shared database-sharded) por medio de la libreria [django-tenants-schemas](https://github.com/bernardopires/django-tenant-schemas) que permite en una sola base de datos generar schemas y asociarlos por medio de la url a un tenant.

Instalación
------------

1. Crear base de datos (revisar settings.py)
2. Ejecutar el archivo requirements.txt
3. ``python manage.py makemigrations``
4. ``python manage.py migrate_schemas``
5. ejecutar los archivos sql que están en la carpeta querys en el siguiente orden:

  * 00_insertar_superusuario.sql
  * 01_insertar_tenant.sql
  * 02_relacionar_dominio.sql
  

 6. levantar servidor e ingresar a [localhost:8000](http://localhost:8000/)


Configuración
------------
1. Cree una cuenta en el sistema por medio de un correo y contraseña [signin](http://localhost:8000/signup)
2. Ingrese departamentos y ciudades; para eso dirijase a la siguiente ruta 

   ``http://localhost:8000/cities/cities/``
   
   y cargue el archivo de excel llamado colombia.xls

2. Cree una empresa, la información de la empresa es la que se utiliza para crear un tenant en el sistema
3. Ingrese a la nueva url de acuerdo al nombre comercial que haya digitado en el formulario de crear empresa, ejemplo:

  ``http://tenant2.localhost:8000/``
  
4. Ingrese con el usuario previamente creado
5. Si desea cargar información al sistema, lo puede hacer por medio de la opción carga masiva que se encuentra en cada modulo y subiendo los archivos de excel que se encuentran en este repositorio.

Funcionalidades básicas
------------

* Gestión de usuarios.
* Gestión de clientes.
* Gestión de vehículos.
* Gestión de conductores.
* Gestión de rutas
* Gestión de reportes
* Generar un archivo en formato JSON
* Personalización de tenant

Librerias externas
------------
Este proyecto hace uso de las siguientes librerias de terceros:

* [Django JET](https://github.com/geex-arts/django-jet): Administrador de Django
* [Django Custom User](https://github.com/jcugat/django-custom-user): Cambia el comportamiento del usuario por defecto de Django
* [Django reCaptcha v2](https://github.com/kbytesys/django-recaptcha2)
* [Anymail](https://github.com/anymail/django-anymail): Django email backends for Mailgun
* [Django-Select2](https://github.com/applegrew/django-select2) Input select2 for Django
* [django-excel](https://github.com/pyexcel/django-excel)
