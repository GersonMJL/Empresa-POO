# Criar classe de Departamento


class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def remover_funcionario(self, funcionario):
        self.funcionarios.remove(funcionario)

    def get_departamento(self):
        return self.nome, self.codigo

    def get_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario.get_funcionario())

    def update_departamento(self, nome=None, codigo=None):
        if nome:
            self.nome = nome
        if codigo:
            self.codigo = codigo
