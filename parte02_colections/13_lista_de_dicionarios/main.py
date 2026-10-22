#lista de dicionarios
usuarios = [
    {
        'nome': "Vagner Isaac",
        'idade': 18,
        'email': "vagner@gmail.com"
    },
    {
        'nome': "Joana da Silva",
        'idade': 41,
        'email': "joana@gmail.com"
     },
     {
         'nome': "Karol com k",
         'idade': 18,
         'email': "karol@gmail.com"
     },
]

for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")