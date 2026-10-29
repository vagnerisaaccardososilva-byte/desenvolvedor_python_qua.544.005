# TODO: parte 03 atividade 02
'''
Crie um programa em que o usuario informe um numero inteiro e o programa e o programa retorne a sequencia fibonacci.
'''
print(f"{'-'*30}")
print("Sequencia de fibonacci")
print(f"{'-'*30}")
n = int(input("Informe um número inteiro: "))
a = 0
b = 1
for i in range(n):
    print(a)
    proximo = a+b
    a = b
    b = proximo