from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, VentaViewSet, VentaVehiculoViewSet, cliente_list

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'venta-vehiculos', VentaVehiculoViewSet)

app_name = 'ventas'  # Define el namespace para las URLs

urlpatterns = [
    path('api/', include(router.urls)),  # URLs de la API
    path('clientes/', cliente_list, name='cliente_list'),  # Vista basada en plantillas
]
