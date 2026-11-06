# bibliotecas
import os
import random

from model import Conta


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    # instancia a classe Conta
    cc = Conta(
        titular="",
        cpf="",
        agencia="1010-1",
        n_conta=f"{random.randint(10000,99999)}-1",
        saldo=0.0
    )

    limpar()

    # usuario informa seus dados
    cc.titular = input("Informe seu nome: ").strip().title()
    cc.cpf = input("Informe seu CPF: ").strip()

    limpar()

    while True:
        print(f"{'-'*20} COBRABANK {'-'*20}")
        print("0 - Sair do Programa")
        print("1 - Exibir dados do Programa ")
        print("2 - Depositar dinheiro ")
        print("3 - Sacar dinheiro ")
        opcao = input("Opção Desejada: ")
        limpar()
        match opcao:
            case '0':
                print("Programa encerrado.")
                break
            case '1':
                cc.consultar_conta()
                continue
            case '2':
                valor = float(input("Informe o valor do depósito: R$").replace(",","."))
                saldo = cc.depositar(valor)
                limpar()
                print(f"Depósito efetuado com secesso. saldo R$:{saldo:.2f}")
            case "3":
                valor = float(input("Informe o valor do saque: R$ ").replace(",","."))
                if valor <= cc.saldo:
                    saldo = cc.sacar(valor)
                    limpar()
                    print(f"Saque efetuado com sucesso. Saldo atual: R$ {cc.saldo:.2f}")
                else:
                    print("Não foi possível efetuar o saque.")
                    continue
            case _:
                print("Opção inválida.")
if __name__ == "__main__":
    main()