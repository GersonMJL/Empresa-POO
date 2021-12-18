from models.funcionario.porteiro import Porteiro
from models.funcionario.recepcionista import Recepcionista
from models.funcionario.motorista import Motorista
from models.departamento import Departamento
from models.empresa import Empresa


def main():

    # Primeiro objetivo:

    # Criação de objetos
    porteiro = Porteiro(
        nome="João",
        telefone=999999999,
        email="email1@email.com",
        rua="Rua Fulano de Tal",
        cidade="Arapiraca",
        estado="AL",
        abono=True,
    )
    recepcionista = Recepcionista(
        "Maria",
        999999999,
        "email2@email.com",
        "Rua Fulano de Tal",
        "Arapiraca",
        "AL",
        True,
    )
    motorista = Motorista(
        "Pedro",
        999999999,
        "email3@email.com",
        "Rua Fulano de Tal",
        "Arapiraca",
        "AL",
        True,
    )

    # Criação de departamento
    departamento = Departamento("Departamento de Geral")

    # Adicionando funcionários ao departamento
    departamento.adicionar_funcionario(porteiro)
    departamento.adicionar_funcionario(recepcionista)
    departamento.adicionar_funcionario(motorista)

    # Imprimindo dados dos funcionários
    print("\nDados dos funcionários de Departamento Geral:")
    departamento.get_funcionarios()

    # Segundo objetivo:

    # Criar uma empresa
    empresa = Empresa(nome="Empresa de Teste", cnpj=12345678901234)

    # Criar departamentos com funcionários e adicionar a empresa
    departamento1 = Departamento("Departamento de Vendas")
    departamento2 = Departamento("Departamento de Marketing")
    departamento3 = Departamento("Departamento de Compras")

    # Adicionando departamentos a empresa
    empresa.adicionar_departamento(departamento1)
    empresa.adicionar_departamento(departamento2)
    empresa.adicionar_departamento(departamento3)

    # Adicionando funcionários aos departamentos
    departamento1.adicionar_funcionario(porteiro)
    departamento2.adicionar_funcionario(recepcionista)
    departamento3.adicionar_funcionario(motorista)

    # Transferir funcionário de um departamento para outro
    empresa.transferir_funcionario(porteiro, departamento1, departamento2)

    # Imprimindo dados dos funcionários
    print("\nDados dos funcionários de Departamento de Vendas:")
    departamento1.get_funcionarios()
    print("\nDados dos funcionários de Departamento de Marketing:")
    departamento2.get_funcionarios()
    print("\nDados dos funcionários de Departamento de Compras:")
    departamento3.get_funcionarios()


main()
