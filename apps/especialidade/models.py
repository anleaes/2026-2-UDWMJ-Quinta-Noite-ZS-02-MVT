from django.db import models

# Create your models here.
class Especialidade(models.Model):
    name = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição', max_length=200) 
    requer_equipamento_especial = models.BooleanField('Requer Equipamento Especial', default=False)
    requer_internacao = models.BooleanField('Requer Internação', default=False)
    
    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'
        ordering =['id']

    def __str__(self):
        return f'{self.name}'

