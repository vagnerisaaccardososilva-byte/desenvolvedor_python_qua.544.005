# biblioteca
import os

#lista
nomes = ['isaac', 'Cybelle', 'Ariana', 'Vagner', 'Gabriel', 'Maria', 'Jarson']

os.system("cls" if os.name == "nt" else "clear")


# loop
while True:
    #exibe a lista original 
    for n, nome in enumerate(nomes):
        print(f"Indice {n}: {nome}")
    #Menu
    print("1 - Alterar item da lista")
    print("2 - finalizar")
    opcao = input("Opção desejada: ").strip()

    #verificar a opção escolhida
    match opcao:
        case "1":
        #informe o indice a ser alterado
            indice = int(input("Informe o indice a ser alterado: "))
        # informe novo valor
            nomes[indice] = input("Informe novo nome: ").strip().title()
            os.system("cls" if os.name == "nt" else "clear")
            continue
        case "2":
               os.system("cls" if os.name == "nt" else "clear")
               #exibir nova lista
               for n, nome in enumerate(nomes):
                    print(f"Indice{n}: {nomes}")
               break 
        case _:
            print("Opção invalida")
            continue
         
            
    