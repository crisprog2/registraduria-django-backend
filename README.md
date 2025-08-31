# Registraduría Django Backend

Backend robusto y documentado para la gestión de registros electorales, lugares de votación, mesas, departamentos y ciudades, siguiendo la estructura de una registraduría colombiana. Desarrollado con Django, Django REST Framework y drf-yasg para documentación interactiva.

## Características principales
- **Modelos alineados con la realidad colombiana:** Departamento, Ciudad, Lugar, Mesa, Persona, Registro.
- **API RESTful completa:** Endpoints CRUD para todos los modelos principales.
- **Endpoints personalizados:**
  - Búsqueda de persona por cédula (incrementa contador de consultas).
  - Reportes agregados: consultas por ciudad, género y edad.
- **Serializadores claros:** Respuestas simplificadas y amigables para frontend.
- **Documentación interactiva:** Swagger y Redoc listos para pruebas y consumo.
- **Listo para frontend React:** CORS configurado para desarrollo local.

## Requisitos
- Python 3.8+ (recomendado 3.13+)
- pip
- (Opcional) MySQL si se desea usar otra base de datos

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
4. **Aplica migraciones:**
   ```bash
   python manage.py migrate
   ```
5. **Ejecuta el servidor:**
   ```bash
   .venv/bin/python manage.py runserver
   ```
6. **Accede al admin:**
   - http://127.0.0.1:8000/admin/

## Estructura del proyecto
- `core/models.py`: Modelos principales, documentados con docstrings detallados.
- `core/views.py`: ViewSets DRF para CRUD y endpoints personalizados, con comentarios y docstrings claros.
- `core/serializers.py`: Serializadores para todos los modelos, documentados.
- `core/urls.py`: Rutas de la API para todos los modelos y reportes personalizados.
- `registraduria/urls.py`: Rutas principales del proyecto y documentación Swagger/Redoc.
- `departamentos_ciudades_colombia.sql`: Script SQL para poblar departamentos y ciudades.

## Endpoints disponibles
Todos los modelos principales cuentan con endpoints tipo REST para listar, crear, consultar, actualizar y eliminar:

- `/api/departamentos/` y `/api/departamentos/<id>/`
- `/api/ciudades/` y `/api/ciudades/<id>/`
- `/api/lugares/` y `/api/lugares/<id>/`
- `/api/mesas/` y `/api/mesas/<id>/`
- `/api/personas/` y `/api/personas/<id>/`
- `/api/registros/` y `/api/registros/<id>/`

### Endpoints personalizados y de reportes
- `/api/personas/buscar-por-cedula/?cedula=<valor>`
  - Devuelve: primer nombre, segundo nombre, primer apellido, segundo apellido, cédula, género, si es jurado, dirección del lugar de votación, mesa, ciudad y departamento.
  - El parámetro `cedula` aparece como campo de entrada en Swagger, facilitando su prueba desde la documentación interactiva.
- `/api/reportes/consultas-por-ciudad/`
  - Devuelve la cantidad total de consultas agrupadas por ciudad.
- `/api/reportes/consultas-por-genero/`
  - Devuelve la cantidad total de consultas agrupadas por género.
- `/api/reportes/consultas-por-edad/`
  - Devuelve la cantidad total de consultas agrupadas por edad.

Cada endpoint soporta los métodos GET, POST, PUT/PATCH y DELETE según corresponda.

## Documentación interactiva (Swagger)
El proyecto incluye documentación automática de la API y todos los endpoints y métodos están documentados y probables desde la interfaz Swagger:

- Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- Redoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## Lógica de reportes agregados
Los endpoints de reportes utilizan agregaciones ORM para devolver la cantidad de consultas realizadas agrupadas por ciudad, género o edad, facilitando el análisis estadístico desde el frontend.

## Notas técnicas
- Por defecto usa SQLite. Si deseas usar MySQL, ajusta la configuración en `settings.py`.
- La API está lista para ser consumida desde un frontend React (CORS configurado para `localhost:3000` y `localhost:5173`).
- Para poblar los departamentos y ciudades de Colombia, ejecuta el script `departamentos_ciudades_colombia.sql` directamente sobre la base de datos SQLite:
   ```bash
   sqlite3 db.sqlite3 < departamentos_ciudades_colombia.sql
   ```

## Licencia
MIT
