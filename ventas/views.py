# ventas/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Cliente
from .forms import ClienteForm

class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'ventas/cliente_list.html'
    context_object_name = 'clientes'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(nombre__icontains=search_query) | queryset.filter(apellido__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'ventas/cliente_form.html'
    success_url = reverse_lazy('ventas:cliente_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Cliente creado exitosamente.")
        return response

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'ventas/cliente_form.html'
    success_url = reverse_lazy('ventas:cliente_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Cliente actualizado exitosamente.")
        return response

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'ventas/cliente_confirm_delete.html'
    success_url = reverse_lazy('ventas:cliente_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Cliente eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)