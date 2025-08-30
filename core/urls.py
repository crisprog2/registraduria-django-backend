

# Rutas de la API para los modelos principales de la aplicación core.
# Cada ruta expone endpoints CRUD para los modelos Departamento, Ciudad, Lugar, Mesa, Persona y Registro.
# Las rutas se registran automáticamente usando DefaultRouter de DRF.

from rest_framework.routers import DefaultRouter
from .views import DepartamentoViewSet, CiudadViewSet, LugarViewSet, MesaViewSet, PersonaViewSet, RegistroViewSet



router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet, basename='departamento')
router.register(r'ciudades', CiudadViewSet, basename='ciudad')
router.register(r'lugares', LugarViewSet, basename='lugar')
router.register(r'mesas', MesaViewSet, basename='mesa')
router.register(r'personas', PersonaViewSet, basename='persona')
router.register(r'registros', RegistroViewSet, basename='registro')


urlpatterns = router.urls
