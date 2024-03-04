"""
Introdução ao try/except

try -> Tentar executar o código
except -> ocorreu algum erro ao tentar executar

"""

# numero = input("Informe um numero: ")

# try:
#     numero_float = float(numero)
#     print(f"o dobre de {numero} é {int(numero) * 2:.2f}")
# except:
#     print("isso não é um numero")

class CadastroCliente():
    
    def __init__(self,email,nome,senha,login):
        self.email = email
        self.nome = nome
        self.senha = senha
        self.login = login
    
    def cadastrarCliente(self):
        
        
        try:
            self.email = input("Informe seu email: ")
            self.nome = input("Informe seu nome: ")
            self.senha = int(input("Informe seu senha: (SOMENTE COM NUMEROS)"))
            self.login = input("Informe seu login: ")
            cliente1.imprimirCliente()
        except:
            print("Informe sua senha somente com numeros")
    
    def imprimirCliente(self):
        
        print("Email: ", self.email)
        print("Nome: ", self.nome)
        print("Senha: ", self.senha)
        print("Login: ", self.login)
        
        
cliente1 = CadastroCliente(email="", nome="", senha="", login="")
cliente1.cadastrarCliente()
    

