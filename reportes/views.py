from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from finanzas.models import Finanzas
from django.contrib.auth.decorators import login_required

class VentasPorMesView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        ventas = Finanzas.objects.filter(tipo='Ingreso').annotate(
            mes=TruncMonth('fecha')
        ).values('mes').annotate(total=Sum('total')).order_by('mes')
        return Response(ventas)

@login_required
def reporte_ventas(request):
    ventas = Finanzas.objects.filter(tipo='Ingreso').annotate(
        mes=TruncMonth('fecha')
    ).values('mes').annotate(total=Sum('total')).order_by('mes')
    return render(request, 'reportes/reporte_ventas.html', {'ventas': ventas})
