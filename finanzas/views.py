# finanzas/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Finanzas, Gasto
from .forms import FinanzasForm, GastoForm
from .serializers import FinanzasSerializer, GastoSerializer
from django.db.models import Q

@login_required
def finanzas_list(request):
    finanzas = Finanzas.objects.all()
    tipo = request.GET.get('tipo', '')
    fecha = request.GET.get('fecha', '')
    if tipo:
        finanzas = finanzas.filter(tipo=tipo)
    if fecha:
        finanzas = finanzas.filter(fecha=fecha)
    return render(request, 'finanzas/finanzas_list.html', {
        'finanzas': finanzas,
        'tipo': tipo,
        'fecha': fecha
    })

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
    search_query = request.GET.get('search', '')
    categoria = request.GET.get('categoria', '')
    fecha = request.GET.get('fecha', '')
    if search_query:
        gastos = gastos.filter(descripcion__icontains=search_query)
    if categoria:
        gastos = gastos.filter(categoria=categoria)
    if fecha:
        gastos = gastos.filter(fecha=fecha)
    categorias = Gasto.objects.values_list('categoria', flat=True).distinct()
    return render(request, 'finanzas/gasto_list.html', {
        'gastos': gastos,
        'search_query': search_query,
        'categoria': categoria,
        'fecha': fecha,
        'categorias': categorias
    })

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
    filterset_fields = ['tipo', 'venta', 'pedido', 'empleado', 'fecha']
    search_fields = ['descripcion']
    ordering_fields = ['id_finanzas', 'fecha', 'valor', 'total']

class GastoViewSet(viewsets.ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['categoria', 'fecha']
    search_fields = ['descripcion']
    ordering_fields = ['id', 'fecha', 'monto']