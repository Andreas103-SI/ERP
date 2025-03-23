from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cliente, Venta, VentaVehiculo
from .serializers import ClienteSerializer, VentaSerializer, VentaVehiculoSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ClienteForm



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
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas:cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'ventas/cliente_form.html', {'form': form})