# pedidos/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Pedido
from .forms import PedidoForm

class PedidoListView(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = 'pedidos/pedido_list.html'
    context_object_name = 'pedidos'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        estado = self.request.GET.get('estado', '')
        if search_query:
            queryset = queryset.filter(cliente__nombre__icontains=search_query)
        if estado:
            queryset = queryset.filter(estado=estado)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['estado_selected'] = self.request.GET.get('estado', '')
        context['estados'] = Pedido.objects.values_list('estado', flat=True).distinct()
        return context

class PedidoCreateView(LoginRequiredMixin, CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedidos/pedido_form.html'
    success_url = reverse_lazy('pedidos:pedido_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Pedido creado exitosamente.")
        return response

class PedidoUpdateView(LoginRequiredMixin, UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedidos/pedido_form.html'
    success_url = reverse_lazy('pedidos:pedido_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Pedido actualizado exitosamente.")
        return response

class PedidoDeleteView(LoginRequiredMixin, DeleteView):
    model = Pedido
    template_name = 'pedidos/pedido_confirm_delete.html'
    success_url = reverse_lazy('pedidos:pedido_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Pedido eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)