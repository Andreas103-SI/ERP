# inventario/views.py
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Vehiculo
from .forms import VehiculoForm
from .serializers import VehiculoSerializer

def vehiculo_list(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'inventario/vehiculo_list.html', {'vehiculos': vehiculos})

def vehiculo_create(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario:vehiculo_list')
    else:
        form = VehiculoForm()
    return render(request, 'inventario/vehiculo_form.html', {'form': form})

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

def vehiculo_delete(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('inventario:vehiculo_list')
    return render(request, 'inventario/vehiculo_confirm_delete.html', {'vehiculo': vehiculo})

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer