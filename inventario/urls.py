# inventario/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VehiculoListView,
    VehiculoCreateView,
    VehiculoUpdateView,
    VehiculoDeleteView,
    VehiculoViewSet,  # Lo definiremos en views.py
)

app_name = 'inventario'

# Configurar el router para la API
router = DefaultRouter()
router.register(r'vehiculos', VehiculoViewSet)

urlpatterns = [
    # URLs para las vistas basadas en plantillas
    path('', VehiculoListView.as_view(), name='vehiculo_list'),
    path('create/', VehiculoCreateView.as_view(), name='vehiculo_create'),
    path('update/<int:pk>/', VehiculoUpdateView.as_view(), name='vehiculo_update'),
    path('delete/<int:pk>/', VehiculoDeleteView.as_view(), name='vehiculo_delete'),

    # URLs de la API REST
    path('api/', include(router.urls)),
]