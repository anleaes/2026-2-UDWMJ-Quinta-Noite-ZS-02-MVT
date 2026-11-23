from django.db import models
from cliente.models import Cliente
from tipoanimal.models import TipoAnimal


class Animal(models.Model):
    class Sexo(models.TextChoices):
        MACHO = 'macho', 'Macho'
        FEMEA = 'femea', 'Fêmea'

    nome = models.CharField('Nome', max_length=100)
    data_nascimento = models.DateField('Data de nascimento')
    sexo = models.CharField('Sexo', max_length=5, choices=Sexo.choices)
    responsavel = models.ForeignKey(
        Cliente,
        verbose_name='Responsável',
        on_delete=models.PROTECT,
        related_name='animais',
    )
    tipo_animal = models.ForeignKey(
        TipoAnimal,
        verbose_name='Tipo de animal',
        on_delete=models.PROTECT,
        related_name='animais',
    )
    foto_animal = models.ImageField('Foto do animal', upload_to='animais/')

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering = ['id']

    def __str__(self):
        return self.nome
