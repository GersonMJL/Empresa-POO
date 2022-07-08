from django.test import TestCase
from enterprisems.tests.utils import TestUtils
from enterprisems.models import Department
from validate_docbr import CPF, CNPJ

cpf = CPF()
cnpj = CNPJ()


class TestEnterprise(TestCase):
    def setUp(self):
        TestUtils.create_user(email="teste@teste.com", name="Teste", cpf=cpf.generate())
        TestUtils.create_user(
            email="teste2@teste2.com", name="Teste2", cpf=cpf.generate()
        )

    def test_create_department(self):
        Department_obj = {
            "name": "Teste",
            "cnpj": cnpj.generate(),
        }
        Department.objects.create(**Department_obj)
        self.assertEqual(Department.objects.count(), 1)
