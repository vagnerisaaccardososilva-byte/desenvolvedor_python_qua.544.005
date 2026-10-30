class Pessoa:
    def __init__(self,nome,idade,email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def cumprimentatar(self):
        return f"Olá, boa tarde. Meu nome é {self.nome}, tenho {self.idade}  anos, e meu email é {self.email}."