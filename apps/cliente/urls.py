from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('listar/', views.list_cliente, name='list_cliente'),
    path('adicionar/', views.add_cliente, name='add_cliente'),
    path('editar/<int:id_cliente>/', views.edit_cliente, name='edit_cliente'),
    path('excluir/<int:id_cliente>/', views.delete_cliente, name='delete_cliente'),
]