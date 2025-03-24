# pedidos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Pedido
from .forms import PedidoForm
from .serializers import PedidoSerializer

def pedido_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/pedido_list.html', {'pedidos': pedidos})

def pedido_create(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedidos:pedido_list')
    else:
        form = PedidoForm()
    return render(request, 'pedidos/pedido_form.html', {'form': form})

def pedido_update(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('pedidos:pedido_list')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedidos/pedido_form.html', {'form': form})

def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedidos:pedido_list')
    return render(request, 'pedidos/pedido_confirm_delete.html', {'pedido': pedido})

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer