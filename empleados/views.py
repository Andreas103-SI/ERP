from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Empleado
from .serializers import EmpleadoSerializer
from django.contrib.auth.decorators import login_required

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated]

@login_required
def empleado_list(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/empleado_list.html', {'empleados': empleados})