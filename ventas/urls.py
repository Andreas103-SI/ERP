
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, VentaViewSet, VentaVehiculoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'venta-vehiculos', VentaVehiculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]