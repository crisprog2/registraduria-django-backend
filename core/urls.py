
# Rutas de la API para los modelos principales de la aplicación core.
# Cada ruta expone endpoints CRUD para los modelos Departamento, Ciudad, Lugarvoto, Persona y Registro.
from django.urls import path
from .views import (
    departamentos_list, departamento_detail,
    ciudades_list, ciudad_detail,
    lugaresvoto_list, lugarvoto_detail,
    personas_list, persona_detail,
    registros_list, registro_detail
)

urlpatterns = [
    # Endpoints para Departamento
    path('departamentos/', departamentos_list, name='departamentos-list'),
    path('departamentos/<int:id>/', departamento_detail, name='departamento-detail'),

    # Endpoints para Ciudad
    path('ciudades/', ciudades_list, name='ciudades-list'),
    path('ciudades/<int:id>/', ciudad_detail, name='ciudad-detail'),

    # Endpoints para Lugarvoto
    path('lugaresvoto/', lugaresvoto_list, name='lugaresvoto-list'),
    path('lugaresvoto/<int:id>/', lugarvoto_detail, name='lugarvoto-detail'),

    # Endpoints para Persona
    path('personas/', personas_list, name='personas-list'),
    path('personas/<int:id>/', persona_detail, name='persona-detail'),

    # Endpoints para Registro
    path('registros/', registros_list, name='registros-list'),
    path('registros/<int:id>/', registro_detail, name='registro-detail'),
]
