import random

def mostrar_butacas():
    butaca = 0
    for f in range(len(matriz)):
        for b in range(len(matriz[f])):
            print('%3d' %butaca,': ','%2d'%matriz[f][b], end='', sep='')
            butaca +=1
            if (butaca % len(matriz[f])) == 0:
                print()

def reservar(matriz, butaca):
    resultado = False
    fila = 0
    while butaca > m:
        fila +=1
        butaca -=m
    if matriz[fila][butaca] == False:
        resultado = True
        matriz[fila][butaca] = True
    return resultado

def cargar_sala(matriz):
    for f in range(len(matriz)):
        for b in range(len(matriz[f])):
            matriz[f][b] = random.choice([True, False]) 
    return matriz

def butacas_libres(matriz):
    resultado = 0
    for f in range(len(matriz)):
        for b in range(len(matriz[f])):
            if matriz[f][b] == False:
                resultado +=1
    return resultado

def butacas_contiguas():
    maximo = 0
    for f in range(len(matriz)):
        contador = 0 
        for i, b in enumerate(matriz[f]):
            if matriz[f][i] == False:
                contador +=1
            else:
                if maximo < contador:
                    maximo = contador
                    posicion_maxima = f,i-contador
                contador = 0
    return posicion_maxima

n = int(input('Ingrese la cantidad de filas: '))
m = int(input('Ingrese la cantidad de butacas(por fila): '))
matriz = [ [False] * m for i in range(n)]

matriz = cargar_sala(matriz)
mostrar_butacas()
print('Hay',butacas_libres(matriz),'butacas libres')
print(f'La fila de butacas mas larga es: {butacas_contiguas()[0]} y empieza en la butaca numero: {butacas_contiguas()[1]}')
butaca = int(input('Ingrese la butaca que desea reservar: '))

if reservar(matriz, butaca):
    print(f'La butaca "{butaca}" fue reservada con exito!')
else:
    print(f'La butaca "{butaca}" ya estaba ocupada!')