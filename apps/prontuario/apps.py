from django.apps import AppConfig


class ProntuarioConfig(AppConfig):
    name = 'prontuario'
    verbose_name = 'Prontuário'

    def ready(self):
        from . import signals
