# proveedores/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProveedorListView,
    ProveedorCreateView,
    ProveedorUpdateView,
    ProveedorDeleteView,
    ProveedorViewSet,
)

app_name = 'proveedores'

# Configurar el router para la API
router = DefaultRouter()
router.register(r'proveedores', ProveedorViewSet)

urlpatterns = [
    path('', ProveedorListView.as_view(), name='proveedor_list'),
    path('create/', ProveedorCreateView.as_view(), name='proveedor_create'),
    path('update/<int:pk>/', ProveedorUpdateView.as_view(), name='proveedor_update'),
    path('delete/<int:pk>/', ProveedorDeleteView.as_view(), name='proveedor_delete'),
    path('api/', include(router.urls)),
]