 # declaração de variáveis

nome = input("informe seu nome: ").strip().title()
idade = int(input("Informe sua idade: "))

# OPerador ternário

print(f"{nome} {'é maior de idade' if idade >= 18 else 'é menor de idade'}.")

# stript (tira os espaços) title (converte as iniciais para maiusculas)
