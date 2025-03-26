from django.urls import path
from . import views

app_name = 'reportes'

urlpatterns = [
    # Vistas renderizadas
    path('ventas/', views.reporte_ventas, name='reporte_ventas'),
    path('ingresos-egresos/', views.IngresosEgresosListView.as_view(), name='reporte_ingresos_egresos'),
    path('ventas-cliente/', views.VentasPorClienteListView.as_view(), name='reporte_ventas_cliente'),
    path('pedidos-proveedor/', views.PedidosPorProveedorListView.as_view(), name='reporte_pedidos_proveedor'),
    path('inventario/', views.InventarioReporteListView.as_view(), name='reporte_inventario'),
    path('gastos-categoria/', views.GastosPorCategoriaListView.as_view(), name='reporte_gastos_categoria'),
    path('empleados/', views.EmpleadosReporteListView.as_view(), name='reporte_empleados'),
    # Vistas API
    path('api/ventas-por-mes/', views.VentasPorMesView.as_view(), name='api_ventas_por_mes'),
    path('api/ingresos-egresos/', views.IngresosEgresosPorMesView.as_view(), name='api_ingresos_egresos'),
    path('api/ventas-cliente/', views.VentasPorClienteView.as_view(), name='api_ventas_cliente'),
    path('api/pedidos-proveedor/', views.PedidosPorProveedorView.as_view(), name='api_pedidos_proveedor'),
    path('api/inventario/', views.InventarioReporteView.as_view(), name='api_inventario'),
    path('api/gastos-categoria/', views.GastosPorCategoriaView.as_view(), name='api_gastos_categoria'),
    path('api/empleados/', views.EmpleadosReporteView.as_view(), name='api_empleados'),
]