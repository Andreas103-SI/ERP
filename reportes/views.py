from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count, Q
from django.db.models.functions import TruncMonth
from finanzas.models import Finanzas, Gasto
from ventas.models import Venta
from pedidos.models import Pedido
from inventario.models import Inventario, Producto
from empleados.models import Empleado

# Reporte de Ingresos y Egresos por Mes 
class IngresosEgresosPorMesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        fecha_inicio = request.GET.get('fecha_inicio', '')
        fecha_fin = request.GET.get('fecha_fin', '')
        
        queryset = Finanzas.objects.all()
        if fecha_inicio:
            queryset = queryset.filter(fecha__gte=fecha_inicio)
        if fecha_fin:
            queryset = queryset.filter(fecha__lte=fecha_fin)

        ingresos_egresos = queryset.annotate(
            mes=TruncMonth('fecha')
        ).values('mes', 'tipo').annotate(
            total=Sum('total')
        ).order_by('mes')

        return Response(ingresos_egresos)

class IngresosEgresosListView(LoginRequiredMixin, ListView):
    template_name = 'reportes/reporte_ingresos_egresos.html'
    context_object_name = 'reporte'

    def get_queryset(self):
        fecha_inicio = self.request.GET.get('fecha_inicio', '')
        fecha_fin = self.request.GET.get('fecha_fin', '')

        queryset = Finanzas.objects.all()
        if fecha_inicio:
            queryset = queryset.filter(fecha__gte=fecha_inicio)
        if fecha_fin:
            queryset = queryset.filter(fecha__lte=fecha_fin)

        return queryset.annotate(
            mes=TruncMonth('fecha')
        ).values('mes', 'tipo').annotate(
            total=Sum('total')
        ).order_by('mes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fecha_inicio'] = self.request.GET.get('fecha_inicio', '')
        context['fecha_fin'] = self.request.GET.get('fecha_fin', '')
        return context

# Reporte de Ventas por Cliente
class VentasPorClienteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cliente_id = request.GET.get('cliente_id', '')
        fecha_inicio = request.GET.get('fecha_inicio', '')
        fecha_fin = request.GET.get('fecha_fin', '')

        queryset = Venta.objects.all()
        if cliente_id:
            queryset = queryset.filter(cliente__id_cliente=cliente_id)  # Cambiar cliente_id a cliente__id_cliente
        if fecha_inicio:
            queryset = queryset.filter(fecha__gte=fecha_inicio)
        if fecha_fin:
            queryset = queryset.filter(fecha__lte=fecha_fin)

        ventas = queryset.values('cliente__nombre', 'cliente__apellido').annotate(
            total_ventas=Sum('total'),
            total_iva=Sum('iva'),
            total_valor=Sum('valor_venta')
        ).order_by('cliente__nombre')

        return Response(ventas)

class VentasPorClienteListView(LoginRequiredMixin, ListView):
    template_name = 'reportes/reporte_ventas_cliente.html'
    context_object_name = 'reporte'

    def get_queryset(self):
        cliente_id = self.request.GET.get('cliente_id', '')
        fecha_inicio = self.request.GET.get('fecha_inicio', '')
        fecha_fin = self.request.GET.get('fecha_fin', '')

        queryset = Venta.objects.all()
        if cliente_id:
            queryset = queryset.filter(cliente__id_cliente=cliente_id)  # Cambiar cliente_id a cliente__id_cliente
        if fecha_inicio:
            queryset = queryset.filter(fecha__gte=fecha_inicio)
        if fecha_fin:
            queryset = queryset.filter(fecha__lte=fecha_fin)

        return queryset.values('cliente__nombre', 'cliente__apellido').annotate(
            total_ventas=Sum('total'),
            total_iva=Sum('iva'),
            total_valor=Sum('valor_venta')
        ).order_by('cliente__nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes'] = Venta.objects.values('cliente__id_cliente', 'cliente__nombre', 'cliente__apellido').distinct()  # Cambiar cliente__id a cliente__id_cliente
        context['cliente_id'] = self.request.GET.get('cliente_id', '')
        context['fecha_inicio'] = self.request.GET.get('fecha_inicio', '')
        context['fecha_fin'] = self.request.GET.get('fecha_fin', '')
        return context

