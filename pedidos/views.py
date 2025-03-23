from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Pedido
from .serializers import PedidoSerializer
from django.contrib.auth.decorators import login_required

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

@login_required
def pedido_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/pedido_list.html', {'pedidos': pedidos})
