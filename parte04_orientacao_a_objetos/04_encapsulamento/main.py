from model import Pessoa


def main():
    usuario = Pessoa(nome="",idade=0,cpf="",telefone="",email="")

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int(input("Informe a idade: "))
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.telefone = input("Informe o telefone: ").strip()
    usuario.email = input("Informe o E-mail: ").strip().lower()

    print(f"Nome: {usuario.nome}")
    print(f"Idade: {usuario.idade}")
    print(f"CPF: {usuario.cpf}")
    print(f"Telefone: {usuario.telefone}")
    print(f"E-mail: {usuario.email}")


if __name__ == "__main__":
    main()