from django.shortcuts import render
from rest_framework import viewsets
from .models import Proveedor, Pedido
from .serializers import ProveedorSerializer, PedidoSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
# Create your views here.
