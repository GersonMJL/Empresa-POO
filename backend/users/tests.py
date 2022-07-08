from django.test import TestCase

# from enterprisems.tests.utils import TestUtils
from django.core.exceptions import ValidationError
from users.models import User
from validate_docbr import CPF
from faker import Faker

cpf = CPF()
fake = Faker("pt_BR")


class TestUser(TestCase):
    def test_create_user(self):
        User.objects.create_user(
            email=fake.email(),
            name=fake.name(),
            cpf=cpf.generate(),
            password="123456",
        )
        self.assertEqual(User.objects.count(), 1)

    def test_invalid_cpf(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email=fake.email(),
                name=fake.name(),
                cpf="12345678901",
                password="123456",
            )

    def test_invalid_email(self):
        with self.assertRaises(ValidationError):
            User.objects.create_user(
                email="sdfsdfsdf",
                name=fake.name(),
                cpf=cpf.generate(),
                password="123456",
            )
