#superclasse / classe-pai
class Pessoa:
    def __init__(self,email,telefone,endereco):
        self.email = email
        self.telefone = telefone
        self.endereço = endereco

    # Metodo da class
    def exibir_dados(self):
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereço}")

#subclasse / classe-filha03_hernca/model.py
class PessoaFisica(Pessoa):
    def __init__(self, nome,cpf, email, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        super().__init__(email=email, telefone=telefone,endereco=endereco)

    def exibir_dados(self):
        print(f"{'-'*20} DADOS DO USUARIO {'-'*20}")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        super().exibir_dados()

class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, razao_social, nome_fantasia, email, telefone, endereco):
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        super().__init__(email=email, telefone=telefone, endereco=endereco)

    def exibir_dados(self):
        print(f"{'-'*20} DADOS DA EMPRESA {'-'*20}")
        print(f"Razão social: {self.razao_social}")
        print(f"Nome: {self.nome_fantasia}")
        print(f"CNPJ: {self.cnpj}")
        super().exibir_dados()