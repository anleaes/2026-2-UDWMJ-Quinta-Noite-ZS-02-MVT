from django.db import models
from pessoa import Pessoa

# Create your models here.
class Cliente(Pessoa):
    email = models.EmailField('Email', max_length=100)
    endereco = models.CharField('Endereço', max_length=100)
    data_admissao = models.DateField('Data de Admissão')
    observacoes_gerais = models.TextField('Observações Gerais', blank=True, null=True)
    # blanck permite que o campo seja deixado em branco no formulário
    # null permite que o campo seja deixado em branco no banco de dados

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        ordering =['id']

    def __str__(self):
        return super().first_name
        # ou pode ser usado "return super().__str__()"

