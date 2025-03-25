# proveedores/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Proveedor
from .forms import ProveedorForm
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ProveedorSerializer

class ProveedorListView(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = 'proveedores/proveedor_list.html'
    context_object_name = 'proveedores'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(nombre__icontains=search_query) | queryset.filter(contacto__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

class ProveedorCreateView(LoginRequiredMixin, CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedores/proveedor_form.html'
    success_url = reverse_lazy('proveedores:proveedor_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Proveedor creado exitosamente.")
        return response

class ProveedorUpdateView(LoginRequiredMixin, UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedores/proveedor_form.html'
    success_url = reverse_lazy('proveedores:proveedor_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Proveedor actualizado exitosamente.")
        return response

class ProveedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Proveedor
    template_name = 'proveedores/proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedores:proveedor_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Proveedor eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['nombre']
    search_fields = ['nombre', 'contacto']
    ordering_fields = ['id', 'nombre']