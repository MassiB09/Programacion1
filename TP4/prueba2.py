import random

def sin_cuatro(elemento):
    resultado = True
    while elemento != 0:
        aux = elemento % 10
        elemento = elemento // 10
        if aux == 4:
            resultado = False
            break
    return resultado

def crear_lista_al_azar():
    lista = [i for i in [random.randint(1000, 9999) for elemento in range(10)] if sin_cuatro(i)]
#    lista = list(filter(sin_cuatro, lista))
    return lista

print(crear_lista_al_azar())