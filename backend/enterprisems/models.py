from django.db import models
from django.core.exceptions import ValidationError
from users.models import User
from validate_docbr import CNPJ


cnpj = CNPJ()


class Department(models.Model):
    """
    Department model

    Attributes:
        name (str): Name of the department
        code_id (AutoField): Code of the department
    """

    name = models.CharField(verbose_name="Nome", max_length=100)
    cnpj = models.CharField(
        verbose_name="CNPJ",
        max_length=14,
        unique=True,
        blank=True,
        null=True,
    )
    manager = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name="Gerente", null=True
    )
    address = models.CharField(verbose_name="Endereço", max_length=100, blank=True)
    phone = models.CharField(verbose_name="Telefone", max_length=20, blank=True)

    REQUIRED_FIELDS = ["name", "cnpj"]

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return self.name

    def cnpj_validator(self):
        if not cnpj.validate(self.cnpj):
            raise ValidationError("CNPJ inválido.")

    def save(self, *args, **kwargs):
        self.cnpj_validator()
        if self.manager.role != User.ROLE_CHOICES[0][0]:
            raise ValidationError("Usuário não é gerente de Departamento")
        super().save(*args, **kwargs)


class Company(models.Model):
    """
    Department model

    Attributes:
        name (str): Name of the company
        code_id (AutoField): Code of the company
    """

    name = models.CharField(verbose_name="Nome", max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    cnpj = models.CharField(
        verbose_name="CNPJ",
        max_length=14,
        unique=True,
        blank=True,
        null=True,
    )
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(verbose_name="Endereço", max_length=100, blank=True)
    phone = models.CharField(verbose_name="Telefone", max_length=20, blank=True)

    REQUIRED_FIELDS = ["name", "cnpj"]

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.name

    def cnpj_validator(self):
        if not cnpj.validate(self.cnpj):
            raise ValidationError("CNPJ inválido.")

    def save(self, *args, **kwargs):
        self.cnpj_validator()
        if self.manager.role != User.ROLE_CHOICES[0][1]:
            raise ValidationError("Usuário não é gerente de Empresa")
        super().save(*args, **kwargs)
