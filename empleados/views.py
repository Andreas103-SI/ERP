# empleados/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Empleado
from .forms import EmpleadoForm
from .serializers import EmpleadoSerializer
from django.db.models import Q

@login_required
def empleado_list(request):
    empleados = Empleado.objects.all()
    search_query = request.GET.get('search', '')
    puesto = request.GET.get('puesto', '')
    if search_query:
        empleados = empleados.filter(
            Q(nombre__icontains=search_query) |
            Q(apellido__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    if puesto:
        empleados = empleados.filter(puesto=puesto)
    puestos = Empleado.objects.values_list('puesto', flat=True).distinct()
    return render(request, 'empleados/empleado_list.html', {
        'empleados': empleados,
        'search_query': search_query,
        'puesto': puesto,
        'puestos': puestos
    })

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
    filterset_fields = ['dni', 'puesto']
    search_fields = ['nombre', 'apellido', 'email']
    ordering_fields = ['id', 'nombre', 'apellido', 'salario']