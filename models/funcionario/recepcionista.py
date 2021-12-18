from models.funcionario.base import FuncionarioBase


class Recepcionista(FuncionarioBase):
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
            cargo="Recepcionista",
            salario=2000,
        )

    def __str__(self):
        return (
            f"{self.nome}, {self.telefone}, {self.email}, {self.cargo}, {self.salario}"
        )
