# core/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ventas.models import Cliente, Venta
from inventario.models import Vehiculo
from empleados.models import Empleado
from pedidos.models import Pedido, Proveedor
from finanzas.models import Finanzas, Gasto
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

@login_required
def home(request):
    # Estadísticas básicas
    total_clientes = Cliente.objects.count()
    total_ventas = Venta.objects.count()
    total_vehiculos = Vehiculo.objects.count()
    total_empleados = Empleado.objects.count()
    total_pedidos = Pedido.objects.count()
    total_proveedores = Proveedor.objects.count()
    total_transacciones = Finanzas.objects.count()
    total_gastos = Gasto.objects.count()

    context = {
        'total_clientes': total_clientes,
        'total_ventas': total_ventas,
        'total_vehiculos': total_vehiculos,
        'total_empleados': total_empleados,
        'total_pedidos': total_pedidos,
        'total_proveedores': total_proveedores,
        'total_transacciones': total_transacciones,
        'total_gastos': total_gastos,
    }
    return render(request, 'core/home.html', context)

def custom_logout(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('login')