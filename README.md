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
- `registraduria/settings.py`: Configuración del proyecto
- `REGISTRADURIAPRO.sql`: Script SQL de referencia

## Notas
- Por defecto usa SQLite. Si deseas usar MySQL, ajusta la configuración en `settings.py`.
- No hay endpoints personalizados ni vistas implementadas aún.

## Licencia
MIT
