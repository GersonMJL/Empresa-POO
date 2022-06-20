import validate_cpf
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, name, cpf, password=None, **extra_fields):
        """Cria um usuário com email, nome e senha.
        Args:
            email (str): Email do usuário.
            nome (str): Nome do usuário.
            password (str, optional): Senha do usuário. Defaults to None.
        Raises:
            ValueError: Levanta exceção caso o email seja vazio.
            ValueError: Levanta exceção caso o nome seja vazio.
        Returns:
            Usuario: Objeto de usuário criado.
        """

        if not email:
            raise ValueError("Usuários precisam de um email.")
        if not name:
            raise ValueError("Usuários precisam de um nome.")

        user = self.model(
            email=self.normalize_email(email), name=name, cpf=cpf, **extra_fields
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, name, password, **extra_fields):
        """Cria um superusuário com email, nome e senha.

        Args:
            email (str): Email do usuário.
            nome (str): Nome do usuário.
            password (str, optional): Senha do usuário. Defaults to None.

        Returns:
            Usuario: Objeto de usuário criado.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(("Superuser must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(("Superuser must have is_superuser=True"))

        return self.create_user(email, name, password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    """Modelo de usuário do sistema."""

    DEPARTMENT_MANAGER = 1
    COMPANY_MANAGER = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (DEPARTMENT_MANAGER, "Gerente de Departamento"),
        (COMPANY_MANAGER, "Gerente de Empresa"),
        (EMPLOYEE, "Funcionário"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name="Email", max_length=100, unique=True)
    cpf = models.CharField(
        verbose_name="CPF",
        unique=True,
        max_length=11,
        blank=True,
        null=True,
    )
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, null=True, verbose_name="Cargo"
    )
    name = models.CharField(verbose_name="Nome", max_length=100)
    is_active = models.BooleanField(verbose_name="Ativo", default=True)
    is_admin = models.BooleanField(verbose_name="Administrador", default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name

    def validate_cpf(self):
        return validate_cpf.validate_cpf(self.cpf)

    def save(self, *args, **kwargs):
        if self.cpf:
            if not self.validate_cpf():
                raise ValueError("CPF inválido")
        super(User, self).save(*args, **kwargs)
