from django.db import models


class AtendimentoExame(models.Model):
    atendimento = models.ForeignKey(
        'atendimento.Atendimento',
        verbose_name='Atendimento',
        on_delete=models.CASCADE,
        related_name='exames',
    )
    tipo_exame = models.ForeignKey(
        'tipoexame.TipoExame',
        verbose_name='Tipo de exame',
        on_delete=models.PROTECT,
        related_name='atendimentos_exame',
    )
    resultado = models.TextField('Resultado')
    data_realizacao = models.DateTimeField('Data de realização')

    class Meta:
        verbose_name = 'Exame do atendimento'
        verbose_name_plural = 'Exames do atendimento'
        ordering = ['id']

    def __str__(self):
        return f'{self.tipo_exame} - {self.atendimento}'
