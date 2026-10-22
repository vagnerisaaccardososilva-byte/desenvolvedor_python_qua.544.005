#biblioteca
import os


#limpa terminal
os.system("cls" if os.name == "nt" else "clear")

#loop
while True:
    #menu
    print(" 1 - Gravar arquivo")
    print(" 2 - Abrir e ler arquivo")
    print(" 3 - sair do Programa")
    opcao = input("opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    #verificar opções
    match opcao:
        case "1":
            # informa o texto a ser gravado
            novo_texto = input("Digite aqui o seu texto: ")
            # informa o nome do arquivo
            novo_arquivo = input("Informe o nome do Arquivo: ").strip()
 
            # Grava o novo arquivo
            with open(f"15_criando_arquivo/{novo_arquivo}.txt","w",encoding="utf-8") as f:
                f.write(novo_texto)
            continue
        case "2":
            abrir_arquivo = input("informe o nome do .txt que deseja abrir: ").strip()
            with open(f"15_criando_arquivo/{abrir_arquivo}.txt","r", encoding="utf-8") as f:
                texto = f.read()
            print(texto)   
        case "3":
            break
        case _:
            print("Opção inválida.")