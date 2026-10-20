#Lista
cidades = [
    'Taguatinga',
    'Plano Piloto',
    'Gama',
    'Santa Maria',
    'Samabaia',
    'planaltina',
    'Plano Piloto',
    'Brazlândia',
    'Plano Piloto',
    'Santa Maria'
]

# Usuario  informa o item a ser pesquisado
item = input("Informe a cidade a ser pesquisada: ").strip().title()

#verificar quantas vezes o termo foi encontrado
print(f"{item} foi encontrado {cidades.count(item)} vezes na lista.")