# Biblioteca
import json
import os


# lista
usuarios = []

# Limpa a tela
os.system("cls" if os.name == "nt" else "clear")

# loop
while True:
    # menu
    print("1 - Cadrastar novo usuario.")
    print("2 - Gravar Arquivo JSON.")
    print("3 -  Abrir arquivo JSON.")
    print("4 - Encerrar Programa.")
    opcao = input("Selecione a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            # novo usuario
            usuario = {}
            # insere usuario
            usuario['nome'] = input("Informe seu nome: ").strip().title()
            usuario['idade'] = int(input("Informe sua idade: "))
            usuario['email'] = input("Informe seu Email: ").strip().lower()
            usuario['cpf'] = input("Informe o CPF: ").strip()
            usuario['telefone'] = input("Informe seu Telefone: ").strip()

            #adiciona usuario
            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")
            #mensagem de confiramação 
            print(f"{usuario.get('nome')} cadastrado com sucesso!")
        case "2":
           for usuario in usuarios:
               for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
               print(f"{'-'*40}")
            #perguntar ao usuario se deseja prosseguir
           prosseguir = input("Deseja gravar os dados? (s/n)").strip().lower()
           if prosseguir == "s":
                os.system("cls" if os.name == "nt" else "clear")
                arquivo = input("Informe o nome do arquivo: ")
                with open(f"16_json/{arquivo}.json","w",encoding="utf-8") as f:
                    json.dump(usuarios, f)
                    print("Arquivo Json garvado com sucesso")
                    continue
           else:
                os.system("cls" if os.name == "nt" else "clear")
                continue
        case "3":
            os.system("cls" if os.name == "nt" else "clear")
            try:
              # informa o nome do arquivo que deseja abrir
              abrir = input("Informe o nome do aquivo que deseja abrir: ").strip()
              with open(f"16_json/{abrir}.json","r",encoding="utf-8") as f:
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
        case "4":
            break
        case _:
            print("Opção inválida.")