# Classe
class Pessoa:
    # contrutor
    def __init__(self,nome,idade,email,cpf):
        # atributos
        self.nome = nome
        self.idade= idade
        self.email = email
        self.cpf = cpf

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Email: {self.email}")
        print(f"CPF: {self.cpf}")


def main():
    # instanciar a classe
    usuario = Pessoa(nome="",idade=0,email="",cpf="")

    #insere valaores npos atributos
    usuario.nome = input("informe o nome: ").strip().title()
    usuario.idade = int(input("Infome a idade: "))
    usuario.email = input("Informe o email: ").strip().lower()
    usuario.cpf = input("Informe o CPF: ").strip()

    # exibe os atributos na tela
    usuario.exibir_dados()

if __name__ == "__main__":
    main()