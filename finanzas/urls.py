# finanzas/urls.py
from django.urls import path
from .views import (
    FinanzasListView,
    FinanzasCreateView,
    FinanzasUpdateView,
    FinanzasDeleteView,
    GastoListView,
    GastoCreateView,
    GastoUpdateView,
    GastoDeleteView,
)

app_name = 'finanzas'

urlpatterns = [
    # Rutas para Finanzas
    path('', FinanzasListView.as_view(), name='finanzas_list'),
    path('create/', FinanzasCreateView.as_view(), name='finanzas_create'),
    path('update/<int:pk>/', FinanzasUpdateView.as_view(), name='finanzas_update'),
    path('delete/<int:pk>/', FinanzasDeleteView.as_view(), name='finanzas_delete'),

    # Rutas para Gastos
    path('gastos/', GastoListView.as_view(), name='gasto_list'),
    path('gastos/create/', GastoCreateView.as_view(), name='gasto_create'),
    path('gastos/update/<int:pk>/', GastoUpdateView.as_view(), name='gasto_update'),
    path('gastos/delete/<int:pk>/', GastoDeleteView.as_view(), name='gasto_delete'),
]