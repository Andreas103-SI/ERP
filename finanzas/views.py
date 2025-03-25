# finanzas/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Finanzas, Gasto
from .forms import FinanzasForm, GastoForm

class FinanzasListView(LoginRequiredMixin, ListView):
    model = Finanzas
    template_name = 'finanzas/finanzas_list.html'
    context_object_name = 'finanzas'

    def get_queryset(self):
        queryset = super().get_queryset()
        tipo = self.request.GET.get('tipo', '')
        fecha = self.request.GET.get('fecha', '')
        if tipo:
            queryset = queryset.filter(tipo=tipo)
        if fecha:
            queryset = queryset.filter(fecha=fecha)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo'] = self.request.GET.get('tipo', '')
        context['fecha'] = self.request.GET.get('fecha', '')
        return context

class FinanzasCreateView(LoginRequiredMixin, CreateView):
    model = Finanzas
    form_class = FinanzasForm
    template_name = 'finanzas/finanzas_form.html'
    success_url = reverse_lazy('finanzas:finanzas_list')

class FinanzasUpdateView(LoginRequiredMixin, UpdateView):
    model = Finanzas
    form_class = FinanzasForm
    template_name = 'finanzas/finanzas_form.html'
    success_url = reverse_lazy('finanzas:finanzas_list')

class FinanzasDeleteView(LoginRequiredMixin, DeleteView):
    model = Finanzas
    template_name = 'finanzas/finanzas_confirm_delete.html'
    success_url = reverse_lazy('finanzas:finanzas_list')

class GastoListView(LoginRequiredMixin, ListView):
    model = Gasto
    template_name = 'finanzas/gasto_list.html'
    context_object_name = 'gastos'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        categoria = self.request.GET.get('categoria', '')
        fecha = self.request.GET.get('fecha', '')
        if search_query:
            queryset = queryset.filter(descripcion__icontains=search_query)
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        if fecha:
            queryset = queryset.filter(fecha=fecha)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['categoria'] = self.request.GET.get('categoria', '')
        context['fecha'] = self.request.GET.get('fecha', '')
        context['categorias'] = Gasto.objects.values_list('categoria', flat=True).distinct()
        return context

class GastoCreateView(LoginRequiredMixin, CreateView):
    model = Gasto
    form_class = GastoForm
    template_name = 'finanzas/gasto_form.html'
    success_url = reverse_lazy('finanzas:gasto_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.warning(
            self.request,
            "Gasto creado exitosamente. Debes registrar este gasto como egreso en el módulo de Finanzas."
        )
        return response

class GastoUpdateView(LoginRequiredMixin, UpdateView):
    model = Gasto
    form_class = GastoForm
    template_name = 'finanzas/gasto_form.html'
    success_url = reverse_lazy('finanzas:gasto_list')

class GastoDeleteView(LoginRequiredMixin, DeleteView):
    model = Gasto
    template_name = 'finanzas/gasto_confirm_delete.html'
    success_url = reverse_lazy('finanzas:gasto_list')