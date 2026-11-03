import os

from model import PessoaFisica, PessoaJuridica


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
   # Instanciar as classe
   usuario = PessoaFisica(nome="",cpf="",email="",telefone="",endereco="")
   empresa = PessoaJuridica(cnpj="",razao_social="", nome_fantasia="", email="",telefone="",endereco="")

   # Informe os dados do usuario
   limpar()
   print(f"{'-'*20} Informe os dados do usuáruio {'-'*20}\n")
   usuario.nome = input("Informe o nome do usúario: ").strip().title()
   usuario.cpf = input("Informe o CPF do usúario: ").strip()
   usuario.email = input("Informe o Email do usúario: ").strip().lower()
   usuario.telefone = input("Informe o telefone do usúario: ").strip()
   usuario.endereço = input("Informe o endereço do usúario: ").strip().title()

    # Informar os dados da empresa
   limpar()
   print(f"{'-'*20} Informe os dados d aempresa {'-'*20}")
   empresa.razao_social = input("Informe a Razão Social: ").strip() 
   empresa.nome_fantasia = input("Informe o nome: ").strip().title() 
   empresa.cnpj = input("Informe o CNPJ: ").strip() 
   empresa.email = input("Informe o email: ").strip().lower() 
   empresa.telefone = input("Informe o telefone: ").strip() 
   empresa.endereço = input("Informe o endereço: ").strip()

   limpar()
   usuario.exibir_dados()
   empresa.exibir_dados()

if __name__ == "__main__":
    main()