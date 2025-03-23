from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Venta, VentaVehiculo
from .serializers import ClienteSerializer, VentaSerializer, VentaVehiculoSerializer
from django.contrib.auth.decorators import login_required
from .models import Cliente


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

@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'ventas/cliente_list.html', {'clientes': clientes})
