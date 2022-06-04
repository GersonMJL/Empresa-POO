import validate_cpf
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, nome, password=None):
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
        if not nome:
            raise ValueError("Usuários precisam de um nome.")

        usuario = self.model(email=self.normalize_email(email), nome=nome)
        usuario.set_password(password)
        usuario.save(using=self._db)

        return usuario

    def create_superuser(self, email, nome, password=None):
        """Cria um superusuário com email, nome e senha.
        Args:
            email (str): Email do usuário.
            nome (str): Nome do usuário.
            password (str, optional): Senha do usuário. Defaults to None.
        Returns:
            Usuario: Objeto de usuário criado.
        """

        usuario = self.create_user(email, nome=nome, password=password)
        usuario.is_active = True
        usuario.is_admin = True
        usuario.is_superuser = True
        usuario.save(using=self._db)
        return usuario


class User(AbstractUser):
    DEPARTMENT_MANAGER = 1
    COMPANY_MANAGER = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (DEPARTMENT_MANAGER, "Gerente de Departamento"),
        (COMPANY_MANAGER, "Gerente de Empresa"),
        (EMPLOYEE, "Funcionário"),
    )

    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, null=True, verbose_name="Cargo"
    )
    cpf = models.CharField(
        verbose_name="CPF", primary_key=True, unique=True, max_length=11
    )
    email = models.EmailField(verbose_name="Email", max_length=100, unique=True)
    name = models.CharField(verbose_name="Nome", max_length=100)
    is_active = models.BooleanField(verbose_name="Ativo", default=True)
    is_admin = models.BooleanField(verbose_name="Administrador", default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "cpf"]

    def __str__(self):
        return self.name

    def validate_cpf(self):
        if validate_cpf.validate_cpf(self.cpf):
            return True
        return False

    def save(self, *args, **kwargs):
        if not self.validate_cpf():
            raise ValueError("CPF inválido")
        super(User, self).save(*args, **kwargs)
