from django.core.files.storage import default_storage
from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Prontuario


@receiver(post_delete, sender=Prontuario)
def delete_diagnostico_file(sender, instance, **kwargs):
    if instance.diagnostico:
        default_storage.delete(instance.diagnostico.name)
