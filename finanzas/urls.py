from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'finanzas', views.FinanzasViewSet)
router.register(r'gastos', views.GastoViewSet)

app_name = 'finanzas'  # Define el namespace para las URLs

urlpatterns = [
    path('api/', include(router.urls)),  # URLs de la API
    path('finanzas/', views.finanza_list, name='finanza_list'),  # Vista basada en plantillas
]