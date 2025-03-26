# empleados/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Empleado
from .forms import EmpleadoForm
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import EmpleadoSerializer



class EmpleadoListView(LoginRequiredMixin, ListView):
    model = Empleado
    template_name = 'empleados/empleado_list.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        puesto = self.request.GET.get('puesto', '')
        if search_query:
            queryset = queryset.filter(nombre__icontains=search_query) | queryset.filter(apellido__icontains=search_query)
        if puesto:
            queryset = queryset.filter(puesto=puesto)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['puesto_selected'] = self.request.GET.get('puesto', '')
        context['puestos'] = Empleado.objects.values_list('puesto', flat=True).distinct()
        return context

class EmpleadoCreateView(LoginRequiredMixin, CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/empleado_form.html'
    success_url = reverse_lazy('empleados:empleado_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Empleado creado exitosamente.")
        return response

class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/empleado_form.html'
    success_url = reverse_lazy('empleados:empleado_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Empleado actualizado exitosamente.")
        return response

class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    template_name = 'empleados/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleados:empleado_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Empleado eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated]