#importar o módulo
import modulo


# algoritmo pricipal
modulo.limpar()
while True:
    print("1 - Calcular área do quadrilatero")
    print("2 -  Calcular área do circulo")
    print("3 -  Calcular comprimento do circulo")
    print("4 -  Sair do programa")
    opcao = input("Selecione a opção desejada: ").strip()
    match opcao:
        case "1":
            b = float(input("Informe a base: ").replace(",","."))
            h = float(input("Informe a altura: ").replace(",","."))
            a = modulo.a_quad(b, h)
            print(f"Área do quadrilátero é: {a}.")
            continue
        case "2":
            r = float(input("Informe o valor do raio: ").replace(",","."))
            a = modulo.a_circulo(r)
            print(f"Área do circulo: {a}.")
            continue
        case "3":
            r = float(input("Informe o raio: ").replace(",","."))
            a = modulo.comprimento_circulo(r)
            print(f"Comprimento do circulo: {a}")
            continue
        case "4":
            break
        case _:
            print("Opção inválida.")
            continue