def mostrar(n,matriz):
    for i in range(n):
        for j in range(n):
            print('%3d' %matriz[i][j],end='')
            if j == n-1:
                print()

def matrizh(n, matriz):
    columna = 0
    fila = 0
    limite = 1
    aux = 0
    limite_lateral = 0
    for f in range(n):
        matriz.append([0]*n)
    for i in range(1,(n*n)+1):
        matriz[fila][columna] = i
        if columna - 1 < limite_lateral:
            if fila + 1 == len(matriz):
                columna = len(matriz) - 1
                aux += 1
            else:
                columna = fila + 1
            if aux < 1:
                fila = 0
            else:
                fila = aux
            if limite < len(matriz):
                limite +=1
        elif fila + 1 < limite:
            fila +=1
            columna -=1
            if fila == len(matriz)-1 and not(columna - 1 < limite_lateral):
                limite_lateral +=1
    mostrar(n,matriz)

n = int(input('Ingrese n: '))

matriz = []
matrizh(n, matriz)
