from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cliente, Venta, VentaVehiculo
from .serializers import ClienteSerializer, VentaSerializer, VentaVehiculoSerializer
from django.contrib.auth.decorators import login_required

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [IsAuthenticated]

class VentaVehiculoViewSet(viewsets.ModelViewSet):
    queryset = VentaVehiculo.objects.all()
    serializer_class = VentaVehiculoSerializer
    permission_classes = [IsAuthenticated]

@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'ventas/cliente_list.html', {'clientes': clientes})