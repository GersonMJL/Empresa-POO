from models.funcionario.base import FuncionarioBase


class Motorista(FuncionarioBase):
    def __init__(
        self,
        nome=None,
        telefone=None,
        email=None,
        rua=None,
        cidade=None,
        estado=None,
        abono=False,
    ):
        super().__init__(
            nome=nome,
            telefone=telefone,
            email=email,
            rua=rua,
            cidade=cidade,
            estado=estado,
            abono=abono,
            cargo="Motorista",
            salario=2030,
        )

    def __str__(self):
        return f"{self.pessoa.nome}, {self.pessoa.telefone}, {self.pessoa.email}, {self.cargo}, {self.salario}"
