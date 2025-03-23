from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehiculoViewSet, InventarioViewSet, vehiculo_list

router = DefaultRouter()
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'inventario', InventarioViewSet)

app_name = 'inventario'  # Define el namespace para las URLs

urlpatterns = [
    path('api/', include(router.urls)),  # URLs de la API
    path('vehiculos/', vehiculo_list, name='vehiculo_list'),  # Vista basada en plantillas
]