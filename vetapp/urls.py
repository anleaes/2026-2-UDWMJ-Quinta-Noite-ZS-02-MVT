"""
URL configuration for vetapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('cliente/', include('cliente.urls', namespace='cliente')),
    path('especialidade/', include('especialidade.urls', namespace='especialidade')),
    path('veterinario/', include('veterinario.urls', namespace='veterinario')),
    path('atendimento/', include('atendimento.urls', namespace='atendimento')),
    path('prontuario/', include('prontuario.urls', namespace='prontuario')),
    path('pagamento/', include('pagamento.urls', namespace='pagamento')),
    path('tipoconsulta/', include('tipoconsulta.urls', namespace='tipoconsulta')),
    path('tipoanimal/', include('tipoanimal.urls', namespace='tipoanimal')),
    path('animal/', include('animal.urls', namespace='animal')),
    path('atendimentoexame/',include('atendimentoexame.urls', namespace='atendimentoexame'),),
    path('tipoexame/', include('tipoexame.urls', namespace='tipoexame')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)