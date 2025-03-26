# empleados/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EmpleadoListView,
    EmpleadoCreateView,
    EmpleadoUpdateView,
    EmpleadoDeleteView,
    EmpleadoViewSet,
)

app_name = 'empleados'

# Configurar el router para la API
router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet)

urlpatterns = [
    path('', EmpleadoListView.as_view(), name='empleado_list'),
    path('create/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('update/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('delete/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado_delete'),
    path('api/', include(router.urls)),
]