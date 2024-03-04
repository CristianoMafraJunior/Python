# OR - se uma condição for verdadeira toda a expressão é verdadeira

email = input("Digite seu Email: ")
senha = input("Digite sua senha: ")

if email == "cristiano@gmail.com" or senha == "1234":
    print("Entrou")
else:
    print("Erro senha ou email incorretos")