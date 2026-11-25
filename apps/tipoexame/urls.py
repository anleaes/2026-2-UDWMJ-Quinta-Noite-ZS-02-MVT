from django.urls import path

from . import views

app_name = 'tipoexame'

urlpatterns = [
    path('listar/', views.list_tipoexame, name='list_tipoexame'),
    path('adicionar/', views.add_tipoexame, name='add_tipoexame'),
    path('editar/<int:id_tipoexame>/', views.edit_tipoexame, name='edit_tipoexame'),
    path('excluir/<int:id_tipoexame>/', views.delete_tipoexame, name='delete_tipoexame'),
]