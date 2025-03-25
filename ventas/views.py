# ventas/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cliente, Venta, VentaVehiculo
from .forms import ClienteForm, VentaForm, VentaVehiculoForm
from .serializers import ClienteSerializer, VentaSerializer, VentaVehiculoSerializer
from django.db.models import Q

# Vistas para Cliente
@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        clientes = clientes.filter(
            Q(nombre__icontains=search_query) |
            Q(apellido__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    return render(request, 'ventas/cliente_list.html', {'clientes': clientes, 'search_query': search_query})

@login_required
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas:cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'ventas/cliente_form.html', {'form': form})

@login_required
def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('ventas:cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'ventas/cliente_form.html', {'form': form})

@login_required
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ventas:cliente_list')
    return render(request, 'ventas/cliente_confirm_delete.html', {'cliente': cliente})

# Vistas para Venta
@login_required
def venta_list(request):
    ventas = Venta.objects.all()
    cliente_id = request.GET.get('cliente', '')
    fecha = request.GET.get('fecha', '')
    if cliente_id:
        ventas = ventas.filter(cliente__id=cliente_id)
    if fecha:
        ventas = ventas.filter(fecha=fecha)
    clientes = Cliente.objects.all()  # Para el filtro de clientes
    return render(request, 'ventas/venta_list.html', {
        'ventas': ventas,
        'clientes': clientes,
        'cliente_id': cliente_id,
        'fecha': fecha
    })

@login_required
def venta_create(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas:venta_list')
    else:
        form = VentaForm()
    return render(request, 'ventas/venta_form.html', {'form': form})

@login_required
def venta_update(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('ventas:venta_list')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'ventas/venta_form.html', {'form': form})

@login_required
def venta_delete(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('ventas:venta_list')
    return render(request, 'ventas/venta_confirm_delete.html', {'venta': venta})

# Vistas para VentaVehiculo
@login_required
def ventavehiculo_list(request):
    ventavehiculos = VentaVehiculo.objects.all()
    venta_id = request.GET.get('venta', '')
    if venta_id:
        ventavehiculos = ventavehiculos.filter(venta__id=venta_id)
    ventas = Venta.objects.all()  # Para el filtro de ventas
    return render(request, 'ventas/ventavehiculo_list.html', {
        'ventavehiculos': ventavehiculos,
        'ventas': ventas,
        'venta_id': venta_id
    })

@login_required
def ventavehiculo_create(request):
    if request.method == 'POST':
        form = VentaVehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas:ventavehiculo_list')
    else:
        form = VentaVehiculoForm()
    return render(request, 'ventas/ventavehiculo_form.html', {'form': form})

@login_required
def ventavehiculo_update(request, pk):
    ventavehiculo = get_object_or_404(VentaVehiculo, pk=pk)
    if request.method == 'POST':
        form = VentaVehiculoForm(request.POST, instance=ventavehiculo)
        if form.is_valid():
            form.save()
            return redirect('ventas:ventavehiculo_list')
    else:
        form = VentaVehiculoForm(instance=ventavehiculo)
    return render(request, 'ventas/ventavehiculo_form.html', {'form': form})

@login_required
def ventavehiculo_delete(request, pk):
    ventavehiculo = get_object_or_404(VentaVehiculo, pk=pk)
    if request.method == 'POST':
        ventavehiculo.delete()
        return redirect('ventas:ventavehiculo_list')
    return render(request, 'ventas/ventavehiculo_confirm_delete.html', {'ventavehiculo': ventavehiculo})

# ViewSets para la API (ya configurados anteriormente)
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['dni_pasaporte', 'email']
    search_fields = ['nombre', 'apellido', 'email']
    ordering_fields = ['id_cliente', 'nombre', 'apellido']

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['cliente', 'fecha']
    search_fields = ['contrato']
    ordering_fields = ['id_venta', 'fecha', 'total']

class VentaVehiculoViewSet(viewsets.ModelViewSet):
    queryset = VentaVehiculo.objects.all()
    serializer_class = VentaVehiculoSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['venta', 'vehiculo']
    search_fields = []
    ordering_fields = ['venta', 'vehiculo']