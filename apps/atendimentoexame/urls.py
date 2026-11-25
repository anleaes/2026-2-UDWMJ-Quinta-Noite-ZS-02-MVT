from django.urls import path

from . import views

app_name = 'atendimentoexame'

urlpatterns = [
    path('listar/', views.list_atendimentoexame, name='list_atendimentoexame'),
    path('adicionar/', views.add_atendimentoexame, name='add_atendimentoexame'),
    path('editar/<int:id_atendimentoexame>/',views.edit_atendimentoexame,name='edit_atendimentoexame',),
    path('excluir/<int:id_atendimentoexame>/',views.delete_atendimentoexame,name='delete_atendimentoexame',
    ),
]