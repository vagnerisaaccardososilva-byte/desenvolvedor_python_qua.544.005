#biblioteca
import os


# função
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def eq_1o_grau(a,b):
    return -b/a