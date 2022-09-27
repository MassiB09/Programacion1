matriz = [[4,3,8],
          [9,5,1],
          [2,7,6]]

n = len(matriz)
valor_magico = sum(matriz[0])
resultado = True

for i in range(n):
    suma = 0
    for j in range(n):
        if valor_magico != sum(matriz[i]):
            resultado = False
    for r in range(n):
        suma += matriz[r][i]
    if valor_magico != suma: 
        resultado = False
        

principal = 0
secundaria = 0
for j in range(n):
    principal += matriz[j][j]
    secundaria += matriz[j][n-j-1]
if valor_magico != principal or valor_magico != secundaria:
    resultado = False

print(resultado)
print(matriz)
'''
def sumar_digitos(elemento):
    resultado = 0
    while elemento > 0:
        resultado += elemento % 10
        elemento = elemento // 10
    return resultado

n = int(input('Ingrese n: '))
lista = [elemento for elemento in range(1, n+1) if elemento % 7 == 0 or elemento % 10 == 7]
print(lista)
lista.sort(key=sumar_digitos)
print(lista)'''