# Reporte de Pedidos por Proveedor
class PedidosPorProveedorView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        proveedor_id = request.GET.get('proveedor_id', '')
        estado = request.GET.get('estado', '')
        fecha_inicio = request.GET.get('fecha_inicio', '')
        fecha_fin = request.GET.get('fecha_fin', '')

        queryset = Pedido.objects.all()
        if proveedor_id:
            queryset = queryset.filter(proveedor__id_proveedor=proveedor_id)  # Cambiar proveedor_id a proveedor__id_proveedor
        if estado:
            queryset = queryset.filter(estado=estado)
        if fecha_inicio:
            queryset = queryset.filter(fecha_pedido__gte=fecha_inicio)
        if fecha_fin:
            queryset = queryset.filter(fecha_pedido__lte=fecha_fin)

        pedidos = queryset.values('proveedor__nombre').annotate(
            total_pedidos=Count('id_pedido'),
            total_valor=Sum('valor'),
            total_iva=Sum('iva'),
            total=Sum('total')
        ).order_by('proveedor__nombre')

        return Response(pedidos)
    

class PedidosPorProveedorListView(LoginRequiredMixin, ListView):
    template_name = 'reportes/reporte_pedidos_proveedor.html'
    context_object_name = 'reporte'

    def get_queryset(self):
        proveedor_id = self.request.GET.get('proveedor_id', '')
        estado = self.request.GET.get('estado', '')
        fecha_inicio = self.request.GET.get('fecha_inicio', '')
        fecha_fin = self.request.GET.get('fecha_fin', '')

        queryset = Pedido.objects.all()
        if proveedor_id:
            queryset = queryset.filter(proveedor__id_proveedor=proveedor_id)  # Cambiar proveedor_id a proveedor__id_proveedor
        if estado:
            queryset = queryset.filter(estado=estado)
        if fecha_inicio:
            queryset = queryset.filter(fecha_pedido__gte=fecha_inicio)
        if fecha_fin:
            queryset = queryset.filter(fecha_pedido__lte=fecha_fin)

        return queryset.values('proveedor__nombre').annotate(
            total_pedidos=Count('id_pedido'),
            total_valor=Sum('valor'),
            total_iva=Sum('iva'),
            total=Sum('total')
        ).order_by('proveedor__nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proveedores'] = Pedido.objects.values('proveedor__id_proveedor', 'proveedor__nombre').distinct()  # Cambiar proveedor__id a proveedor__id_proveedor
        context['estados'] = [choice[0] for choice in Pedido._meta.get_field('estado').choices]
        context['proveedor_id'] = self.request.GET.get('proveedor_id', '')
        context['estado'] = self.request.GET.get('estado', '')
        context['fecha_inicio'] = self.request.GET.get('fecha_inicio', '')
        context['fecha_fin'] = self.request.GET.get('fecha_fin', '')
        return context
    
# Reporte de Inventario
class InventarioReporteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tipo = request.GET.get('tipo', '')

        queryset = Inventario.objects.all()
        if tipo:
            queryset = queryset.filter(tipo=tipo)

        inventario = queryset.values('tipo', 'nombre_producto', 'vehiculo__marca', 'vehiculo__modelo').annotate(
            total_cantidad=Sum('cantidad')
        ).order_by('tipo')

        productos = Producto.objects.all()
        if tipo and tipo != 'Vehículo':
            productos = productos.filter(nombre__icontains=tipo.lower())

        productos = productos.values('nombre', 'stock', 'stock_minimo')

        return Response({'inventario': inventario, 'productos': productos})

