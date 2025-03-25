# finanzas/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FinanzasViewSet, GastoViewSet,
    finanzas_list, finanzas_create, finanzas_update, finanzas_delete,
    gasto_list, gasto_create, gasto_update, gasto_delete
)

router = DefaultRouter()
router.register(r'finanzas', FinanzasViewSet)
router.register(r'gastos', GastoViewSet)  # Ahora sí existe

app_name = 'finanzas'

urlpatterns = [
    # URLs de la API REST
    path('api/', include(router.urls)),

    # URLs para vistas basadas en plantillas - Finanzas
    path('', finanzas_list, name='finanzas_list'),
    path('create/', finanzas_create, name='finanzas_create'),
    path('update/<int:pk>/', finanzas_update, name='finanzas_update'),
    path('delete/<int:pk>/', finanzas_delete, name='finanzas_delete'),

    # URLs para vistas basadas en plantillas - Gastos
    path('gastos/', gasto_list, name='gasto_list'),
    path('gastos/create/', gasto_create, name='gasto_create'),
    path('gastos/update/<int:pk>/', gasto_update, name='gasto_update'),
    path('gastos/delete/<int:pk>/', gasto_delete, name='gasto_delete'),
]