from django.test import TestCase
from enterprisems.tests.utils import TestUtils
from validate_docbr import CPF

class TestUser(TestCase):

    def setUp(self):
        TestUtils.create_user(email="
