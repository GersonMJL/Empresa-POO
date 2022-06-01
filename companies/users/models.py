import validate_cpf
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, groups=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Usuários precisam de email")
        if not name:
            raise ValueError("Usuários precisam de nome")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        if groups:
            for group in groups:
                user.groups.add(group)

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField(
        verbose_name="CPF", primary_key=True, unique=True, max_length=11
    )
    email = models.EmailField(verbose_name="Email", max_length=100, unique=True)
    name = models.CharField(verbose_name="Nome", max_length=100)
    groups = models.ManyToManyField("Group", verbose_name="Grupos", blank=True)
    is_active = models.BooleanField(verbose_name="Ativo", default=True)
    is_admin = models.BooleanField(verbose_name="Administrador", default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def cpf_validate(self):
        if validate_cpf.validate_cpf(self.cpf):
            return True
        return False

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
