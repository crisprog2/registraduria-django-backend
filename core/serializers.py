
from rest_framework import serializers
from .models import Departamento, Ciudad, Lugar, Mesa, Persona, Registro

class DepartamentoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Departamento.
    """
    class Meta:
        model = Departamento
        fields = '__all__'

class CiudadSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Ciudad.
    """
    class Meta:
        model = Ciudad
        fields = '__all__'

class LugarSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Lugar de Votación.
    """
    class Meta:
        model = Lugar
        fields = '__all__'


class MesaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Mesa de Votación.
    """
    class Meta:
        model = Mesa
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Persona.
    """
    class Meta:
        model = Persona
        fields = '__all__'

class RegistroSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Registro.
    """
    class Meta:
        model = Registro
        fields = '__all__'
