from django.urls import path
from . import views

app_name = 'especialidade'

urlpatterns = [
    path('listar/', views.list_especialidade, name='list_especialidade'),
    path('adicionar/', views.add_especialidade, name='add_especialidade'),
    path('editar/<int:id_especialidade>/', views.edit_especialidade, name='edit_especialidade'),
    path('excluir/<int:id_especialidade>/', views.delete_especialidade, name='delete_especialidade'),
]