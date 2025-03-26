# ventas/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClienteListView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
    ClienteViewSet,
    VentaViewSet,
    VentaVehiculoViewSet,
)

app_name = 'ventas'

# Configurar el router para la API
router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'venta-vehiculos', VentaVehiculoViewSet)

urlpatterns = [
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/create/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/update/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/delete/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
    path('api/', include(router.urls)),
]