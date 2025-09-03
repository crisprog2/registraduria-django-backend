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
- PostgreSQL

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
4. **Configura la base de datos PostgreSQL:**
   - Crea una base de datos y un usuario en PostgreSQL.
   - Crea un archivo `.env` en la raíz del proyecto con:
     ```env
     DB_NAME=nombre_de_tu_db
     DB_USER=tu_usuario
     DB_PASSWORD=tu_contraseña
     DB_HOST=localhost
     DB_PORT=5432
     ```
5. **Aplica migraciones:**
   ```bash
   python manage.py migrate
   ```
6. **Ejecuta el servidor:**
   ```bash
   .venv/bin/python manage.py runserver
   ```
7. **Accede al admin:**
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


## Ejemplo de uso de endpoints (con curl)

### 1. Autenticación y obtención de token JWT

```bash
# Obtener token JWT
curl -X POST http://127.0.0.1:8000/api/token/ \
   -H "Content-Type: application/json" \
   -d '{"email": "usuario@correo.com", "password": "tu_contraseña"}'
# Respuesta:
# {"refresh": "<refresh_token>", "access": "<access_token>"}
```

### 2. Consumir endpoint protegido con JWT

```bash
curl -X GET http://127.0.0.1:8000/api/departamentos/ \
   -H "Authorization: Bearer <access_token>"
```

### 3. Endpoint público: buscar persona por cédula

```bash
curl -X GET "http://127.0.0.1:8000/api/personas/buscar-por-cedula/?cedula=123456789"
```

### 4. Crear un nuevo registro (ejemplo POST)

```bash
curl -X POST http://127.0.0.1:8000/api/ciudades/ \
   -H "Authorization: Bearer <access_token>" \
   -H "Content-Type: application/json" \
   -d '{"cod_Ciudad": "001", "ciudad": "Bogotá", "cod_Departamento": "11"}'
```

### 5. Refrescar el token JWT

```bash
curl -X POST http://127.0.0.1:8000/api/token/refresh/ \
   -H "Content-Type: application/json" \
   -d '{"refresh": "<refresh_token>"}'
# Respuesta:
# {"access": "<nuevo_access_token>"}
```

## Autenticación y seguridad

La autenticación se realiza mediante JWT (JSON Web Token). Todos los endpoints (excepto `/api/personas/buscar-por-cedula/` y los de obtención/refresh de token) requieren el header:

```
Authorization: Bearer <access_token>
```

Para obtener el token, usa el endpoint `/api/token/` enviando email y contraseña. Para refrescar el access token, usa `/api/token/refresh/`.
