from datetime import date

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from animal.models import Animal
from atendimento.models import Atendimento
from cliente.models import Cliente
from tipoanimal.models import TipoAnimal
from veterinario.models import Veterinario

from .models import Pagamento


class PagamentoViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cliente = Cliente.objects.create(
            nome='Ana',
            sobrenome='Silva',
            cpf='12345678900',
            telefone='11999999999',
            email='ana@example.com',
            endereco='Rua A',
            data_admissao=date(2026, 1, 1),
        )
        tipo_animal = TipoAnimal.objects.create(
            nome='Cão',
            porte=TipoAnimal.Porte.PEQUENO,
            descricao='Canino',
            faixa_peso='Até 10 kg',
        )
        animal = Animal.objects.create(
            nome='Rex',
            data_nascimento=date(2020, 1, 1),
            sexo=Animal.Sexo.MACHO,
            responsavel=cliente,
            tipo_animal=tipo_animal,
            foto_animal='animais/rex.jpg',
        )
        veterinario = Veterinario.objects.create(
            nome='João',
            sobrenome='Médico',
            cpf='98765432100',
            telefone='11988888888',
            salario='5000.00',
            crmv='CRMV123',
            titulacao_maxima='Mestrado',
            horario_plantao='08:00 às 18:00',
        )
        cls.atendimento = Atendimento.objects.create(
            data_hora=timezone.now(),
            motivo='Consulta de rotina',
            animal=animal,
            veterinario=veterinario,
        )

    def pagamento_form_data(self, **overrides):
        data = {
            'atendimento': self.atendimento.pk,
            'valor_total': '150.00',
            'forma_pagamento': Pagamento.FormaPagamento.PIX,
            'status_pagamento': Pagamento.StatusPagamento.PENDENTE,
            'data_pagamento': timezone.localtime().strftime('%Y-%m-%dT%H:%M'),
        }
        data.update(overrides)
        return data

    def test_list_pagamentos(self):
        Pagamento.objects.create(
            atendimento=self.atendimento,
            valor_total='150.00',
            forma_pagamento=Pagamento.FormaPagamento.PIX,
            status_pagamento=Pagamento.StatusPagamento.PENDENTE,
            data_pagamento=timezone.now(),
        )

        response = self.client.get(reverse('pagamento:list_pagamento'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '150.00')
        self.assertContains(response, 'Rex')
        self.assertContains(response, 'Pix')

    def test_add_pagamento(self):
        response = self.client.post(
            reverse('pagamento:add_pagamento'),
            self.pagamento_form_data(),
        )

        self.assertRedirects(
            response,
            reverse('pagamento:list_pagamento'),
        )
        self.assertTrue(Pagamento.objects.filter(atendimento=self.atendimento).exists())

    def test_one_payment_per_atendimento(self):
        Pagamento.objects.create(
            atendimento=self.atendimento,
            valor_total='150.00',
            forma_pagamento=Pagamento.FormaPagamento.PIX,
            status_pagamento=Pagamento.StatusPagamento.PENDENTE,
            data_pagamento=timezone.now(),
        )

        response = self.client.post(
            reverse('pagamento:add_pagamento'),
            self.pagamento_form_data(),
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('atendimento', response.context['form'].errors)
        self.assertEqual(Pagamento.objects.count(), 1)

    def test_invalid_payment_choices_do_not_create_payment(self):
        response = self.client.post(
            reverse('pagamento:add_pagamento'),
            self.pagamento_form_data(
                forma_pagamento='cripto',
                status_pagamento='invalido',
            ),
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('forma_pagamento', response.context['form'].errors)
        self.assertIn('status_pagamento', response.context['form'].errors)
        self.assertEqual(Pagamento.objects.count(), 0)

    def test_edit_pagamento(self):
        pagamento = Pagamento.objects.create(
            atendimento=self.atendimento,
            valor_total='150.00',
            forma_pagamento=Pagamento.FormaPagamento.PIX,
            status_pagamento=Pagamento.StatusPagamento.PENDENTE,
            data_pagamento=timezone.now(),
        )

        response = self.client.post(
            reverse('pagamento:edit_pagamento', args=[pagamento.pk]),
            self.pagamento_form_data(
                valor_total='175.50',
                forma_pagamento=Pagamento.FormaPagamento.DINHEIRO,
                status_pagamento=Pagamento.StatusPagamento.PAGO,
            ),
        )

        self.assertRedirects(
            response,
            reverse('pagamento:list_pagamento'),
        )
        pagamento.refresh_from_db()
        self.assertEqual(str(pagamento.valor_total), '175.50')
        self.assertEqual(pagamento.status_pagamento, Pagamento.StatusPagamento.PAGO)

    def test_delete_requires_confirmation(self):
        pagamento = Pagamento.objects.create(
            atendimento=self.atendimento,
            valor_total='150.00',
            forma_pagamento=Pagamento.FormaPagamento.PIX,
            status_pagamento=Pagamento.StatusPagamento.PENDENTE,
            data_pagamento=timezone.now(),
        )

        response = self.client.get(
            reverse('pagamento:delete_pagamento', args=[pagamento.pk]),
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Pagamento.objects.filter(pk=pagamento.pk).exists())

    def test_delete_pagamento(self):
        pagamento = Pagamento.objects.create(
            atendimento=self.atendimento,
            valor_total='150.00',
            forma_pagamento=Pagamento.FormaPagamento.PIX,
            status_pagamento=Pagamento.StatusPagamento.PENDENTE,
            data_pagamento=timezone.now(),
        )

        response = self.client.post(
            reverse('pagamento:delete_pagamento', args=[pagamento.pk]),
        )

        self.assertRedirects(
            response,
            reverse('pagamento:list_pagamento'),
        )
        self.assertFalse(Pagamento.objects.filter(pk=pagamento.pk).exists())

    def test_deleting_atendimento_removes_its_payment(self):
        pagamento = Pagamento.objects.create(
            atendimento=self.atendimento,
            valor_total='150.00',
            forma_pagamento=Pagamento.FormaPagamento.PIX,
            status_pagamento=Pagamento.StatusPagamento.PAGO,
            data_pagamento=timezone.now(),
        )

        self.atendimento.delete()

        self.assertFalse(Pagamento.objects.filter(pk=pagamento.pk).exists())
