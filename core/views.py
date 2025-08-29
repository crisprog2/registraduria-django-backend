# --- Ciudad ---
"""
Endpoints para Ciudad:
- GET /api/ciudades/ : Lista todas las ciudades
- POST /api/ciudades/ : Crea una nueva ciudad
- GET /api/ciudades/<id>/ : Consulta una ciudad por ID
- PUT /api/ciudades/<id>/ : Actualiza una ciudad
- DELETE /api/ciudades/<id>/ : Elimina una ciudad
"""
# --- Lugarvoto ---
"""
Endpoints para Lugarvoto:
- GET /api/lugaresvoto/ : Lista todos los lugares de voto
- POST /api/lugaresvoto/ : Crea un nuevo lugar de voto
- GET /api/lugaresvoto/<id>/ : Consulta un lugar de voto por ID
- PUT /api/lugaresvoto/<id>/ : Actualiza un lugar de voto
- DELETE /api/lugaresvoto/<id>/ : Elimina un lugar de voto
"""
# --- Persona ---
"""
Endpoints para Persona:
- GET /api/personas/ : Lista todas las personas
- POST /api/personas/ : Crea una nueva persona
- GET /api/personas/<id>/ : Consulta una persona por ID
- PUT /api/personas/<id>/ : Actualiza una persona
- DELETE /api/personas/<id>/ : Elimina una persona
"""
# --- Registro ---
"""
Endpoints para Registro:
- GET /api/registros/ : Lista todos los registros
- POST /api/registros/ : Crea un nuevo registro
- GET /api/registros/<id>/ : Consulta un registro por ID
- PUT /api/registros/<id>/ : Actualiza un registro
- DELETE /api/registros/<id>/ : Elimina un registro
"""
# Vistas DRF para todos los modelos principales
from rest_framework import viewsets
from .models import Departamento, Ciudad, Lugar, Mesa, Persona, Registro
from .serializers import (
	DepartamentoSerializer, CiudadSerializer, LugarSerializer,
	MesaSerializer, PersonaSerializer, RegistroSerializer
)

# ViewSets para CRUD completo de cada modelo
class DepartamentoViewSet(viewsets.ModelViewSet):
	queryset = Departamento.objects.all()
	serializer_class = DepartamentoSerializer

class CiudadViewSet(viewsets.ModelViewSet):
	queryset = Ciudad.objects.all()
	serializer_class = CiudadSerializer


class LugarViewSet(viewsets.ModelViewSet):
	queryset = Lugar.objects.all()
	serializer_class = LugarSerializer

class MesaViewSet(viewsets.ModelViewSet):
	queryset = Mesa.objects.all()
	serializer_class = MesaSerializer


from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class PersonaViewSet(viewsets.ModelViewSet):
	queryset = Persona.objects.all()
	serializer_class = PersonaSerializer

class RegistroViewSet(viewsets.ModelViewSet):
	queryset = Registro.objects.all()
	serializer_class = RegistroSerializer


