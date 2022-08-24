import random

def lista_aleatoria():
    lista = []
    for i in range(50):
        lista.append(random.randint(1, 100))
    return lista

def tiene_repetidos(lista):
    resultado = False
    for i in lista:
        if lista.count(i) > 1:
            resultado = True
            break
    return resultado

def sin_repetidos(lista):
    resultado = []
    for i in lista:
        if i not in resultado:
            resultado.append(i)
    return resultado
            

print(lista_aleatoria())
print(tiene_repetidos([1,2]))
algo = sin_repetidos([1,1,1,2,2,3,5,6,7,7,8,3,2,2,2,2])
print(algo)