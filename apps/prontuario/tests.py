from datetime import date
from tempfile import TemporaryDirectory

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import default_storage
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone

from animal.models import Animal
from atendimento.models import Atendimento
from cliente.models import Cliente
from tipoanimal.models import TipoAnimal
from veterinario.models import Veterinario

from .models import Prontuario


class ProntuarioViewsTests(TestCase):
    def setUp(self):
        self.media_directory = TemporaryDirectory()
        self.media_settings = override_settings(
            MEDIA_ROOT=self.media_directory.name,
        )
        self.media_settings.enable()

    def tearDown(self):
        self.media_settings.disable()
        self.media_directory.cleanup()

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
        cls.atendimento = Atendimento.objects.create(
            data_hora=timezone.now(),
            motivo='Consulta de rotina',
            animal=cls.animal,
            veterinario=cls.veterinario,
        )

    def prontuario_form_data(self, **overrides):
        data = {
            'descricao': 'Avaliação clínica inicial.',
            'prescricao': 'Repouso e retorno em sete dias.',
            'data_registro': '2026-01-02',
            'atendimento': self.atendimento.pk,
        }
        data.update(overrides)
        return data

    def diagnostico_file(self):
        return SimpleUploadedFile(
            'diagnostico.pdf',
            b'%PDF-1.4 arquivo de teste',
            content_type='application/pdf',
        )

    def test_list_prontuarios(self):
        prontuario = Prontuario.objects.create(
            **self.prontuario_form_data(),
            diagnostico=self.diagnostico_file(),
        )

        response = self.client.get(reverse('prontuario:list_prontuario'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Avaliação clínica inicial.')
        self.assertContains(response, 'Rex')
        prontuario.diagnostico.delete(save=False)

    def test_add_prontuario(self):
        data = self.prontuario_form_data()
        data['diagnostico'] = self.diagnostico_file()
        response = self.client.post(
            reverse('prontuario:add_prontuario'),
            data,
        )

        self.assertRedirects(
            response,
            reverse('prontuario:list_prontuario'),
        )
        self.assertTrue(
            Prontuario.objects.filter(atendimento=self.atendimento).exists(),
        )
        prontuario = Prontuario.objects.get(atendimento=self.atendimento)
        prontuario.diagnostico.delete(save=False)

    def test_one_prontuario_per_atendimento(self):
        Prontuario.objects.create(
            **self.prontuario_form_data(),
            diagnostico=self.diagnostico_file(),
        )

        data = self.prontuario_form_data()
        data['diagnostico'] = self.diagnostico_file()
        response = self.client.post(
            reverse('prontuario:add_prontuario'),
            data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('atendimento', response.context['form'].errors)
        Prontuario.objects.get(atendimento=self.atendimento).diagnostico.delete(
            save=False,
        )

    def test_edit_prontuario(self):
        prontuario = Prontuario.objects.create(
            **self.prontuario_form_data(),
            diagnostico=self.diagnostico_file(),
        )

        response = self.client.post(
            reverse('prontuario:edit_prontuario', args=[prontuario.pk]),
            self.prontuario_form_data(
                descricao='Avaliação atualizada.',
            ),
        )

        self.assertRedirects(
            response,
            reverse('prontuario:list_prontuario'),
        )
        prontuario.refresh_from_db()
        self.assertEqual(prontuario.descricao, 'Avaliação atualizada.')
        prontuario.diagnostico.delete(save=False)

    def test_delete_requires_confirmation(self):
        prontuario = Prontuario.objects.create(
            **self.prontuario_form_data(),
            diagnostico=self.diagnostico_file(),
        )

        response = self.client.get(
            reverse('prontuario:delete_prontuario', args=[prontuario.pk]),
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Prontuario.objects.filter(pk=prontuario.pk).exists())
        prontuario.diagnostico.delete(save=False)

    def test_delete_prontuario(self):
        prontuario = Prontuario.objects.create(
            **self.prontuario_form_data(),
            diagnostico=self.diagnostico_file(),
        )
        diagnostico_path = prontuario.diagnostico.name

        response = self.client.post(
            reverse('prontuario:delete_prontuario', args=[prontuario.pk]),
        )

        self.assertRedirects(
            response,
            reverse('prontuario:list_prontuario'),
        )
        self.assertFalse(Prontuario.objects.filter(pk=prontuario.pk).exists())
        self.assertFalse(default_storage.exists(diagnostico_path))

    def test_deleting_atendimento_removes_its_prontuario_file(self):
        prontuario = Prontuario.objects.create(
            **self.prontuario_form_data(),
            diagnostico=self.diagnostico_file(),
        )
        diagnostico_path = prontuario.diagnostico.name

        self.atendimento.delete()

        self.assertFalse(Prontuario.objects.filter(pk=prontuario.pk).exists())
        self.assertFalse(default_storage.exists(diagnostico_path))
