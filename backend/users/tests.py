from django.test import TestCase
from faker import Faker
from validate_docbr import CPF, CNPJ

from users.models import User

fake = Faker("pt_BR")
cpf = CPF()
cnpj = CNPJ()


@staticmethod
def create_user(email, name, type, is_superuser=False):
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

    user = User(
        email=email,
        name=name,
    )
    user.set_password("segredo")

    user.is_active = True
    user.is_superuser = is_superuser
    user.save()

    return user
