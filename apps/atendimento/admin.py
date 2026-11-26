from django.contrib import admin

from .models import Atendimento, TipoAtendimento


admin.site.register(Atendimento)
admin.site.register(TipoAtendimento)
