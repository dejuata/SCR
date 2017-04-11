## SCR


  1. Crear base de datos (revisar settings.py) 
  2. python manage.py makemigrations
  3. python manage.py migrate_schemas
  4. ejecutar el siguiente codigo sql (para crear el tenant publico):
  
    `insert into tenant_tenant("schema_name", "nit", "correo", "ciudad", "direccion") 
              values ('public', 1143859996, 'uncorreo@hotmail.com', 'una ciudad', 'una dirección');`
