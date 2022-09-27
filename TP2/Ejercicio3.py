N = int(input('Ingrese N: '))
lista = []

for i in range(1,N+1):
    lista.append(i**2)

print(lista[-10:])