from django.urls import path

from . import views

app_name = 'tipoconsulta'

urlpatterns = [
    path('listar/', views.list_tipo_consulta, name='list_tipo_consulta'),
    path('adicionar/', views.add_tipo_consulta, name='add_tipo_consulta'),
    path(
        'editar/<int:id_tipo_consulta>/',
        views.edit_tipo_consulta,
        name='edit_tipo_consulta',
    ),
    path(
        'excluir/<int:id_tipo_consulta>/',
        views.delete_tipo_consulta,
        name='delete_tipo_consulta',
    ),
]
