#TODO: parte 02 atividade 01
'''
crie um programa que faça as seguites operações:
- Cadastra o novo usuario (nom, email, telefone, cpf)
- lista todos os usuarios cadastrado 
- altera dados de um usuario
- exclui um usuario
- grava dados de todos os usuarios em um .json
- abre aquivos .json e lista todos os usuarios cadastrado nele
'''

import json
import os 
usuarios = []
os.system("cls" if os.name == "nt" else "clear")

while True:
    print("1 - Cadastrar novo usuário")
    print("2 - Ver lista de todos os usuários")
    print("3 - alterar dados de um usuário")
    print("4 - Excluir um usuário")
    print("5 - Gravar dados")
    print("6 - Abrir programa")
    print("7 - Encerrar programa")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
           usuario = {}
           usuario['nome'] = input("Informe seu nome: ").strip().title()
           usuario['email'] = input("Informe seu email: ").strip().lower()
           usuario['telefone'] = input("Informe seu telefone para contato: ").strip()
           usuario['cpf'] = input("Informe seu CPF: ").strip()

           usuarios.append(usuario)
           os.system("cls" if os.name == "nt" else "clear")
           print(f"{usuario.get('nome')} cadastrado com sucesso!")
           continue
        case "2":
            for n, usuario in enumerate(usuarios,start=1):
                print(f"Usuario{n}")
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                    print(f"{'-'*40}")
                    continue
        case "3":
            for n, usuario in enumerate(usuarios,start=1):
                print(f"alterar {n}: {usuario['nome']}")
            alterar = int(input("Informe o usuário que deseja alterar: "))
            if 1 <= alterar <= len(usuarios):
                print("1 - Alterar o email")
                print("2 - alterar telefone")
                opcao_alterar = input("Selecione a opção desejada: ")

                os.system("cls" if os.name == "nt" else "clear")
                if opcao_alterar == "1":
                    usuarios[alterar - 1]["email"] = input("Informe o novo Email: ").strip().lower()
                    print("Email alterado com sucesso!")
                elif opcao_alterar == "2":
                    usuarios[alterar - 1]["telefone"] = input("Informe o novo número: ").strip()
                    print("Telefone alterado com sucesso!")
                else:
                    print("Opção inválida.")
        case"4":
            for n, usuario in enumerate(usuarios,start=1):
                print(f"Excluir {n}: {usuario['nome']}")
            excluir = int(input("Informe o usuario a ser excluído: "))
            if 1 <= excluir <= len(usuarios):
                usuario_excluido = usuarios.pop(excluir - 1)
                print(f"Usuário {usuario_excluido ['nome']} exluido com sucesso!")
            else:
                print("Usuário inválido.")
                continue
        case "5":
            prosseguir = input("Deseja gravar dados? (s/n)").strip().lower()
            if prosseguir == "s":
                os.system("cls" if os.name == "nt" else "clear")
                arquivo = input("Informe o nome do arquivo: ")
                with open(f"atv01/{arquivo}.json","w",encoding="utf-8") as f:
                    json.dump(usuarios, f)
                    print("Arquivo gravado com sucesso!")
                    continue
                
        case "6":
            os.system("cls" if os.name == "nt" else "clear")
            try:
              # informa o nome do arquivo que deseja abrir
              abrir = input("Informe o nome do aquivo que deseja abrir: ").strip()
              with open(f"atv01/{abrir}.json","r",encoding="utf-8") as f:
                  usuarios = json.load(f)
                  #Exibe dados do arquivo
              for usuario in usuarios:
                  for chave, valor in usuario.items():
                      print(f"{chave.capitalize()}: {valor}")
                  print(f"{'-'*40}")
                  continue
            except Exception as e:
                print(f"Não foi possível abrir o arquivo. {e}.")
            continue
        case "7":
            break
            
            
                
