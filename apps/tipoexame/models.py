from django.db import models

# Create your models here.
class TipoExame(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tempo_resultado = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tipo de Exame"
        verbose_name_plural = "Tipos de Exames"
        ordering = ['id']


    def __str__(self):
        return self.nome