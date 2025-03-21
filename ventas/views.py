from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Venta, VentaVehiculo
from .serializers import ClienteSerializer, VentaSerializer, VentaVehiculoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class VentaVehiculoViewSet(viewsets.ModelViewSet):
    queryset = VentaVehiculo.objects.all()
    serializer_class = VentaVehiculoSerializer

# Create your views here.
