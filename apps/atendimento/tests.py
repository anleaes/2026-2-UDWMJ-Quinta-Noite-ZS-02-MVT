from datetime import date

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from animal.models import Animal
from cliente.models import Cliente
from tipoanimal.models import TipoAnimal
from veterinario.models import Veterinario

from .models import Atendimento, TipoAtendimento


class AtendimentoViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cliente = Cliente.objects.create(
            nome='Ana',
            sobrenome='Silva',
            cpf='12345678900',
            telefone='11999999999',
            email='ana@example.com',
            endereco='Rua A',
            data_admissao=date(2026, 1, 1),
        )
        cls.tipo_animal = TipoAnimal.objects.create(
            nome='Cão',
            porte=TipoAnimal.Porte.PEQUENO,
            descricao='Canino',
            faixa_peso='Até 10 kg',
        )
        cls.animal = Animal.objects.create(
            nome='Rex',
            data_nascimento=date(2020, 1, 1),
            sexo=Animal.Sexo.MACHO,
            responsavel=cls.cliente,
            tipo_animal=cls.tipo_animal,
            foto_animal='animais/rex.jpg',
        )
        cls.veterinario = Veterinario.objects.create(
            nome='João',
            sobrenome='Médico',
            cpf='98765432100',
            telefone='11988888888',
            salario='5000.00',
            crmv='CRMV123',
            titulacao_maxima='Mestrado',
            horario_plantao='08:00 às 18:00',
        )
        cls.tipo_atendimento = TipoAtendimento.objects.create(
            nome='Consulta',
            descricao='Atendimento clínico',
        )
        cls.data_hora = timezone.now().replace(second=0, microsecond=0)

    def atendimento_form_data(self, **overrides):
        data = {
            'data_hora': self.data_hora.strftime('%Y-%m-%dT%H:%M'),
            'motivo': 'Consulta de rotina',
            'observacoes': '',
            'status': Atendimento.Status.AGENDADO,
            'tipo_atendimento': self.tipo_atendimento.pk,
            'animal': self.animal.pk,
            'veterinario': self.veterinario.pk,
        }
        data.update(overrides)
        return data

    def test_list_atendimentos(self):
        Atendimento.objects.create(
            data_hora=self.data_hora,
            motivo='Consulta de rotina',
            tipo_atendimento=self.tipo_atendimento,
            animal=self.animal,
            veterinario=self.veterinario,
        )

        response = self.client.get(reverse('atendimento:list_atendimento'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Consulta de rotina')
        self.assertContains(response, 'Rex')

    def test_add_atendimento(self):
        response = self.client.post(
            reverse('atendimento:add_atendimento'),
            self.atendimento_form_data(),
        )

        self.assertRedirects(response, reverse('atendimento:list_atendimento'))
        self.assertEqual(Atendimento.objects.count(), 1)

    def test_invalid_status_does_not_create_atendimento(self):
        response = self.client.post(
            reverse('atendimento:add_atendimento'),
            self.atendimento_form_data(status='invalido'),
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('status', response.context['form'].errors)
        self.assertEqual(Atendimento.objects.count(), 0)

    def test_edit_atendimento(self):
        atendimento = Atendimento.objects.create(
            data_hora=self.data_hora,
            motivo='Consulta de rotina',
            tipo_atendimento=self.tipo_atendimento,
            animal=self.animal,
            veterinario=self.veterinario,
        )

        response = self.client.post(
            reverse('atendimento:edit_atendimento', args=[atendimento.pk]),
            self.atendimento_form_data(motivo='Retorno'),
        )

        self.assertRedirects(response, reverse('atendimento:list_atendimento'))
        atendimento.refresh_from_db()
        self.assertEqual(atendimento.motivo, 'Retorno')

    def test_delete_atendimento(self):
        atendimento = Atendimento.objects.create(
            data_hora=self.data_hora,
            motivo='Consulta de rotina',
            tipo_atendimento=self.tipo_atendimento,
            animal=self.animal,
            veterinario=self.veterinario,
        )

        response = self.client.get(
            reverse('atendimento:delete_atendimento', args=[atendimento.pk]),
        )

        self.assertRedirects(response, reverse('atendimento:list_atendimento'))
        self.assertFalse(Atendimento.objects.filter(pk=atendimento.pk).exists())
