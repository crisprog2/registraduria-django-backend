# Registraduría Django Backend

Este proyecto es un backend básico en Django para la gestión de registros de personas, lugares de votación y usuarios, inspirado en la estructura de una registraduría.

## Requisitos
- Python 3.8+
- pip
- (Opcional) MySQL si se desea usar la base de datos del archivo SQL

## Instalación y uso rápido

1. **Clona el repositorio y entra al directorio:**
   ```bash
   git clone <repo_url>
   cd registraduria-django-backend
   ```
2. **Crea y activa el entorno virtual:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
   O simplemente:
   ```bash
   pip install django
   ```

4. **Aplica migraciones (ya migradas en SQLite por defecto):**
   ```bash
   python manage.py migrate
   ```
   > Los modelos ya han sido migrados a la base de datos SQLite.

5. **Ejecuta el servidor:**
   ```bash
   python manage.py runserver
   ```
6. **Accede al admin:**
   - http://127.0.0.1:8000/admin/


## Estructura principal
- `core/models.py`: Modelos principales (Departamento, Ciudad, Lugarvoto, Usuario, Persona, Registro)
- `core/views.py`: Vistas tipo API para CRUD de todos los modelos principales
- `core/urls.py`: Rutas de la API para todos los modelos
- `registraduria/settings.py`: Configuración del proyecto y CORS
- `REGISTRADURIAPRO.sql`: Script SQL de referencia


## Endpoints disponibles
Todos los modelos principales cuentan con endpoints tipo REST para listar, crear, consultar, actualizar y eliminar:

- `/api/departamentos/` y `/api/departamentos/<id>/`
- `/api/ciudades/` y `/api/ciudades/<id>/`
- `/api/lugaresvoto/` y `/api/lugaresvoto/<id>/`
- `/api/personas/` y `/api/personas/<id>/`
- `/api/registros/` y `/api/registros/<id>/`

Cada endpoint soporta los métodos GET, POST, PUT y DELETE según corresponda.

## Documentación interactiva (Swagger / Redoc)
El proyecto incluye documentación automática de la API:

- Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- Redoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

Para aprovechar Swagger al máximo, se recomienda migrar las vistas a Django REST Framework.

## Notas
- Por defecto usa SQLite. Si deseas usar MySQL, ajusta la configuración en `settings.py`.
- La API está lista para ser consumida desde un frontend React (CORS configurado para `localhost:3000` y `localhost:5173`).

## Licencia
MIT
