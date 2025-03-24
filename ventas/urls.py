# ventas/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClienteViewSet, VentaViewSet, VentaVehiculoViewSet,
    cliente_list, cliente_create, cliente_update, cliente_delete,
    venta_list, venta_create, venta_update, venta_delete,
    ventavehiculo_list, ventavehiculo_create, ventavehiculo_update, ventavehiculo_delete
)

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'venta-vehiculos', VentaVehiculoViewSet)

app_name = 'ventas'

urlpatterns = [
    # URLs de la API REST
    path('api/', include(router.urls)),

    # URLs para vistas basadas en plantillas - Clientes
    path('clientes/', cliente_list, name='cliente_list'),
    path('clientes/create/', cliente_create, name='cliente_create'),
    path('clientes/update/<int:pk>/', cliente_update, name='cliente_update'),
    path('clientes/delete/<int:pk>/', cliente_delete, name='cliente_delete'),

    # URLs para vistas basadas en plantillas - Ventas
    path('ventas/', venta_list, name='venta_list'),
    path('ventas/create/', venta_create, name='venta_create'),
    path('ventas/update/<int:pk>/', venta_update, name='venta_update'),
    path('ventas/delete/<int:pk>/', venta_delete, name='venta_delete'),

    # URLs para vistas basadas en plantillas - VentaVehiculo
    path('venta-vehiculos/', ventavehiculo_list, name='ventavehiculo_list'),
    path('venta-vehiculos/create/', ventavehiculo_create, name='ventavehiculo_create'),
    path('venta-vehiculos/update/<int:pk>/', ventavehiculo_update, name='ventavehiculo_update'),
    path('venta-vehiculos/delete/<int:pk>/', ventavehiculo_delete, name='ventavehiculo_delete'),
]