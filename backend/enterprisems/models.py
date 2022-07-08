from django.db import models
from django.core.exceptions import ValidationError
from users.models import User
from validate_docbr import CNPJ
from enterprisems.utils import validate_phone


cnpj = CNPJ()


class ManageableEntity(models.Model):
    """
    Manegable model, can be a department or a company.

    Attributes:
        name (str): Name of entity.
        cnpj (str): CNPJ of entity.
        manager (User): Manager of entity.
        address (str): Address of entity.
        phone (str): Phone of entity.
    """

    name = models.CharField(verbose_name="Nome", max_length=100)
    cnpj = models.CharField(
        verbose_name="CNPJ",
        max_length=14,
        unique=True,
        null=True,
    )
    manager = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name="Gerente", null=True
    )
    address = models.CharField(verbose_name="Endereço", max_length=100, blank=True)
    phone = models.CharField(verbose_name="Telefone", max_length=20, blank=True)

    REQUIRED_FIELDS = ["name", "cnpj"]

    class Meta:
        abstract = True
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return self.name

    def cnpj_validator(self):
        if not self.cnpj:
            raise ValidationError("CNPJ é obrigatório.")
        if not cnpj.validate(self.cnpj):
            raise ValidationError("CNPJ inválido.")
        return True

    def associate_manager(self, manager: User):
        if type(manager) is not User:
            raise TypeError("Manager must be a User.")
        self.manager = manager
        self.save()

    def remove_manager(self):
        self.manager = None
        self.save()

    def set_address(self, address: str):
        self.address = address
        self.save()

    def set_phone(self, phone: str):
        if validate_phone(phone):
            self.phone = phone
            return True
        raise ValidationError("Telefone inválido.")

    def save(self, *args, **kwargs):
        self.cnpj_validator()
        if self.phone:
            self.set_phone(self.phone)
        super().save(*args, **kwargs)


class Company(ManageableEntity):
    """
    Modelo de empresa do sistema.

    Attributes:
        name (str): Name of entity.
        cnpj (str): CNPJ of entity.
        manager (User): Manager of entity.
        address (str): Address of entity.
        phone (str): Phone of entity.

    Methods:
        associate_manager(manager: User): Associate manager to company.
    """

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.name

    # Aqui poderia ser criado métodos específicos para modelo Empresa


class Department(ManageableEntity):
    """
    Modelo de departamento do sistema.

    Attributes:
        name (str): Name of entity.
        cnpj (str): CNPJ of entity.
        manager (User): Manager of entity.
        address (str): Address of entity.
        phone (str): Phone of entity.

    Methods:
        associate_manager(manager: User): Associate manager to department.
    """

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return self.name

    # Aqui poderia ser criado métodos específicos para modelo Departamento
