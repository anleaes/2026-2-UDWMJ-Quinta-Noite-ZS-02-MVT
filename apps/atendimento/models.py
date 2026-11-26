from django.db import models


class Atendimento(models.Model):
    class Status(models.TextChoices):
        AGENDADO = 'agendado', 'Agendado'
        EM_ANDAMENTO = 'em_andamento', 'Em andamento'
        CONCLUIDO = 'concluido', 'Concluído'
        CANCELADO = 'cancelado', 'Cancelado'

    data_hora = models.DateTimeField('Data e hora')
    motivo = models.TextField('Motivo')
    observacoes = models.TextField('Observações', blank=True)
    status = models.CharField(
        'Status',
        max_length=20,
        choices=Status.choices,
        default=Status.AGENDADO,
    )
    animal = models.ForeignKey(
        'animal.Animal',
        verbose_name='Animal',
        on_delete=models.PROTECT,
        related_name='atendimentos',
    )
    veterinario = models.ForeignKey(
        'veterinario.Veterinario',
        verbose_name='Veterinário',
        on_delete=models.PROTECT,
        related_name='atendimentos',
    )
    tipo_consulta = models.ForeignKey(
        'tipoconsulta.TipoConsulta',
        verbose_name='Tipo de consulta',
        on_delete=models.PROTECT,
        related_name='atendimentos',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'
        ordering = ['data_hora', 'id']

    def __str__(self):
        return f'{self.animal} - {self.data_hora:%d/%m/%Y %H:%M}'
