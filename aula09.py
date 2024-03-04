# Operador Lógico "and"

login = input("Informe Login: ")
senha = int(input("Informe a senha: "))

if login == "Admin" and senha == 1234:
    print("Entrou no Sistema")
else:
    print("Login ou senha invalido")