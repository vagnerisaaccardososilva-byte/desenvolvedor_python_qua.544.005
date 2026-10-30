import os

from model import Pessoa


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    limpar()

    usuario = Pessoa(nome='',idade=0,email='')

    usuario.nome = input("informe o nome: ").strip().title()
    usuario.idade = input("Informe a idade: ")
    usuario.email = input("Informe o emai: ").strip().lower()
    
    print(usuario.cumprimentatar())

if __name__ == "__main__":
    main()