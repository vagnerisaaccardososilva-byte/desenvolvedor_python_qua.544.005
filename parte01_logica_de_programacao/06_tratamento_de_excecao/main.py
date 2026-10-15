# tratmento de exceção
try:
    nome = input("informe seu nome: ").strip().title()
    idade = int(input("Informe sua idade: "))

    print(f"Nome do usuário: {nome}")
    print(f"Idade do usuário: {idade} anos")
except Exception as e:
        print(f"Não foi possivelcexecutar a ação! {e}.")
finally:
    print("Programa finalizado com sucesso!")