from django.db import models
from pessoa.models import Pessoa
from especialidade.models import Especialidade

# Create your models here.
class Veterinario(Pessoa):
    salario = models.DecimalField('Salario', max_digits=10, decimal_places=2)
    crmv = models.CharField('CRMV', max_length=10, unique=True)
    ativo = models.BooleanField('Ativo', default=True)
    titulacao_maxima = models.CharField('Titulação Máxima', max_length=100)
    horario_plantao = models.CharField('Horário de Plantão', max_length=100)
    especialidade = models.ManyToManyField(Especialidade, verbose_name="Especialidades")

    
    class Meta:
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'
        ordering =['id']

    def __str__(self):
        return super().first_name
        # ou pode ser usado "return super().__str__()"

