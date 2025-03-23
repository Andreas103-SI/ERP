from django.urls import path
from .views import VentasPorMesView, reporte_ventas

app_name = 'reportes'  # Define el namespace para las URLs

urlpatterns = [
    path('api/ventas-por-mes/', VentasPorMesView.as_view(), name='ventas-por-mes'),
    path('ventas-por-mes/', reporte_ventas, name='reporte_ventas'),  # Vista basada en plantillas
]