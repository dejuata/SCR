## SCR


  1. Crear base de datos (revisar settings.py) 
  2. Ejecutar el archivo requirements.txt
  3. python manage.py makemigrations
  4. python manage.py migrate_schemas
  5. ejecutar los archivos sql que están en la carpeta querys en el siguiente orden:
  
    * 00_insertar_superusuario.sql
    * 01_insertar_tenant.sql
    * 02_relacionar_dominio.sql
    * 00_users_schema_public.sql
    
   6. levantar servidor
  
