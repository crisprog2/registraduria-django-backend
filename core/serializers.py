
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
    Permite crear ciudades especificando el departamento (cod_Departamento).
    Devuelve el nombre del departamento en el campo 'departamento'.
    """
    departamento = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Ciudad
        fields = ['cod_Ciudad', 'ciudad', 'cod_Departamento', 'departamento']

    def get_departamento(self, obj):
        return obj.cod_Departamento.departamento if obj.cod_Departamento else None

class LugarSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Lugar de Votación.
    Permite crear lugares especificando la ciudad (cod_Ciudad).
    Devuelve el nombre de la ciudad en el campo 'ciudad'.
    """
    ciudad = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Lugar
        fields = ['cod_lugar', 'nombre_lugar', 'direccion', 'cod_Ciudad', 'ciudad']

    def get_ciudad(self, obj):
        return obj.cod_Ciudad.ciudad if obj.cod_Ciudad else None


class MesaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Mesa de Votación.
    Permite crear mesas especificando el lugar (cod_lugar).
    Devuelve el nombre del lugar en el campo 'lugar'.
    """
    lugar = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Mesa
        fields = ['cod_Mesa', 'mesa', 'cod_lugar', 'lugar']

    def get_lugar(self, obj):
        return obj.cod_lugar.nombre_lugar if obj.cod_lugar else None

class PersonaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Persona.
    Permite crear personas especificando la mesa (cod_Mesa).
    """
    class Meta:
        model = Persona
        fields = ['cedula', 'primer_Nombre', 'segundo_Nombre', 'primer_Apellido', 'segundo_Apellido', 'genero', 'edad', 'jurado', 'cod_Mesa']

class RegistroSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Registro.
    Serializa el código, número de registros y la cédula asociada.
    """
    class Meta:
        model = Registro
        fields = ['cod_Registro', 'registro', 'cedula']
