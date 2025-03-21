from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import datetime, timedelta
from ventas.models import Venta
from inventario.models import Producto
from empleados.models import Empleado
from finanzas.models import Gasto

class VentasPorMesView(APIView):
    def get(self, request):
        # Obtener ventas del mes actual
        mes_actual = timezone.now().month
        año_actual = timezone.now().year
        
        ventas_mes = Venta.objects.filter(
            fecha__month=mes_actual,
            fecha__year=año_actual
        ).aggregate(
            total_ventas=Sum('total'),
            cantidad_ventas=Count('id')
        )
        
        return Response({
            'mes': mes_actual,
            'año': año_actual,
            'total_ventas': ventas_mes['total_ventas'] or 0,
            'cantidad_ventas': ventas_mes['cantidad_ventas']
        })

class InventarioDisponibleView(APIView):
    def get(self, request):
        # Obtener productos con stock bajo
        stock_bajo = Producto.objects.filter(stock__lte=10)
        
        return Response({
            'productos_stock_bajo': [
                {
                    'nombre': producto.nombre,
                    'stock': producto.stock,
                    'stock_minimo': producto.stock_minimo
                }
                for producto in stock_bajo
            ]
        })

class GastosPorNominaView(APIView):
    def get(self, request):
        # Obtener gastos de nómina del mes actual
        mes_actual = timezone.now().month
        año_actual = timezone.now().year
        
        gastos_nomina = Gasto.objects.filter(
            fecha__month=mes_actual,
            fecha__year=año_actual,
            categoria='nomina'
        ).aggregate(
            total_gastos=Sum('monto')
        )
        
        return Response({
            'mes': mes_actual,
            'año': año_actual,
            'total_gastos_nomina': gastos_nomina['total_gastos'] or 0
        })

# Create your views here.
