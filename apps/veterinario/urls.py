from django.urls import path
from . import views

app_name = 'veterinario'

urlpatterns = [
    path('listar/', views.list_veterinario, name='list_veterinario'),
    path('adicionar/', views.add_veterinario, name='add_veterinario'),
    path('editar/<int:id_veterinario>/', views.edit_veterinario, name='edit_veterinario'),
    path('excluir/<int:id_veterinario>/', views.delete_veterinario, name='delete_veterinario'),
]