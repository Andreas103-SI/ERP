from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoViewSet, pedido_list

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet)

app_name = 'pedidos'  # Define el namespace para las URLs

urlpatterns = [
    path('api/', include(router.urls)),  # URLs de la API
    path('pedidos/', pedido_list, name='pedido_list'),  # Vista basada en plantillas
]