from validate_docbr import CPF
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


cpf = CPF()


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
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, cpf, password=None, **extra_fields):
        """Cria um superusuário com email, nome e senha.

        Args:
            email (str): Email do usuário.
            nome (str): Nome do usuário.
            password (str, optional): Senha do usuário. Defaults to None.

        Returns:
            Usuario: Objeto de usuário criado.
        """

        usuario = self.create_user(
            email=email, name=name, cpf=cpf, password=password, **extra_fields
        )
        usuario.is_active = True
        usuario.is_admin = True
        usuario.is_superuser = True
        usuario.save(self._db)
        return usuario


class Profile(models.Model):

    id_count = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"


class User(AbstractUser):
    """Modelo de usuário do sistema."""

    profile = models.OneToOneField(
        Profile, on_delete=models.SET_NULL, null=True)
    username = None
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(verbose_name="Email", max_length=100)
    cpf = models.CharField(
        verbose_name="CPF",
        unique=True,
        max_length=11,
        primary_key=True,
    )
    name = models.CharField(verbose_name="Nome", max_length=100)
    is_active = models.BooleanField(verbose_name="Ativo", default=True)
    is_admin = models.BooleanField(verbose_name="Administrador", default=False)

    objects = UserManager()

    USERNAME_FIELD = "cpf"
    REQUIRED_FIELDS = ["name", "email"]

    def __str__(self):
        return self.name

    def validate_cpf(self):
        return cpf.validate(self.cpf)

    def save(self, *args, **kwargs):
        if self.cpf:
            if not self.validate_cpf():
                raise ValueError("CPF inválido")

        self.profile = Profile.objects.create()
        super(User, self).save(*args, **kwargs)
