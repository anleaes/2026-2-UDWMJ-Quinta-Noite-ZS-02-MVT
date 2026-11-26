from django.urls import path

from . import views

app_name = 'pagamento'

urlpatterns = [
    path('listar/', views.list_pagamento, name='list_pagamento'),
    path('adicionar/', views.add_pagamento, name='add_pagamento'),
    path(
        'editar/<int:id_pagamento>/',
        views.edit_pagamento,
        name='edit_pagamento',
    ),
    path(
        'excluir/<int:id_pagamento>/',
        views.delete_pagamento,
        name='delete_pagamento',
    ),
]
