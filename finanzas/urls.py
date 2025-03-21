from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FinanzasViewSet

router = DefaultRouter()
router.register(r'finanzas', FinanzasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]