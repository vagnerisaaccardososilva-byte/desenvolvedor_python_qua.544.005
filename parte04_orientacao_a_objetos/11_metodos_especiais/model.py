class Pessoa:
    # construtor
    def __init__(self,nome,idade,altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

        #metodo string
    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {len(self)}\nAltura: {float(self)}"
    
        #metodo length
    def __len__(self):
        return self.idade 

    #metodo float
    def __float__(self):
        return self.altura

    # destrutor
    def __def__(self):
        print(f"Objeto {self.nome} Destruido com sucesso")