# biblioteca
import os

# LIsta vazia
tarefas = []

# limpar o terminal
os.system("cls" if os.name == "nt" else "clear")

# loop
while True:
    print("1- Inserir nova tarefa na lista")
    print("2- Finalizar e exibir a lista")
    opcao = input("Opção desejada: ").strip() #informa a opção deesejada

    # verificar a opção informada
    match opcao:
        case "1":
            nova_tarefa = input("Informe a nova tarefa: ")
            tarefas.append(nova_tarefa) # insere item na lista
            continue #retorna para o inicio do loop
        case "2":
            os.system("cls" if os.name == "nt" else "clear")

            #exibe a lista
            for n, tarefa in enumerate(tarefas, start=1):
                print(f"{n}º tarefa: {tarefa}")
            break
        case _:
            print("Opção invalida")
        

