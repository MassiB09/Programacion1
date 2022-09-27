def normalizar_numeros(lista_de_numeros):
    suma = sum(lista_de_numeros)
    for i in range(len(lista_de_numeros)):
        lista_de_numeros[i]/= suma
    return lista_de_numeros

print(normalizar_numeros([1,1,2]))