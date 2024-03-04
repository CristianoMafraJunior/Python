"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.

Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar se a letra digitada está na palavra secreta.

"""
contador = 0
palavra_secreta = "Carro"
palavra_adivinhada = ['_'] * len(palavra_secreta)

while contador < 5:
    letra = input("Informe uma letra: ")
    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_adivinhada[i] = letra
        print(f"A palavra até agora: {''.join(palavra_adivinhada)}")
        if '_' not in palavra_adivinhada:
            print("Parabéns, você acertou a palavra!")
            break
    else:
        print("Letra incorreta")
        contador += 1

if '_' in palavra_adivinhada:
    print("Você perdeu! A palavra secreta era:", palavra_secreta)

