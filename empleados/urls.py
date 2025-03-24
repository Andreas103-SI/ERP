# empleados/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet, empleado_list, empleado_create, empleado_update, empleado_delete

router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet)

app_name = 'empleados'

urlpatterns = [
    # URLs de la API REST
    path('api/', include(router.urls)),

    # URLs para vistas basadas en plantillas
    path('', empleado_list, name='empleado_list'),
    path('create/', empleado_create, name='empleado_create'),
    path('update/<int:pk>/', empleado_update, name='empleado_update'),
    path('delete/<int:pk>/', empleado_delete, name='empleado_delete'),
]