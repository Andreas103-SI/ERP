# finanzas/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Finanzas, Gasto
from .forms import FinanzasForm, GastoForm
from .serializers import FinanzasSerializer, GastoSerializer

@login_required
def finanzas_list(request):
    finanzas = Finanzas.objects.all()
    return render(request, 'finanzas/finanzas_list.html', {'finanzas': finanzas})

@login_required
def finanzas_create(request):
    if request.method == 'POST':
        form = FinanzasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finanzas:finanzas_list')
    else:
        form = FinanzasForm()
    return render(request, 'finanzas/finanzas_form.html', {'form': form})

@login_required
def finanzas_update(request, pk):
    finanzas = get_object_or_404(Finanzas, pk=pk)
    if request.method == 'POST':
        form = FinanzasForm(request.POST, instance=finanzas)
        if form.is_valid():
            form.save()
            return redirect('finanzas:finanzas_list')
    else:
        form = FinanzasForm(instance=finanzas)
    return render(request, 'finanzas/finanzas_form.html', {'form': form})

@login_required
def finanzas_delete(request, pk):
    finanzas = get_object_or_404(Finanzas, pk=pk)
    if request.method == 'POST':
        finanzas.delete()
        return redirect('finanzas:finanzas_list')
    return render(request, 'finanzas/finanzas_confirm_delete.html', {'finanzas': finanzas})

@login_required
def gasto_list(request):
    gastos = Gasto.objects.all()
    return render(request, 'finanzas/gasto_list.html', {'gastos': gastos})

@login_required
def gasto_create(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finanzas:gasto_list')
    else:
        form = GastoForm()
    return render(request, 'finanzas/gasto_form.html', {'form': form})

@login_required
def gasto_update(request, pk):
    gasto = get_object_or_404(Gasto, pk=pk)
    if request.method == 'POST':
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('finanzas:gasto_list')
    else:
        form = GastoForm(instance=gasto)
    return render(request, 'finanzas/gasto_form.html', {'form': form})

@login_required
def gasto_delete(request, pk):
    gasto = get_object_or_404(Gasto, pk=pk)
    if request.method == 'POST':
        gasto.delete()
        return redirect('finanzas:gasto_list')
    return render(request, 'finanzas/gasto_confirm_delete.html', {'gasto': gasto})

class FinanzasViewSet(viewsets.ModelViewSet):
    queryset = Finanzas.objects.all()
    serializer_class = FinanzasSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['tipo', 'venta', 'pedido', 'empleado', 'fecha']  # Filtrar por tipo, venta, pedido, empleado o fecha
    search_fields = ['descripcion']  # Buscar por descripción
    ordering_fields = ['id_finanzas', 'fecha', 'valor', 'total']  # Ordenar por ID, fecha, valor o total

class GastoViewSet(viewsets.ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['categoria', 'fecha']  # Filtrar por categoría o fecha
    search_fields = ['descripcion']  # Buscar por descripción
    ordering_fields = ['id', 'fecha', 'monto']  # Ordenar por ID, fecha o monto