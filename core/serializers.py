
from rest_framework import serializers
from .models import Departamento, Ciudad, Lugar, Mesa, Persona, Registro

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'

class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = '__all__'


class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = '__all__'
