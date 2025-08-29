from rest_framework import serializers
from .models import Departamento, Ciudad, Lugarvoto, Persona, Registro, Usuario

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['DepartamentoId', 'DepartamentoNombre']

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ['CiudadId', 'CiudadNombre', 'Departamento']

class LugarvotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugarvoto
        fields = ['LugarId', 'DireccionVoto', 'MesaVoto', 'Ciudad']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['UsuarioId', 'Usuario', 'Password']

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['PersonaId', 'PersonaNombre', 'PersonaApellido', 'PersonaGenero', 'PersonaFechaN', 'PersonaJurado', 'Lugar', 'Usuario']

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ['RegistrosId', 'DocId', 'Persona']
