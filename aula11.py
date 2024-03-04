nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

if nome and idade:
    print(f"Seu nome é {nome}")
    nome_invertido = nome[::-1]
    print(f"Seu nome invertido é {nome_invertido}")
    print(f"Seu nome tem {(len(nome))} letras")
    print(f"A ultima letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios.")