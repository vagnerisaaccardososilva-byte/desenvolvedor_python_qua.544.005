import pyjokes
from translate import Translator

import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def gerar_piadas():
    tradutor = Translator(to_lang="pt")
    piada = pyjokes.get_joke()
    return tradutor.translate(piada)

def main():
    limpar()
    while True:
        print("0 - Sair do programa")
        print("1 - Gerar piadas aleatória")
        opcao = input("Opção desejada: ").strip()

        match opcao:
            case "0":
                break
            case "1":
                print(f"Piada: {gerar_piadas()}")
                continue
            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    main()