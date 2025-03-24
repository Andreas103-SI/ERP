# ventas/views.py
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Cliente, Venta, VentaVehiculo
from .forms import ClienteForm, VentaForm, VentaVehiculoForm
from .serializers import ClienteSerializer, VentaSerializer, VentaVehiculoSerializer

# Vistas para Cliente
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'ventas/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas:cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'ventas/cliente_form.html', {'form': form})

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

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ventas:cliente_list')
    return render(request, 'ventas/cliente_confirm_delete.html', {'cliente': cliente})

# Vistas para Venta
def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/venta_list.html', {'ventas': ventas})

def venta_create(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas:venta_list')
    else:
        form = VentaForm()
    return render(request, 'ventas/venta_form.html', {'form': form})

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

def venta_delete(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('ventas:venta_list')
    return render(request, 'ventas/venta_confirm_delete.html', {'venta': venta})

# Vistas para VentaVehiculo
def ventavehiculo_list(request):
    ventavehiculos = VentaVehiculo.objects.all()
    return render(request, 'ventas/ventavehiculo_list.html', {'ventavehiculos': ventavehiculos})

def ventavehiculo_create(request):
    if request.method == 'POST':
        form = VentaVehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas:ventavehiculo_list')
    else:
        form = VentaVehiculoForm()
    return render(request, 'ventas/ventavehiculo_form.html', {'form': form})

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

def ventavehiculo_delete(request, pk):
    ventavehiculo = get_object_or_404(VentaVehiculo, pk=pk)
    if request.method == 'POST':
        ventavehiculo.delete()
        return redirect('ventas:ventavehiculo_list')
    return render(request, 'ventas/ventavehiculo_confirm_delete.html', {'ventavehiculo': ventavehiculo})

# ViewSets para la API
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class VentaVehiculoViewSet(viewsets.ModelViewSet):
    queryset = VentaVehiculo.objects.all()
    serializer_class = VentaVehiculoSerializer