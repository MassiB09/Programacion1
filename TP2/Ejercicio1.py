'''lista = [1,2,3,4,4,4,4,4,4,44,4,4]

def eliminacion_valor(lista, valor):
    contador = lista.count(valor)
    for i in range(contador):
        lista.remove(valor)
    return lista

print(eliminacion_valor(lista, 4))
'''
def capicua(lista):
    resultado = True
    elementos = len(lista)
    mitad = elementos//2
    for i in range(mitad):
        if lista[i] != lista[elementos-1]:
            resultado = False
            break
        elementos -=1
    return resultado
            

print(capicua([50,17,91,17,50]))

