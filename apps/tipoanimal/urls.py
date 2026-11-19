from django.urls import path
from . import views
from django.urls import path, include

app_name = 'tipoanimal'

urlpatterns = [
    path('listar/', views.list_tipoanimal, name='list_tipoanimal'),
    path('adicionar/', views.add_tipoanimal, name='add_tipoanimal'),
    path('editar/<int:id_tipoanimal>/', views.edit_tipoanimal, name='edit_tipoanimal'),
    path('excluir/<int:id_tipoanimal>/', views.delete_tipoanimal, name='delete_tipoanimal'),
]
