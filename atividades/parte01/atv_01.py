#crie um programa que receba nome, altura em metros, massa em kg do usuario, calcule seu IMC (indice da massa corporal) e finalize informando o diagnostico do usuario com base no valor do IMC (se está magro, gordo ou so peso ideal)

nome = input("Informe o seu nome: ").strip().title()
altura = float(input("Digite sua altura em metros ").replace(",","."))
massa = float(input("Digite sua massa corporal em kg: ").replace(",","."))

imc = massa / (altura * altura)

print(f"Seu IMC é: {imc:.2f}!")

if imc < 18.5:
    print(f"O {nome} está abaixo da massa corporal indicada")

elif imc < 25.0:
    print(f"O {nome} está com amassa ideal")

elif imc < 30.0:
    print(f"O {nome} está com sobrepeso")

elif imc < 35.0:
    print(f"O {nome} está com obesidade grau I")

elif imc < 40.0:
    print(f"O {nome} está com obesidade grau II (severa)")

else:
    print(f"O {nome} está com obesidade severa")