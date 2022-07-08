from django.test import TestCase
from enterprisems.tests.utils import TestUtils
from validate_docbr import CPF
from faker import Faker
from users.models import User, Profile, UserManager

fake = Faker()
cpf = CPF()


class TestUser(TestCase):

    def test_create_user(self):
        UserManager().create_user(cpf=cpf.generate(), email=fake.email(), name=fake.name())
        self.assertEqual(Profile().objects.count(), 1)
