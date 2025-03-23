from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Vehiculo, Inventario
from .serializers import VehiculoSerializer, InventarioSerializer
from django.contrib.auth.decorators import login_required

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [IsAuthenticated]

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [IsAuthenticated]

@login_required
def vehiculo_list(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'inventario/vehiculo_list.html', {'vehiculos': vehiculos})