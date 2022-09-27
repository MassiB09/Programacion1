def sin_repetidos(lista,lista_2):
    resultado = []
    for i in lista:
        if i not in lista_2:
            resultado.append(i)
    return resultado

lista = ['hola','chau','god', 'hola']
lista_2 = ['gaston','hola','sol','hola','god']

print(lista)
print(lista_2)
print(sin_repetidos(lista,lista_2))