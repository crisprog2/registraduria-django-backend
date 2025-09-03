

"""
Configuración de URLs principal para el proyecto Registraduría.

Incluye rutas para:
    - Admin de Django
    - API REST (core)
    - Documentación Swagger y Redoc
    - Cualquier otra app futura
"""



from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Configuración para que Swagger acepte JWT (Bearer)
from drf_yasg import openapi
from drf_yasg import app_settings as yasg_settings

yasg_settings.swagger_settings.SECURITY_DEFINITIONS = {
    'Bearer': {
        'type': 'apiKey',
        'name': 'Authorization',
        'in': 'header',
        'description': 'JWT Authorization header using the Bearer scheme. Ejemplo: "Bearer {token}"',
        'x-example': 'Bearer <tu_token_jwt>'
    }
}

schema_view = get_schema_view(
    openapi.Info(
        title="Registraduría API",
        default_version='v1',
        description="Documentación de la API de Registraduría",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
