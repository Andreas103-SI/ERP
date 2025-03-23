from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet, empleado_list

router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet)

app_name = 'empleados'  # Define el namespace para las URLs

urlpatterns = [
    path('api/', include(router.urls)),  # URLs de la API
    path('empleados/', empleado_list, name='empleado_list'),  # Vista basada en plantillas
]