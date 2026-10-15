# Declaração de variaveis
x = float(input("Informe um numero:").replace(",","."))
y = float(input("Informe outro numero:").replace(",","."))

#menu
print(f"{'-'*20} Escolha uma opoeração {'-'*20}")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")

operador = input("Operação desejada: ").strip()

# match...case
match operador:
    case "1":
        print(f"Resultado da soma: {x+y}")
    case "2":
        print(f"Resultado da subtração: {x-y}")
    case "3":
        print(f"Resultado da multiplicação: {x*y}")
    case "4":
        print(f"Resultado da divisão: {x/y}")
    case _:
        print("Operação inválida")