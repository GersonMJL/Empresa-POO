class Pessoa:
    # Método set
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"{self.nome}, {self.telefone}, {self.email}"
