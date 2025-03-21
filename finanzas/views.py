from django.shortcuts import render
from rest_framework import viewsets
from .models import Finanzas
from .serializers import FinanzasSerializer

class FinanzasViewSet(viewsets.ModelViewSet):
    queryset = Finanzas.objects.all()
    serializer_class = FinanzasSerializer
# Create your views here.
