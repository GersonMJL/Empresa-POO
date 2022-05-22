from django.db import models
from django.core.exceptions import ValidationError
import validate_cpf


class Department(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Person(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    role = models.CharField(verbose_name="Cargo", max_length=100)
    allowance = models.BooleanField(verbose_name="Abono", default=False)
    name = models.CharField(max_length=100)
    telephone = models.IntegerField()
    email = models.EmailField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    wage = models.DecimalField(decimal_places=2)

    def __str__(self):
        return self.name

    def validate_cpf(self):
        if validate_cpf.validate_cpf(self.cpf):
            return True
        return False

    def save(self, *args, **kwargs):
        if self.validate_cpf():
            super(Employee, self).save(*args, **kwargs)
        else:
            raise ValidationError("CPF inválido")


class CompanyManager(Person):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Employee(Person):
    cpf = models.CharField(max_length=11, primary_key=True)
    role = models.CharField(verbose_name="Cargo", max_length=100)
    allowance = models.BooleanField(verbose_name="Abono", default=False)
    name = models.CharField(max_length=100)
    telephone = models.IntegerField()
    email = models.EmailField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    wage = models.DecimalField(decimal_places=2)
