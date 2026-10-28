# biblioteca 
import math
import os


# função
def raiz(n):
    return math.sqrt(n)

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

#algoritimo principal
def main():
    limpar()
    n = int(input("Informe um número inteiro: "))
    print(f"Raiz de {n} é {raiz(n)}")


#algoritmo principal
if __name__ == "__main__":
        main()