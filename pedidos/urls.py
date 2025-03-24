# pedidos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoViewSet, pedido_list, pedido_create, pedido_update, pedido_delete

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet)

app_name = 'pedidos'  # Define el namespace para las URLs

urlpatterns = [
    # URLs de la API REST
    path('api/', include(router.urls)),

    # URLs para vistas basadas en plantillas
    path('', pedido_list, name='pedido_list'),
    path('create/', pedido_create, name='pedido_create'),
    path('update/<int:pk>/', pedido_update, name='pedido_update'),
    path('delete/<int:pk>/', pedido_delete, name='pedido_delete'),
]