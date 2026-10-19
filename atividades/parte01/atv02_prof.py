import os
#limpar o terminal
os.system("cls"if os.name == "nt" else "clear")
#dados
nome = input("Digite seu nome: ").strip().title()
idade = int(input("Informe sua idade: "))
idade_minima = None

while True:
    #menu de filmes
    print(f"{'-'*20} CINE COBRA")
    print("Sala 1 - Up - Altas aventuras - Classsificação indicativa livre")
    print("Sala 2 - A bela e a Fera - Classificação indicativa 10 anos")
    print("Sala 3 - A Casa Monstro - Classificação indicativa 12 anos")
    print("Sala 4 - A Casa do Medo - Classificação indicativa 16 anos")
    print("Sala 5 - A Freira - Classificação indicativa 18 anos")

    #usuario informe a sala
    sala = input("Informe a sala desejada: ").strip()

    #atribui a idade minima do filme
    match sala:
        case "1":
            idade_minima = 0
        case "2":
            idade_minima = 10
        case "3":
            idade_minima = 12
        case "4":
            idade_minima = 16
        case "5":
            idade_minima = 18
        case _:
            print("Sala inexistente")
            idade_minima = idade + 1

    if idade >= idade_minima:
        print(f"Ingresso impresso para: {nome}")
        print("tenha um bom filme")
        break
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"ingresso negado para {nome}")
        print("Você não tem a idade mínima permitida")
        print("Por favor, escolha outro filme. obrigado pela compreensão.")