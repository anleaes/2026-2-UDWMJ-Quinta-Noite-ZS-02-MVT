from django.db import models


class TipoConsulta(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', blank=True)

    class Meta:
        verbose_name = 'Tipo de consulta'
        verbose_name_plural = 'Tipos de consulta'
        ordering = ['id']

    def __str__(self):
        return self.nome
