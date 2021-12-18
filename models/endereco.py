class Endereco:
    def __init__(self, rua, cidade, estado):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f"{self.rua}, {self.cidade} - {self.estado}"
