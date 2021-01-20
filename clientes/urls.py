from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name="lista"),
    path('eliminar/<int:id>/', views.eliminar, name="eliminar"),
    path('detalle/<int:id>/', views.detalle, name="detalle"),
    path('crear/', views.crear, name="crear"),
    path('editar/<int:id>/', views.editar, name="editar"),
]