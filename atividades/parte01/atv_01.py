#crie um programa que receba nome, altura em metros, massa em kg do usuario, calcule seu IMC (indice da massa corporal) e finalize informando o diagnostico do usuario com base no valor do IMC (se está magro, gordo ou so peso ideal)

nome = input("Informe o seu nome: ").strip().title()
altura = float(input("Digite sua altura em metros ").replace(",","."))
peso = float(input("Digite seu peso em kg: ").replace(",","."))

imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:2}")

if imc < 18.5:
    print(f"O {nome} está abaixo do peso")
elif imc < 18.5:
    print(f"O {nome} está com o peso ideal")
elif imc < 25.0:
    print(f"O {nome} está com sobrepeso")
elif imc < 30.0:
    print(f"O {nome} está com obesidade grau I")
elif imc < 35.0:
    print(f"O {nome} está com obesidade grau II (severa)")
else:
    print(f"O {nome} está com obesidade severa")
