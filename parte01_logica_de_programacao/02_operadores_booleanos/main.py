# and =  e (quando duas ou mais condicionais sejam verdadeiras)
# or = ou (quando uma das duas precisam ser verdadeiras)
# not = não (quando é obrigatóriamente falsa)

# exemplo.01
# eclaração de variavéis

nome = input("Informe seu nome: ").strip().title()
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura em metros: ").replace(",","."))

# verificação se o pagante possui os requisitos
if idade >= 12 and altura >= 1.35:
    print(f"{nome} a sua entrada está autorizada! Seja bem vindo(a)")
else:
    print(f"{nome} a sua entrada não foi autorizada!")