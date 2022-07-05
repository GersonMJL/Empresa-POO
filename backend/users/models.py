from validate_docbr import CPF
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


cpf = CPF()


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
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

        user = self.model(email=self.normalize_email(email), name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

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

        usuario = self.create_user(
            email=email, name=name, password=password, **extra_fields
        )
        usuario.is_active = True
        usuario.is_admin = True
        usuario.is_superuser = True
        usuario.save(self._db)
        return usuario


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

    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
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
        return cpf.validate(self.cpf)

    def save(self, *args, **kwargs):
        if self.cpf:
            if not self.validate_cpf():
                raise ValueError("CPF inválido")
        super(User, self).save(*args, **kwargs)


# class EmployeeDepartment(User):
#     """Modelo de funcionário do sistema."""

#     department = models.ForeignKey(
#         "users.Department", on_delete=models.CASCADE, verbose_name="Departamento"
#     )

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Funcionário"
#         verbose_name_plural = "Funcionários"
