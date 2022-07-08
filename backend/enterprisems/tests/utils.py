from faker import Faker
from validate_docbr import CPF, CNPJ

from users.models import User

fake = Faker("pt_BR")
cpf = CPF()
cnpj = CNPJ()


class TestUtils:
    @staticmethod
    def create_user(email, name, cpf, is_superuser=False):
        """Cria um usuário com email, nome e senha.
        Args:
            email (str): Email do usuário.
            nome (str): Nome do usuário.
            password (str, optional): Senha do usuário é 'segredo'.
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
            cpf=cpf,
        )
        user.set_password("segredo")

        user.is_active = True
        user.is_superuser = is_superuser
        user.save()

        return user

    @staticmethod
    def create_random_user(is_superuser=False):
        """Cria um usuário no banco de dados.
        Returns:
            Usuario: Objeto do usuário criado.
        """

        nome = fake.name()
        email = fake.email()
        random_cpf = cpf.generate()
        is_superuser = is_superuser
        return TestUtils.create_user(nome, email, random_cpf, is_superuser)
