from django.db import models

# from django.core.exceptions import ValidationError
# import validate_cpf


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
