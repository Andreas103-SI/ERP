import csv
from django.http import HttpResponse
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

    def render_to_response(self, context, **response_kwargs):
        if 'export' in self.request.GET:
            # Exportar a CSV
            queryset = self.get_queryset()
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="reporte_ingresos_egresos.csv"'

            writer = csv.writer(response)
            writer.writerow(['Mes', 'Tipo', 'Total'])  # Encabezados

            for item in queryset:
                writer.writerow([
                    item['mes'].strftime('%Y-%m'),
                    item['tipo'],
                    item['total']
                ])

            return response
        return super().render_to_response(context, **response_kwargs)

# Reporte de Ventas por Cliente
class VentasPorClienteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cliente_id = request.GET.get('cliente_id', '')
        fecha_inicio = request.GET.get('fecha_inicio', '')
        fecha_fin = request.GET.get('fecha_fin', '')

        queryset = Venta.objects.all()
        if cliente_id:
            queryset = queryset.filter(cliente__id_cliente=cliente_id)
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
            queryset = queryset.filter(cliente__id_cliente=cliente_id)
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
        context['clientes'] = Venta.objects.values('cliente__id_cliente', 'cliente__nombre', 'cliente__apellido').distinct()
        context['cliente_id'] = self.request.GET.get('cliente_id', '')
        context['fecha_inicio'] = self.request.GET.get('fecha_inicio', '')
        context['fecha_fin'] = self.request.GET.get('fecha_fin', '')
        return context

    def render_to_response(self, context, **response_kwargs):
        if 'export' in self.request.GET:
            # Exportar a CSV
            queryset = self.get_queryset()
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="reporte_ventas_cliente.csv"'

            writer = csv.writer(response)
            writer.writerow(['Cliente', 'Total Valor', 'Total IVA', 'Total Ventas'])  # Encabezados

            for item in queryset:
                cliente_nombre = f"{item['cliente__nombre']} {item['cliente__apellido']}"
                writer.writerow([
                    cliente_nombre,
                    item['total_valor'],
                    item['total_iva'],
                    item['total_ventas']
                ])

            return response
        return super().render_to_response(context, **response_kwargs)

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
            queryset = queryset.filter(proveedor__id_proveedor=proveedor_id)
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
            queryset = queryset.filter(proveedor__id_proveedor=proveedor_id)
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
        context['proveedores'] = Pedido.objects.values('proveedor__id_proveedor', 'proveedor__nombre').distinct()
        context['estados'] = [choice[0] for choice in Pedido._meta.get_field('estado').choices]
        context['proveedor_id'] = self.request.GET.get('proveedor_id', '')
        context['estado'] = self.request.GET.get('estado', '')
        context['fecha_inicio'] = self.request.GET.get('fecha_inicio', '')
        context['fecha_fin'] = self.request.GET.get('fecha_fin', '')
        return context

    def render_to_response(self, context, **response_kwargs):
        if 'export' in self.request.GET:
            # Exportar a CSV
            queryset = self.get_queryset()
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="reporte_pedidos_proveedor.csv"'

            writer = csv.writer(response)
            writer.writerow(['Proveedor', 'Total Pedidos', 'Total Valor', 'Total IVA', 'Total'])  # Encabezados

            for item in queryset:
                writer.writerow([
                    item['proveedor__nombre'],
                    item['total_pedidos'],
                    item['total_valor'],
                    item['total_iva'],
                    item['total']
                ])

            return response
        return super().render_to_response(context, **response_kwargs)

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

    def render_to_response(self, context, **response_kwargs):
        if 'export' in self.request.GET:
            # Exportar a CSV
            queryset = self.get_queryset()
            productos = self.get_context_data()['productos']

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="reporte_inventario.csv"'

            writer = csv.writer(response)
            # Exportar Inventario
            writer.writerow(['--- Inventario ---'])
            writer.writerow(['Tipo', 'Producto', 'Vehículo', 'Cantidad Total'])
            for item in queryset:
                vehiculo = f"{item['vehiculo__marca'] or ''} {item['vehiculo__modelo'] or ''}".strip() or '-'
                writer.writerow([
                    item['tipo'],
                    item['nombre_producto'] or '-',
                    vehiculo,
                    item['total_cantidad']
                ])

            # Exportar Productos
            writer.writerow([])  # Línea en blanco
            writer.writerow(['--- Productos ---'])
            writer.writerow(['Nombre', 'Stock', 'Stock Mínimo', 'Estado'])
            for producto in productos:
                estado = 'Stock Bajo' if producto.stock < producto.stock_minimo else 'Stock Suficiente'
                writer.writerow([
                    producto.nombre,
                    producto.stock,
                    producto.stock_minimo,
                    estado
                ])

            return response
        return super().render_to_response(context, **response_kwargs)

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

    def render_to_response(self, context, **response_kwargs):
        if 'export' in self.request.GET:
            # Exportar a CSV
            queryset = self.get_queryset()
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="reporte_gastos_categoria.csv"'

            writer = csv.writer(response)
            writer.writerow(['Categoría', 'Total Monto'])  # Encabezados

            for item in queryset:
                writer.writerow([
                    item['categoria'],
                    item['total_monto']
                ])

            return response
        return super().render_to_response(context, **response_kwargs)

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

    def render_to_response(self, context, **response_kwargs):
        if 'export' in self.request.GET:
            # Exportar a CSV
            queryset = self.get_queryset()
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="reporte_empleados.csv"'

            writer = csv.writer(response)
            writer.writerow(['Puesto', 'Total Empleados', 'Total Salario'])  # Encabezados

            for item in queryset:
                writer.writerow([
                    item['puesto'],
                    item['total_empleados'],
                    item['total_salario']
                ])

            return response
        return super().render_to_response(context, **response_kwargs)

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

    if 'export' in request.GET:
        # Exportar a CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="reporte_ventas_por_mes.csv"'

        writer = csv.writer(response)
        writer.writerow(['Mes', 'Total Ventas'])  # Encabezados

        for venta in ventas:
            writer.writerow([
                venta['mes'].strftime('%Y-%m'),
                venta['total']
            ])

        return response

    return render(request, 'reportes/reporte_ventas.html', {'ventas': ventas})