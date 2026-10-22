#biblioteca
import os

#lista de usuarios
usuarios = []

#limpar terminal
os.system("cls" if os.name == "nt" else "clear")
#loop
while True:
    # menu
    print("1 - Cadastrar novo usuário")
    print("2 -  Exibir lista de usuários")
    print("3 - Sair do programa")
    opcao = input("Opção desejada: ").strip()

    #varificar opção escolhida
    match opcao:
        case "1":
            # Criar novo diciponaroio
            usuario = {}
            #insere dados do usuario
            usuario['nome'] = input("Informe seu nome: ").strip().title()
            usuario['idade'] = int(input("Informe sua idade: "))
            usuario['email'] = input("Informe seu email: ").strip().lower()
            usuario['CPF'] = input("Informe o numero do seu CFP: ").strip()

            #adicionando o usuario na lista
            usuarios.append(usuario)

            #mensagem de sucesso
            print(f"{usuario.get('nome')} cadastrado com sucesso")
            continue
        case "2":
           #exibe lista de usuarios
           for usuario in usuarios:
               for chave, valor in usuario.items():
                   print(f"{chave.capitalize()}: {valor}")
                   print(f"{'-'*40}")
        case "3":
            break
        case _:
            print("Opção inválida.")