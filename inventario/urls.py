from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehiculoViewSet, InventarioViewSet

router = DefaultRouter()
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'inventarios', InventarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]