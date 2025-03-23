from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Finanzas
from .serializers import FinanzasSerializer
from django.contrib.auth.decorators import login_required

class FinanzasViewSet(viewsets.ModelViewSet):
    queryset = Finanzas.objects.all()
    serializer_class = FinanzasSerializer
    permission_classes = [IsAuthenticated]

@login_required
def finanza_list(request):
    finanzas = Finanzas.objects.all()
    return render(request, 'finanzas/finanza_list.html', {'finanzas': finanzas})