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
    print("6 - Encerrar programa")
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
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                    print(f"{'-'*40}")
                    continue
        case "3":
            for n, nome in enumerate(usuarios):
                print(f"alterar {n}: {usuario}")
            alterar = int(input("Informe o usuário que sofrerar a alteração: "))
            usuarios[alterar] = input("Informe o novo nome: ").strip().title()
            usuarios[alterar] = input("Informe o novo email: ").strip().lower()
            usuarios[alterar] = input("Informe o novo telefone: ").strip()
            usuarios[alterar] = input("Informe o novo CPF: ").strip()
            os.system("cls" if os.name == "nt" else "clear")
            continue
        case"4":
            #TODO
            pass
        case "5":
            #TODO - 
            pass
        case "6":
            break
           #TODO - linha 40 com problema na volta da verificaçãao da lista