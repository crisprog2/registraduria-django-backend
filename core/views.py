from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
"""
Vistas y endpoints de la API para los modelos principales.
Incluye ViewSets para CRUD y acciones personalizadas.
"""
from rest_framework import viewsets
from .models import Departamento, Ciudad, Lugar, Mesa, Persona, Registro
from .serializers import (
	DepartamentoSerializer, CiudadSerializer, LugarSerializer,
	MesaSerializer, PersonaSerializer, RegistroSerializer
)

# ViewSets para CRUD completo de cada modelo
class DepartamentoViewSet(viewsets.ModelViewSet):
	"""
	ViewSet para el modelo Departamento.
	Permite operaciones CRUD sobre departamentos.
	"""
	queryset = Departamento.objects.all()
	serializer_class = DepartamentoSerializer

class CiudadViewSet(viewsets.ModelViewSet):
	"""
	ViewSet para el modelo Ciudad.
	Permite operaciones CRUD sobre ciudades.
	"""
	queryset = Ciudad.objects.all()
	serializer_class = CiudadSerializer


class LugarViewSet(viewsets.ModelViewSet):
	"""
	ViewSet para el modelo Lugar.
	Permite operaciones CRUD sobre lugares de votación.
	"""
	queryset = Lugar.objects.all()
	serializer_class = LugarSerializer

class MesaViewSet(viewsets.ModelViewSet):
	"""
	ViewSet para el modelo Mesa.
	Permite operaciones CRUD sobre mesas de votación.
	"""
	queryset = Mesa.objects.all()
	serializer_class = MesaSerializer


from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class PersonaViewSet(viewsets.ModelViewSet):
	"""
	ViewSet para el modelo Persona.
	Permite operaciones CRUD y búsqueda personalizada por cédula.
	"""
	queryset = Persona.objects.all()
	serializer_class = PersonaSerializer

	@swagger_auto_schema(
		manual_parameters=[
			openapi.Parameter(
				'cedula', openapi.IN_QUERY, description="Cédula de la persona", type=openapi.TYPE_INTEGER, required=True
			)
		]
	)
	@action(detail=False, methods=['get'], url_path='buscar-por-cedula')
	def buscar_por_cedula(self, request):
		"""
		Endpoint personalizado para buscar una persona por cédula y retornar información relevante:
		- Nombres y apellidos
		- Cédula, género, jurado
		- Dirección y mesa de votación
		- Ciudad y departamento
		"""
		cedula = request.query_params.get('cedula')
		if not cedula:
			return Response({'error': 'Debe proporcionar una cédula.'}, status=status.HTTP_400_BAD_REQUEST)
		try:
			persona = Persona.objects.select_related(
				'cod_Mesa',
			).get(cedula=cedula)
		except Persona.DoesNotExist:
			return Response({'error': 'Persona no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

		# Obtener lugar, ciudad y departamento a través de la mesa
		lugar = None
		ciudad = None
		departamento = None
		if persona.cod_Mesa:
			mesa = persona.cod_Mesa
			# Buscar el lugar asociado a la mesa (si existe relación)
			if hasattr(mesa, 'cod_lugar') and mesa.cod_lugar:
				lugar = mesa.cod_lugar
				if lugar.cod_Ciudad:
					ciudad = lugar.cod_Ciudad
					if ciudad.cod_Departamento:
						departamento = ciudad.cod_Departamento

		data = {
			'primer_nombre': persona.primer_Nombre,
			'segundo_nombre': persona.segundo_Nombre,
			'primer_apellido': persona.primer_Apellido,
			'segundo_apellido': persona.segundo_Apellido,
			'cedula': persona.cedula,
			'genero': persona.genero,
			'es_jurado': persona.jurado,
			'direccion_lugar_votacion': lugar.direccion if lugar else None,
			'mesa_votacion': mesa.mesa if persona.cod_Mesa else None,
			'ciudad': ciudad.ciudad if ciudad else None,
			'departamento': departamento.departamento if departamento else None,
		}
		return Response(data)

class RegistroViewSet(viewsets.ModelViewSet):
	"""
	ViewSet para el modelo Registro.
	Permite operaciones CRUD sobre registros de personas.
	"""
	queryset = Registro.objects.all()
	serializer_class = RegistroSerializer


