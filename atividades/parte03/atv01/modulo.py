# TODO: parte 03 atividade 01
'''
Crie um programa que calcule o  peso de uma pessoa em um planeta do sistema solar escolhido por ela
'''
# NOTE: pesquisar aceleração da gravidade em cada planeta.
# NOTE: inclua a lua

import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def peso_astro(massa, gravidade):
    return massa * gravidade