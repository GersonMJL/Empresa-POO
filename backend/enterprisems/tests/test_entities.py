from django.test import TestCase
from enterprisems.tests.utils import TestUtils
from enterprisems.models import Department, Company
from users.models import User
from validate_docbr import CPF, CNPJ
from faker import Faker

fake = Faker("pt_BR")
cpf = CPF()
cnpj = CNPJ()
FAKE_PHONE = "11 99999-9999"


class TestEnterprise(TestCase):
    def test_create_department(self):
        Department_obj = {
            "name": "Teste",
            "cnpj": cnpj.generate(),
        }
        Department.objects.create(**Department_obj)
        self.assertEqual(Department.objects.count(), 1)

    def test_create_department_without_cnpj(self):
        Department_obj = {
            "name": "Teste",
        }

        self.assertRaises(Exception, Department.objects.create, **Department_obj)

    def test_create_department_without_name(self):
        Department_obj = {
            "cnpj": cnpj.generate(),
        }
        Department.objects.create(**Department_obj)

    def test_create_department_without_cnpj_and_name(self):
        Department_obj = {}

        self.assertRaises(Exception, Department.objects.create, **Department_obj)

    def test_create_department_all_fields(self):

        user_obj = {
            "email": fake.email(),
            "name": fake.name(),
            "cpf": cpf.generate(mask=True),
        }

        user = TestUtils.create_user(**user_obj)

        self.assertEqual(user.email, user_obj["email"])
        self.assertEqual(User.objects.count(), 1)

        Department_obj = {
            "name": "Teste",
            "cnpj": cnpj.generate(),
            "manager": user,
            "address": fake.address(),
            "phone": FAKE_PHONE,
        }
        tested_department = Department.objects.create(**Department_obj)
        self.assertEqual(tested_department.cnpj, Department_obj["cnpj"])
        self.assertEqual(Department.objects.count(), 1)
        self.assertEqual(tested_department.manager, user)

    def test_associate_manager(self):
        user_obj = {
            "email": fake.email(),
            "name": fake.name(),
            "cpf": cpf.generate(mask=True),
        }

        user = TestUtils.create_user(**user_obj)

        self.assertEqual(user.email, user_obj["email"])
        self.assertEqual(User.objects.count(), 1)

        Department_obj = {
            "name": "Teste",
            "cnpj": cnpj.generate(),
            "address": fake.address(),
            "phone": FAKE_PHONE,
        }
        tested_department = Department.objects.create(**Department_obj)
        self.assertEqual(tested_department.cnpj, Department_obj["cnpj"])
        self.assertEqual(Department.objects.count(), 1)

        tested_department.associate_manager(user)
        self.assertEqual(tested_department.manager, user)

    def test_set_address(self):
        user_obj = {
            "email": fake.email(),
            "name": fake.name(),
            "cpf": cpf.generate(mask=True),
        }

        user = TestUtils.create_user(**user_obj)

        self.assertEqual(user.email, user_obj["email"])
        self.assertEqual(User.objects.count(), 1)

        Department_obj = {
            "name": "Teste",
            "cnpj": cnpj.generate(),
            "manager": user,
            "phone": FAKE_PHONE,
        }
        tested_department = Department.objects.create(**Department_obj)
        self.assertEqual(tested_department.cnpj, Department_obj["cnpj"])
        self.assertEqual(Department.objects.count(), 1)

        fake_address = fake.street_name()
        tested_department.set_address(fake_address)
        self.assertEqual(tested_department.address, fake_address)

    def test_set_phone(self):
        user_obj = {
            "email": fake.email(),
            "name": fake.name(),
            "cpf": cpf.generate(mask=True),
        }

        user = TestUtils.create_user(**user_obj)

        self.assertEqual(user.email, user_obj["email"])
        self.assertEqual(User.objects.count(), 1)

        Department_obj = {
            "name": "Teste",
            "cnpj": cnpj.generate(),
            "manager": user,
            "address": fake.address(),
        }
        tested_department = Department.objects.create(**Department_obj)
        self.assertEqual(tested_department.cnpj, Department_obj["cnpj"])
        self.assertEqual(Department.objects.count(), 1)

        fake_phone = "11 99999-9999"
        tested_department.set_phone(fake_phone)
        self.assertEqual(tested_department.phone, fake_phone)

    def test_invalid_cnpj(self):
        Department_obj = {
            "name": "Teste",
            "cnpj": "12345678901234",
        }

        self.assertRaises(Exception, Department.objects.create, **Department_obj)

    def test_invalid_phone(self):
        Department_obj = {
            "name": "Teste",
            "cnpj": cnpj.generate(),
            "phone": "12345678901234",
        }

        self.assertRaises(Exception, Department.objects.create, **Department_obj)

    def test_remove_manager(self):
        user_obj = {
            "email": fake.email(),
            "name": fake.name(),
            "cpf": cpf.generate(mask=True),
        }

        user = TestUtils.create_user(**user_obj)

        self.assertEqual(user.email, user_obj["email"])
        self.assertEqual(User.objects.count(), 1)

        Department_obj = {
            "name": "Teste",
            "cnpj": cnpj.generate(),
            "manager": user,
            "address": fake.address(),
            "phone": FAKE_PHONE,
        }
        tested_department = Department.objects.create(**Department_obj)
        self.assertEqual(tested_department.cnpj, Department_obj["cnpj"])
        self.assertEqual(Department.objects.count(), 1)
        self.assertEqual(tested_department.manager, user)

        tested_department.remove_manager()
        self.assertEqual(tested_department.manager, None)


