# pedidos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PedidoListView,
    PedidoCreateView,
    PedidoUpdateView,
    PedidoDeleteView,
    PedidoViewSet,
)

app_name = 'pedidos'

# Configurar el router para la API
router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('', PedidoListView.as_view(), name='pedido_list'),
    path('create/', PedidoCreateView.as_view(), name='pedido_create'),
    path('update/<int:pk>/', PedidoUpdateView.as_view(), name='pedido_update'),
    path('delete/<int:pk>/', PedidoDeleteView.as_view(), name='pedido_delete'),
    path('api/', include(router.urls)),
]