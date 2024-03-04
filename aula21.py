"""
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido 
e continue pedindo até que o usuário informe um valor válido.
"""

while True:
    nota = float(input("Informe sua nota: "))
    
    if 0 <= nota <=10:
        print("Nota Valida")
        print("Programa Finalizado")
        break
    else: 
        print("Informe a nota novamente")
        
"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
while True:
    nome_usuario = input("Informe seu nome: ")
    senha = input("Informe sua Senha: ")

    if nome_usuario == senha:
        print("Nome e senha estão iguais")
        
    else:
        print("Cadastro Feito")
        break

"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';         
"""
while True:
    nome = input("Informe seu Nome: (MAIOR QUE 3 CARACTERES) ")
    if len(nome) > 3:
        print("Informação Correta")
    idade = int(input("Informe sua Idade: (ENTRE 0 A 150)"))
    if 0 <= idade <= 150:
        print("Informação Correta")
    salario = float(input("Informe seu Salario: (MAIOR QUE ZERO)"))
    if salario > 0:
        print("Informação Correta")
    sexo = input("Informe seu sexo: (F/M) ")
    if sexo == "F".lower() and "M".lower():
        print("Informação Correta")
    estado_civil = input("Informe seu Estado Civil: (S/C/V/D)")
    if estado_civil.lower() in ['s','c','v','d']:
        print("Informação Correta")
        break

