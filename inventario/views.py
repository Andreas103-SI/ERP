# inventario/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Vehiculo
from .forms import VehiculoForm
from .serializers import VehiculoSerializer
from django.db.models import Q

@login_required
def vehiculo_list(request):
    vehiculos = Vehiculo.objects.all()
    search_query = request.GET.get('search', '')
    marca = request.GET.get('marca', '')
    disponibilidad = request.GET.get('disponibilidad', '')
    if search_query:
        vehiculos = vehiculos.filter(
            Q(marca__icontains=search_query) |
            Q(modelo__icontains=search_query) |
            Q(caracteristicas__icontains=search_query)
        )
    if marca:
        vehiculos = vehiculos.filter(marca__iexact=marca)
    if disponibilidad:
        vehiculos = vehiculos.filter(disponibilidad=disponibilidad)
    marcas = Vehiculo.objects.values_list('marca', flat=True).distinct()
    return render(request, 'inventario/vehiculo_list.html', {
        'vehiculos': vehiculos,
        'search_query': search_query,
        'marca': marca,
        'disponibilidad': disponibilidad,
        'marcas': marcas
    })

@login_required
def vehiculo_create(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario:vehiculo_list')
    else:
        form = VehiculoForm()
    return render(request, 'inventario/vehiculo_form.html', {'form': form})

@login_required
def vehiculo_update(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('inventario:vehiculo_list')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'inventario/vehiculo_form.html', {'form': form})

@login_required
def vehiculo_delete(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('inventario:vehiculo_list')
    return render(request, 'inventario/vehiculo_confirm_delete.html', {'vehiculo': vehiculo})

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['marca', 'modelo', 'anio', 'estado', 'disponibilidad']
    search_fields = ['marca', 'modelo', 'caracteristicas', 'datos_propietario_anterior']
    ordering_fields = ['id', 'marca', 'modelo', 'anio', 'precio']