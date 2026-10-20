# Lista
frutas = [
    'Maçã',
    'Pera',
    'Maracujá',
    'Melancia',
    'Limão',
    'Goiaba',
    'Morango'
]

while True:
    for n, fruta in enumerate(frutas):
        print(f"Indice {n}: {fruta}")

        # menu
    print("1 - Excluir fruta")
    print("2 - encerrar programa")
    opcao = input("Opção desejada; ").strip()

    # verificar opoção
    match opcao:
        case "1":
            indice = int(input("Informe o indice a ser excluido: "))
            del(frutas[indice])
            print("Fruta excluida com sucesso!")
            continue
        case "2":
            break
        case _:
            print("Opção inválida!")
            continue