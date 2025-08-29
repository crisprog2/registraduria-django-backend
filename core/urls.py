from django.urls import path
from .views import departamentos_list, departamento_detail

urlpatterns = [
    path('departamentos/', departamentos_list, name='departamentos-list'),
    path('departamentos/<int:id>/', departamento_detail, name='departamento-detail'),
]
