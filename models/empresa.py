class Empresa:
    def __init__(self, nome: str, cnpj: int):
        self.nome = nome
        self.cnpj = cnpj
        self.departamentos = []

    def adicionar_departamento(self, departamento):
        if len(self.departamentos) >= 9:
            print("Não é possível adicionar mais departamentos")
            pass
        else:
            self.departamentos.append(departamento)

    def transferir_funcionario(
        self, funcionario, departamento_atual, departamento_novo
    ):
        if departamento_atual in self.departamentos:
            if departamento_novo in self.departamentos:
                departamento_atual.remover_funcionario(funcionario)
                departamento_novo.adicionar_funcionario(funcionario)
            else:
                print("Departamento destino não existe")
                print(departamento_novo)
        else:
            print("Departamento origem não existe")
