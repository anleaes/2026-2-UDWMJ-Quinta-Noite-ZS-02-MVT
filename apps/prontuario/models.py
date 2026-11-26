from django.db import models


class Prontuario(models.Model):
    descricao = models.TextField('Descrição')
    diagnostico = models.FileField(
        'Diagnóstico',
        upload_to='prontuarios/diagnosticos/',
    )
    prescricao = models.TextField('Prescrição')
    data_registro = models.DateField('Data de registro')
    atendimento = models.OneToOneField(
        'atendimento.Atendimento',
        verbose_name='Atendimento',
        on_delete=models.CASCADE,
        related_name='prontuario',
    )

    class Meta:
        verbose_name = 'Prontuário'
        verbose_name_plural = 'Prontuários'
        ordering = ['-data_registro', 'id']

    def __str__(self):
        return f'Prontuário do atendimento #{self.atendimento_id}'
