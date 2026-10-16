# crieem qual o usuario informe uma unica vez o nome e a idade, e em seguida, o programa exiba uma lsita de 5 filmes do cinema e suas respectivas salas e classificações indicativas.
# o usuario devera escolher a sala do filme imprima o inresso e encerre, senão o programa inpede a entrada do usuario e retorna a lista para que o mesmo possa escolher outro filmne.
import os
nome = input("Digite seu nome: ").strip().title()
print(f"{nome}, seja bem vindo ao cinema digital!")
print("Lista de filmes disponíveis")
print("Sala 1 - Up - Altas aventuras - Classsificação indicativa livre")
print("Sala 2 - A bela e a Fera - Classificação indicativa 10 anos")
print("Sala 3 - A Casa Monstro - Classificação indicativa 12 anos")
print("Sala 4 - A Casa do Medo - Classificação indicativa 16 anos")
print("Sala 5 - A Freira - Classificação indicativa 18 anos")

idade = int(input("Digite sua idade: "))
sala = int(input("Escolha uma sala entre 1 a 5: "))

if sala == 1:
    print("Up - Altas aventuras - Classsificação indicativa livre")
    print("Sala 1")
    print("Ingresso liberado!")
elif sala == 2:
    if idade >= 10:
        print("A bela e a Fera - Classificação indicativa 10 anos")
        print("Sala 2")
        print("Ingresso liberado!")
    else:
        print(f"O {nome} não tem a idade minima permitida. Ingresso não liberado")
elif sala == 3:
    if idade >= 12:
        print(" A Casa Monstro - Classificação indicativa 12 anos")
        print("Sala 3")
        print("Ingresso liberado!")
    else:
        print(f"O {nome} não tem a idade minima permitida. Ingresso não liberado")
elif sala == 4:
    if idade >= 16:
        print("A Casa do Medo - Classificação indicativa 16 anos")
        print("Sala 4")
        print("Ingresso liberado!")
    else:
        print(f"O {nome} não tem a idade minima permitida. Ingresso não liberado")
elif sala == 5:
    if idade >= 18:
        print(" A Freira - Classificação indicativa 18 anos")
        print("Sala 5")
        print("Ingresso liberado!")
    else:
        print(f"O {nome} não tem a idade minima permitida. Ingresso não liberado")
else:
    print("Sala inexistente!")
    print("Acesso negado!")
