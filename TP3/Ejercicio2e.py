def mostrar(n,matriz):
    for i in range(n):
        for j in range(n):
            print('%3d' %matriz[i][j],end='')
            if j == n-1:
                print()

def matriz0(n, matriz):
    indicador = True
    contador = 1
    for i in range(n):
        matriz.append([])
        if i % 2 == 0:
            indicador = True
        else:
            indicador = False
        for j in range(n):
            if indicador:
                matriz[i].append(0)
                indicador = False
            else:
                matriz[i].append(contador)
                contador +=1
                indicador = True
    mostrar(n, matriz)

n = int(input('Ingrese n: '))

matriz = []
matriz0(n, matriz)

