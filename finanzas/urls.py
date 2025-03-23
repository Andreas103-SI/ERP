from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FinanzasViewSet, finanza_list

router = DefaultRouter()
router.register(r'finanzas', FinanzasViewSet)

app_name = 'finanzas'  # Define el namespace para las URLs

urlpatterns = [
    path('api/', include(router.urls)),  # URLs de la API
    path('finanzas/', finanza_list, name='finanza_list'),  # Vista basada en plantillas
]