class TestCompany(TestCase):
    def test_create_company(self):
        company_obj = {
            "name": "Teste",
            "cnpj": cnpj.generate(),
        }
        Company.objects.create(**company_obj)
        self.assertEqual(Company.objects.count(), 1)

    def test_create_company_without_cnpj(self):
        company_obj = {
            "name": "Teste",
        }

        self.assertRaises(Exception, Company.objects.create, **company_obj)

    def test_create_company_without_name(self):
        company_obj = {
            "cnpj": cnpj.generate(),
        }
        Company.objects.create(**company_obj)

    def test_create_company_without_cnpj_and_name(self):
        company_obj = {}

        self.assertRaises(Exception, Company.objects.create, **company_obj)

    def test_create_company_all_fields(self):

        user_obj = {
            "email": fake.email(),
            "name": fake.name(),
            "cpf": cpf.generate(mask=True),
        }

        user = TestUtils.create_user(**user_obj)

        self.assertEqual(user.email, user_obj["email"])
        self.assertEqual(User.objects.count(), 1)

        company_obj = {
            "name": "Teste",
            "cnpj": cnpj.generate(),
            "manager": user,
            "address": fake.address(),
            "phone": FAKE_PHONE,
        }
        tested_company = Company.objects.create(**company_obj)
        self.assertEqual(tested_company.cnpj, company_obj["cnpj"])
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(tested_company.manager, user)

    def test_associate_manager(self):
        user_obj = {
            "email": fake.email(),
            "name": fake.name(),
            "cpf": cpf.generate(mask=True),
        }

        user = TestUtils.create_user(**user_obj)

        self.assertEqual(user.email, user_obj["email"])
        self.assertEqual(User.objects.count(), 1)

        company_obj = {
            "name": "Teste",
            "cnpj": cnpj.generate(),
            "address": fake.address(),
            "phone": FAKE_PHONE,
        }
        tested_company = Company.objects.create(**company_obj)
        self.assertEqual(tested_company.cnpj, company_obj["cnpj"])
        self.assertEqual(Company.objects.count(), 1)

        tested_company.associate_manager(user)
        self.assertEqual(tested_company.manager, user)

    def test_set_address(self):
        user_obj = {
            "email": fake.email(),
            "name": fake.name(),
            "cpf": cpf.generate(mask=True),
        }

        user = TestUtils.create_user(**user_obj)

        self.assertEqual(user.email, user_obj["email"])
        self.assertEqual(User.objects.count(), 1)

        company_obj = {
            "name": "Teste",
            "cnpj": cnpj.generate(),
            "manager": user,
            "phone": FAKE_PHONE,
        }
        tested_company = Company.objects.create(**company_obj)
        self.assertEqual(tested_company.cnpj, company_obj["cnpj"])
        self.assertEqual(Company.objects.count(), 1)

        fake_address = fake.street_name()
        tested_company.set_address(fake_address)
        self.assertEqual(tested_company.address, fake_address)

    def test_set_phone(self):
        user_obj = {
            "email": fake.email(),
            "name": fake.name(),
            "cpf": cpf.generate(mask=True),
        }

        user = TestUtils.create_user(**user_obj)

        self.assertEqual(user.email, user_obj["email"])
        self.assertEqual(User.objects.count(), 1)

        company_obj = {
            "name": "Teste",
            "cnpj": cnpj.generate(),
            "manager": user,
            "address": fake.address(),
        }
        tested_company = Company.objects.create(**company_obj)
        self.assertEqual(tested_company.cnpj, company_obj["cnpj"])
        self.assertEqual(Company.objects.count(), 1)

        fake_phone = "11 99999-9999"
        tested_company.set_phone(fake_phone)
        self.assertEqual(tested_company.phone, fake_phone)

    def test_invalid_cnpj(self):
        company_obj = {
            "name": "Teste",
            "cnpj": "12345678901234",
        }

        self.assertRaises(Exception, Company.objects.create, **company_obj)

    def test_invalid_phone(self):
        company_obj = {
            "name": "Teste",
            "cnpj": cnpj.generate(),
            "phone": "12345678901234",
        }

        self.assertRaises(Exception, Company.objects.create, **company_obj)

    def test_remove_manager(self):
        user_obj = {
            "email": fake.email(),
            "name": fake.name(),
            "cpf": cpf.generate(mask=True),
        }

        user = TestUtils.create_user(**user_obj)

        self.assertEqual(user.email, user_obj["email"])
        self.assertEqual(User.objects.count(), 1)

        company_obj = {
            "name": "Teste",
            "cnpj": cnpj.generate(),
            "manager": user,
            "address": fake.address(),
            "phone": FAKE_PHONE,
        }
        tested_company = Company.objects.create(**company_obj)
        self.assertEqual(tested_company.cnpj, company_obj["cnpj"])
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(tested_company.manager, user)

        tested_company.remove_manager()
        self.assertEqual(tested_company.manager, None)
