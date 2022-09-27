import random
def mostrar(n,matriz):
    for i in range(n):
        for j in range(n):
            print('%3d' %matriz[i][j],end='')
            if j == n-1:
                print()

def crearMatriz(n):
    matriz = []
    for i in range(n):
        matriz.append([])
    return matriz

lista_repetidos = []
n = int(input('Ingrese n: '))
matriz = crearMatriz(n)
for i in range(n):
    while len(matriz[i]) < n:
        elemento = random.randint(0,n**2)
        if elemento not in lista_repetidos:
            lista_repetidos.append(elemento)
            matriz[i].append(elemento)
mostrar(n,matriz)