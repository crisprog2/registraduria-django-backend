
# Rutas de la API para los modelos principales de la aplicación core.
# Cada ruta expone endpoints CRUD para los modelos Departamento, Ciudad, Lugarvoto, Persona y Registro.

from rest_framework.routers import DefaultRouter
from .views import DepartamentoViewSet, CiudadViewSet, LugarvotoViewSet, PersonaViewSet, RegistroViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet, basename='departamento')
router.register(r'ciudades', CiudadViewSet, basename='ciudad')
router.register(r'lugaresvoto', LugarvotoViewSet, basename='lugarvoto')
router.register(r'personas', PersonaViewSet, basename='persona')
router.register(r'registros', RegistroViewSet, basename='registro')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')


urlpatterns = router.urls
