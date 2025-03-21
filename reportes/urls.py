from django.urls import path
from .views import VentasPorMesView, InventarioDisponibleView, GastosPorNominaView

urlpatterns = [
    path('ventas-por-mes/', VentasPorMesView.as_view(), name='ventas-por-mes'),
    path('inventario-disponible/', InventarioDisponibleView.as_view(), name='inventario-disponible'),
    path('gastos-por-nomina/', GastosPorNominaView.as_view(), name='gastos-por-nomina'),
]