# proveedores/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'proveedores', views.ProveedorViewSet)

urlpatterns = [
    path('', views.proveedor_list, name='proveedor_list'),
    path('create/', views.proveedor_create, name='proveedor_create'),
    path('update/<int:pk>/', views.proveedor_update, name='proveedor_update'),
    path('delete/<int:pk>/', views.proveedor_delete, name='proveedor_delete'),
    path('api/', include(router.urls)),
]