# inventario/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Vehiculo
from .forms import VehiculoForm
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import VehiculoSerializer

class VehiculoListView(LoginRequiredMixin, ListView):
    model = Vehiculo
    template_name = 'inventario/vehiculo_list.html'
    context_object_name = 'vehiculos'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(marca__icontains=search_query) | queryset.filter(modelo__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

class VehiculoCreateView(LoginRequiredMixin, CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'inventario/vehiculo_form.html'
    success_url = reverse_lazy('inventario:vehiculo_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Vehículo creado exitosamente.")
        return response

class VehiculoUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'inventario/vehiculo_form.html'
    success_url = reverse_lazy('inventario:vehiculo_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Vehículo actualizado exitosamente.")
        return response

class VehiculoDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehiculo
    template_name = 'inventario/vehiculo_confirm_delete.html'
    success_url = reverse_lazy('inventario:vehiculo_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Vehículo eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [IsAuthenticated]