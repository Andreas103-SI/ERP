# empleados/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Empleado
from .forms import EmpleadoForm
from .serializers import EmpleadoSerializer

@login_required
def empleado_list(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/empleado_list.html', {'empleados': empleados})

@login_required
def empleado_create(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados:empleado_list')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/empleado_form.html', {'form': form})

@login_required
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

@login_required
def empleado_delete(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleados:empleado_list')
    return render(request, 'empleados/empleado_confirm_delete.html', {'empleado': empleado})

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['dni', 'puesto']  # Filtrar por DNI o puesto
    search_fields = ['nombre', 'apellido', 'email']  # Buscar por nombre, apellido o email
    ordering_fields = ['id', 'nombre', 'apellido', 'salario']  # Ordenar por ID, nombre, apellido o salario