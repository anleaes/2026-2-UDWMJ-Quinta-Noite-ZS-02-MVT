from django.db import models


class Pagamento(models.Model):
    class FormaPagamento(models.TextChoices):
        DINHEIRO = 'dinheiro', 'Dinheiro'
        PIX = 'pix', 'Pix'
        CARTAO_DEBITO = 'cartao_debito', 'Cartão de débito'
        CARTAO_CREDITO = 'cartao_credito', 'Cartão de crédito'
        TRANSFERENCIA = 'transferencia', 'Transferência'

    class StatusPagamento(models.TextChoices):
        PENDENTE = 'pendente', 'Pendente'
        PAGO = 'pago', 'Pago'
        CANCELADO = 'cancelado', 'Cancelado'
        ESTORNADO = 'estornado', 'Estornado'

    atendimento = models.OneToOneField(
        'atendimento.Atendimento',
        verbose_name='Atendimento',
        on_delete=models.CASCADE,
        related_name='pagamento',
    )
    valor_total = models.DecimalField(
        'Valor total',
        max_digits=10,
        decimal_places=2,
    )
    forma_pagamento = models.CharField(
        'Forma de pagamento',
        max_length=20,
        choices=FormaPagamento.choices,
    )
    status_pagamento = models.CharField(
        'Status do pagamento',
        max_length=20,
        choices=StatusPagamento.choices,
    )
    data_pagamento = models.DateTimeField('Data do pagamento')

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['-data_pagamento', 'id']

    def __str__(self):
        return f'Pagamento do atendimento #{self.atendimento_id}'
