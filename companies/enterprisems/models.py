from django.db import models
from django.core.exceptions import ValidationError
import validate_cpf

"""
Tipos de pessoas que podem ser cadastradas no sistema:
"""
ROLES_CHOICES = (
    ("1", "Gerente de Departamento"),
    ("2", "Gerente de Empresa"),
    ("3", "Funcionário"),
)


class Department(models.Model):
    """
    Department model

    Attributes:
        name (str): Name of the department
        code_id (AutoField): Code of the department
    """

    code_id = models.AutoField(primary_key=True, verbose_name="Código", unique=True)
    name = models.CharField(verbose_name="Nome", max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    """
    Department model

    Attributes:
        name (str): Name of the company
        code_id (AutoField): Code of the company
    """

    code_id = models.AutoField(primary_key=True, verbose_name="Código", unique=True)
    name = models.CharField(verbose_name="Nome", max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Person(models.Model):
    cpf = models.CharField(
        verbose_name="CPF", primary_key=True, unique=True, max_length=11
    )
    role = models.CharField(verbose_name="Cargo", choices=ROLES_CHOICES, max_length=100)
    allowance = models.BooleanField(verbose_name="Abono", default=False)
    name = models.CharField(verbose_name="Nome", max_length=100)
    telephone = models.IntegerField(verbose_name="Telefone", max_length=11)
    email = models.EmailField(verbose_name="E-mail", max_length=100)
    street = models.CharField(verbose_name="Rua", max_length=100)
    city = models.CharField(verbose_name="Cidade", max_length=100)
    state = models.CharField(verbose_name="Estado", max_length=100)
    wage = models.DecimalField(verbose_name="Salário", decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name

    def validate_cpf(self):
        if validate_cpf.validate_cpf(self.cpf):
            return True
        return False

    def save(self, *args, **kwargs):
        if self.validate_cpf():
            super(self).save(*args, **kwargs)
        else:
            raise ValidationError("CPF inválido")


class Employee(Person):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DepartmentManager(Person):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CompanyManager(Person):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
