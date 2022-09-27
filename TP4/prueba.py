import random

def imprimirmatriz(mat):
    for f in mat:
        for c in f:
            print("%3d" %c, end="")
        print()
    print()

def determinarcuadradomagico(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    esmagico = True
    # Control de filas
    sumafilas = []
    for fila in matriz:
        sumafilas.append(sum(fila))
    if min(sumafilas)!=max(sumafilas):
        esmagico = False
    # Control de columnas
    sumacolumnas = []
    for c in range(columnas):
        suma = 0
        for f in range(filas):
            suma = suma + matriz[f][c]
        sumacolumnas.append(suma)
    if min(sumacolumnas)!=max(sumacolumnas):
        esmagico = False
    # Diagonales
    principal = 0
    secundaria = 0
    for f in range(filas):
        principal += matriz[f][f]
        secundaria += matriz[f][filas-f-1]
    if principal!=secundaria:
        esmagico = False
    return esmagico

# Programa principal
n = int(input("Ingrese el tamaño de la matriz: "))
print()
# Creamos la matriz ya terminada usando listas por comprensión anidadas
'''mat = [[random.randint(0,9) for c in range(n)] for f in range(n)]
'''
mat = [ [4,3,8],
        [9,5,1],
        [2,7,6] ]

imprimirmatriz(mat)
if determinarcuadradomagico(mat):
    print("Es un cuadrado mágico")
else:
    print("No es un cuadrado mágico")