lista_numeros = []
print(lista_numeros)
numeros = 1,2,3,5
lista_numeros.append(numeros)

print(lista_numeros)

lista_numeros2 = []
lista_numeros2.extend(lista_numeros)
del lista_numeros[0]
lista_numeros.append(1)

lista_numeros.append("Valor Ajustado")
print(lista_numeros)
print(lista_numeros2)

lista_numeros.pop()
print(lista_numeros)