class InventarioReporteListView(LoginRequiredMixin, ListView):
    template_name = 'reportes/reporte_inventario.html'
    context_object_name = 'reporte'

    def get_queryset(self):
        tipo = self.request.GET.get('tipo', '')
        queryset = Inventario.objects.all()
        if tipo:
            queryset = queryset.filter(tipo=tipo)

        return queryset.values('tipo', 'nombre_producto', 'vehiculo__marca', 'vehiculo__modelo').annotate(
            total_cantidad=Sum('cantidad')
        ).order_by('tipo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipo = self.request.GET.get('tipo', '')
        productos = Producto.objects.all()
        if tipo and tipo != 'Vehículo':
            productos = productos.filter(nombre__icontains=tipo.lower())

        context['productos'] = productos
        context['tipos'] = [choice[0] for choice in Inventario._meta.get_field('tipo').choices]
        context['tipo'] = tipo
        return context

# Reporte de Gastos por Categoría
class GastosPorCategoriaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categoria = request.GET.get('categoria', '')
        fecha_inicio = request.GET.get('fecha_inicio', '')
        fecha_fin = request.GET.get('fecha_fin', '')

        queryset = Gasto.objects.all()
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        if fecha_inicio:
            queryset = queryset.filter(fecha__gte=fecha_inicio)
        if fecha_fin:
            queryset = queryset.filter(fecha__lte=fecha_fin)

        gastos = queryset.values('categoria').annotate(
            total_monto=Sum('monto')
        ).order_by('categoria')

        return Response(gastos)

class GastosPorCategoriaListView(LoginRequiredMixin, ListView):
    template_name = 'reportes/reporte_gastos_categoria.html'
    context_object_name = 'reporte'

    def get_queryset(self):
        categoria = self.request.GET.get('categoria', '')
        fecha_inicio = self.request.GET.get('fecha_inicio', '')
        fecha_fin = self.request.GET.get('fecha_fin', '')

        queryset = Gasto.objects.all()
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        if fecha_inicio:
            queryset = queryset.filter(fecha__gte=fecha_inicio)
        if fecha_fin:
            queryset = queryset.filter(fecha__lte=fecha_fin)

        return queryset.values('categoria').annotate(
            total_monto=Sum('monto')
        ).order_by('categoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = [choice[0] for choice in Gasto._meta.get_field('categoria').choices]
        context['categoria'] = self.request.GET.get('categoria', '')
        context['fecha_inicio'] = self.request.GET.get('fecha_inicio', '')
        context['fecha_fin'] = self.request.GET.get('fecha_fin', '')
        return context

# Reporte de Empleados
class EmpleadosReporteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        puesto = request.GET.get('puesto', '')

        queryset = Empleado.objects.all()
        if puesto:
            queryset = queryset.filter(puesto=puesto)

        empleados = queryset.values('puesto').annotate(
            total_empleados=Count('id_empleado'),
            total_salario=Sum('salario')
        ).order_by('puesto')

        return Response(empleados)

class EmpleadosReporteListView(LoginRequiredMixin, ListView):
    template_name = 'reportes/reporte_empleados.html'
    context_object_name = 'reporte'

    def get_queryset(self):
        puesto = self.request.GET.get('puesto', '')

        queryset = Empleado.objects.all()
        if puesto:
            queryset = queryset.filter(puesto=puesto)

        return queryset.values('puesto').annotate(
            total_empleados=Count('id_empleado'),
            total_salario=Sum('salario')
        ).order_by('puesto')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['puestos'] = Empleado.objects.values_list('puesto', flat=True).distinct()
        context['puesto'] = self.request.GET.get('puesto', '')
        return context

# Reporte de Ventas por Mes (Ya Existente)
class VentasPorMesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        ventas = Finanzas.objects.filter(tipo='Ingreso').annotate(
            mes=TruncMonth('fecha')
        ).values('mes').annotate(total=Sum('total')).order_by('mes')
        return Response(ventas)

@login_required
def reporte_ventas(request):
    ventas = Finanzas.objects.filter(tipo='Ingreso').annotate(
        mes=TruncMonth('fecha')
    ).values('mes').annotate(total=Sum('total')).order_by('mes')
    return render(request, 'reportes/reporte_ventas.html', {'ventas': ventas})