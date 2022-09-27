def intercalar(lista1, lista2):
    n = 1
    for elemento in lista2:
        lista1[n:n] = [elemento]
        n +=2
    return lista1

print(intercalar([8,1,3], [5,9,7]))