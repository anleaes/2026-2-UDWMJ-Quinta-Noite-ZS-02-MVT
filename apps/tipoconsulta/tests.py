from django.test import TestCase
from django.urls import reverse

from .models import TipoConsulta


class TipoConsultaViewsTests(TestCase):
    def test_list_tipo_consulta(self):
        TipoConsulta.objects.create(nome='Consulta geral')

        response = self.client.get(reverse('tipoconsulta:list_tipo_consulta'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Consulta geral')

    def test_add_tipo_consulta(self):
        response = self.client.post(
            reverse('tipoconsulta:add_tipo_consulta'),
            {'nome': 'Dermatológica', 'descricao': 'Consulta de pele.'},
        )

        self.assertRedirects(
            response,
            reverse('tipoconsulta:list_tipo_consulta'),
        )
        self.assertTrue(
            TipoConsulta.objects.filter(nome='Dermatológica').exists(),
        )

    def test_add_tipo_consulta_requires_name(self):
        response = self.client.post(
            reverse('tipoconsulta:add_tipo_consulta'),
            {'nome': '', 'descricao': ''},
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('nome', response.context['form'].errors)
        self.assertEqual(TipoConsulta.objects.count(), 0)

    def test_edit_tipo_consulta(self):
        tipo_consulta = TipoConsulta.objects.create(nome='Consulta')

        response = self.client.post(
            reverse(
                'tipoconsulta:edit_tipo_consulta',
                args=[tipo_consulta.pk],
            ),
            {'nome': 'Consulta geral', 'descricao': 'Atendimento clínico.'},
        )

        self.assertRedirects(
            response,
            reverse('tipoconsulta:list_tipo_consulta'),
        )
        tipo_consulta.refresh_from_db()
        self.assertEqual(tipo_consulta.nome, 'Consulta geral')

    def test_delete_requires_confirmation(self):
        tipo_consulta = TipoConsulta.objects.create(nome='Retorno')

        response = self.client.get(
            reverse(
                'tipoconsulta:delete_tipo_consulta',
                args=[tipo_consulta.pk],
            ),
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            TipoConsulta.objects.filter(pk=tipo_consulta.pk).exists(),
        )

    def test_delete_tipo_consulta(self):
        tipo_consulta = TipoConsulta.objects.create(nome='Emergência')

        response = self.client.post(
            reverse(
                'tipoconsulta:delete_tipo_consulta',
                args=[tipo_consulta.pk],
            ),
        )

        self.assertRedirects(
            response,
            reverse('tipoconsulta:list_tipo_consulta'),
        )
        self.assertFalse(
            TipoConsulta.objects.filter(pk=tipo_consulta.pk).exists(),
        )
