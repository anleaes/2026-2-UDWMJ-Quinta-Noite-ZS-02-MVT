from django.db import models


class TipoAnimal(models.Model):
    class Porte(models.TextChoices):
        PEQUENO = 'pequeno', 'Pequeno'
        MEDIO = 'medio', 'Médio'
        GRANDE = 'grande', 'Grande'

    nome = models.CharField(max_length=100)
    porte = models.CharField(max_length=10, choices=Porte.choices)
    descricao = models.TextField()
    faixa_peso = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Tipo de Animal'
        verbose_name_plural = 'Tipos de Animal'
        ordering = ['id']

    def __str__(self):
        return self.nome
