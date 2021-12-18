from models.endereco import Endereco
from models.pessoa import Pessoa


class FuncionarioBase:
    def __init__(
        self,
        cargo: str,
        abono: bool,
        nome: str = None,
        telefone: int = None,
        email: str = None,
        salario: int = None,
        rua: str = None,
        cidade: str = None,
        estado: str = None,
    ):
        self.salario = salario
        if self.validate_salario():

            if abono and salario:
                salario = salario + 300

            # Se todos os atributos forem passados, cria um objeto Pessoa e Endereco
            if (
                nome
                and telefone
                and email
                and cargo
                and salario
                and rua
                and cidade
                and estado
            ):
                self.pessoa = Pessoa(nome, telefone, email)
                self.endereco = Endereco(rua, cidade, estado)
                self.cargo = cargo
                self.salario = salario
            # Se forem passados apenas os atributos de Pessoa e salario, cria um objeto Pessoa
            elif nome and telefone and email and salario:
                self.pessoa = Pessoa(nome, telefone, email)
                self.salario = salario
            # Se forem passados apenas os atributos de Pessoa e cargo, cria um objeto Pessoa
            elif nome and telefone and email and salario:
                self.pessoa = Pessoa(nome, telefone, email)
                self.cargo = cargo
            # Se nenhum atributo for passado, não cria nenhum objeto
            else:
                print("Atributos insuficientes")
                exit()
        else:
            print("Salario invalido")
            exit()

    # Método get atributos
    def get_funcionario(self):
        return f"Nome: {self.pessoa.nome}, Rua: {self.endereco.rua}, Cargo: {self.cargo}, Salário Final: {self.salario}"

    def update_funcionario(
        self,
        nome=None,
        telefone=None,
        email=None,
        cargo=None,
        salario=None,
        rua=None,
        cidade=None,
        estado=None,
    ):
        if nome:
            self.pessoa.nome = nome
        if telefone:
            self.pessoa.telefone = telefone
        if email:
            self.pessoa.email = email
        if cargo:
            self.cargo = cargo
        if salario:
            self.salario = salario
        if rua:
            self.endereco.rua = rua
        if cidade:
            self.endereco.cidade = cidade
        if estado:
            self.endereco.estado = estado

    def validate_salario(self):
        if self.salario < 0:
            return False
        else:
            return True
