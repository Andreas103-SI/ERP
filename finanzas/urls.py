# finanzas/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FinanzasListView,
    FinanzasCreateView,
    FinanzasUpdateView,
    FinanzasDeleteView,
    GastoListView,
    GastoCreateView,
    GastoUpdateView,
    GastoDeleteView,
    FinanzasViewSet,
)

app_name = 'finanzas'

# Configurar el router para la API
router = DefaultRouter()
router.register(r'finanzas', FinanzasViewSet)

urlpatterns = [
    # Rutas para las vistas basadas en plantillas
    path('', FinanzasListView.as_view(), name='finanzas_list'),
    path('create/', FinanzasCreateView.as_view(), name='finanzas_create'),
    path('update/<int:pk>/', FinanzasUpdateView.as_view(), name='finanzas_update'),
    path('delete/<int:pk>/', FinanzasDeleteView.as_view(), name='finanzas_delete'),
    path('gastos/', GastoListView.as_view(), name='gasto_list'),
    path('gastos/create/', GastoCreateView.as_view(), name='gasto_create'),
    path('gastos/update/<int:pk>/', GastoUpdateView.as_view(), name='gasto_update'),
    path('gastos/delete/<int:pk>/', GastoDeleteView.as_view(), name='gasto_delete'),

    # Rutas para la API
    path('api/', include(router.urls)),
]