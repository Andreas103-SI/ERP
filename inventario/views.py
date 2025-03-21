from django.shortcuts import render
from rest_framework import viewsets
from .models import Vehiculo, Inventario
from .serializers import VehiculoSerializer, InventarioSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

# Create your views here.
