from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, VentaViewSet, VentaVehiculoViewSet, cliente_list, cliente_create

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'venta-vehiculos', VentaVehiculoViewSet)

app_name = 'ventas'

urlpatterns = [
    path('api/', include(router.urls)),
    path('clientes/', cliente_list, name='cliente_list'),
    path('clientes/crear/', cliente_create, name='cliente_create'),
]