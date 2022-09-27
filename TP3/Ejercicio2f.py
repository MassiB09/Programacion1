def mostrar(n,matriz):
    for i in range(n):
        for j in range(n):
            print('%3d' %matriz[i][j],end='')
            if j == n-1:
                print()

def matrizf(n, matriz):
    contador = int(n*(n+1)/2) #1 3 6 10 15 21 28 36
    for f in range(n):
        matriz.append([])
        for c in range(n-f):
            matriz[f].append(contador)
            contador -=1
        while len(matriz[f]) < n:
            matriz[f][0:0] = [0]
    matriz = matriz[::-1]

    mostrar(n,matriz)

n = int(input('Ingrese n: '))

matriz = []
matrizf(n, matriz)