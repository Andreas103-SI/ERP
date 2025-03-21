from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProveedorViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r'proveedores', ProveedorViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]