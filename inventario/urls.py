# inventario/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehiculoViewSet, vehiculo_list, vehiculo_create, vehiculo_update, vehiculo_delete

router = DefaultRouter()
router.register(r'vehiculos', VehiculoViewSet)  # Mantenemos solo VehiculoViewSet

app_name = 'inventario'  # Define el namespace para las URLs

urlpatterns = [
    # URLs de la API REST
    path('api/', include(router.urls)),

    # URLs para vistas basadas en plantillas
    path('', vehiculo_list, name='vehiculo_list'),  # Cambiamos 'vehiculos/' a '' para que sea la raíz
    path('create/', vehiculo_create, name='vehiculo_create'),
    path('update/<int:pk>/', vehiculo_update, name='vehiculo_update'),
    path('delete/<int:pk>/', vehiculo_delete, name='vehiculo_delete'),
]