
from rest_framework import serializers
from .models import Departamento, Ciudad, Lugar, Mesa, Persona, Registro

class DepartamentoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Departamento.
    Convierte instancias de Departamento a JSON y viceversa.
    """
    class Meta:
        model = Departamento
        fields = '__all__'

class CiudadSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Ciudad.
    Devuelve el nombre del departamento en vez del código.
    Facilita la visualización de la relación ciudad-departamento.
    """
    departamento = serializers.SerializerMethodField()

    class Meta:
        model = Ciudad
        fields = ['cod_Ciudad', 'ciudad', 'departamento']

    def get_departamento(self, obj):
        return obj.cod_Departamento.departamento if obj.cod_Departamento else None

class LugarSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Lugar de Votación.
    Devuelve el nombre de la ciudad asociada.
    Facilita la visualización de la relación lugar-ciudad.
    """
    ciudad = serializers.SerializerMethodField()

    class Meta:
        model = Lugar
        fields = ['cod_lugar', 'nombre_lugar', 'direccion', 'ciudad']

    def get_ciudad(self, obj):
        return obj.cod_Ciudad.ciudad if obj.cod_Ciudad else None


class MesaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Mesa de Votación.
    Devuelve el nombre del lugar asociado.
    Facilita la visualización de la relación mesa-lugar.
    """
    lugar = serializers.SerializerMethodField()

    class Meta:
        model = Mesa
        fields = ['cod_Mesa', 'mesa', 'lugar']

    def get_lugar(self, obj):
        return obj.cod_lugar.nombre_lugar if obj.cod_lugar else None

class PersonaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Persona.
    Serializa los datos básicos de la persona, sin relaciones anidadas.
    """
    class Meta:
        model = Persona
        fields = ['cedula', 'primer_Nombre', 'segundo_Nombre', 'primer_Apellido', 'segundo_Apellido', 'genero', 'edad', 'jurado']

class RegistroSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Registro.
    Serializa el código, número de registros y la cédula asociada.
    """
    class Meta:
        model = Registro
        fields = ['cod_Registro', 'registro', 'cedula']
