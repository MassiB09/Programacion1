def matriz_g(n, matriz):
    direccion = 'derecha'
    for f in range(n):
        matriz.append([0]*n)
    tamanio = len(matriz)
    f = 0
    c = 0
    
    for i in range(tamanio**2):
        matriz[f][c] = i+1
        if direccion == 'derecha':
            if c+1 < tamanio and matriz[f][c+1] == 0:
                c +=1
            else:
                direccion = 'abajo'
                f +=1
        elif direccion == 'abajo':
            if f+1 < tamanio and matriz[f+1][c] == 0:
                f +=1
            else:
                direccion = 'izquierda'
                c-=1
        elif direccion == 'izquierda':
            if c > 0 and matriz[f][c-1] == 0:
                c -=1
            else:
                direccion = 'arriba'
                f -=1
        elif direccion == 'arriba':
            if f > 0 and matriz[f-1][c] == 0:
                f -=1
            else:
                direccion = 'derecha'
                c +=1
        
    for i in range(n):
        for j in range(n):
            print('%3d' %matriz[i][j],end='')
            if j == n-1:
                print()


matriz = []
n = int(input('Ingrese n: '))
matriz_g(n,matriz)