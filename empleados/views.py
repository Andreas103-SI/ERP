# empleados/views.py
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Empleado
from .forms import EmpleadoForm
from .serializers import EmpleadoSerializer

def empleado_list(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/empleado_list.html', {'empleados': empleados})

def empleado_create(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados:empleado_list')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/empleado_form.html', {'form': form})

def empleado_update(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleados:empleado_list')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleados/empleado_form.html', {'form': form})

def empleado_delete(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleados:empleado_list')
    return render(request, 'empleados/empleado_confirm_delete.html', {'empleado': empleado})

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer