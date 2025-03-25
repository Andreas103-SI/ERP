# proveedores/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from pedidos.models import Proveedor
from .forms import ProveedorForm
from .serializers import ProveedorSerializer
from django.db.models import Q

@login_required
def proveedor_list(request):
    proveedores = Proveedor.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        proveedores = proveedores.filter(
            Q(nombre__icontains=search_query) |
            Q(contacto__icontains=search_query) |
            Q(producto__icontains=search_query)
        )
    return render(request, 'proveedores/proveedor_list.html', {
        'proveedores': proveedores,
        'search_query': search_query
    })

@login_required
def proveedor_create(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores:proveedor_list')
    else:
        form = ProveedorForm()
    return render(request, 'proveedores/proveedor_form.html', {'form': form})

@login_required
def proveedor_update(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedores:proveedor_list')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedores/proveedor_form.html', {'form': form})

@login_required
def proveedor_delete(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedores:proveedor_list')
    return render(request, 'proveedores/proveedor_confirm_delete.html', {'proveedor': proveedor})

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['nombre']
    search_fields = ['nombre', 'contacto', 'producto']
    ordering_fields = ['id_proveedor', 'nombre']