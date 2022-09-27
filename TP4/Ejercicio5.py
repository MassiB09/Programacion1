def filtrar_palabras_v1(cadena, n):
    lista = cadena.split()
    resultado = ''
    for i, palabra in enumerate(lista):
        if len(palabra) > n:
            resultado += lista[i]
    return resultado

def filtrar_palabras_v2(cadena, n):
    lista = [ elemento for elemento in cadena.split() if len(elemento) > n]
    return ' '.join(lista)

def filtrar_palabras_v3(cadena, n):
    lista = list(filter(lambda x: len(x) > n, cadena.split()))
    return ' '.join(lista)

cadena = input('Ingrese la cadena: ')
n = int(input('Ingrese n: '))
print(filtrar_palabras_v1(cadena, n))
print(filtrar_palabras_v2(cadena, n))
print(filtrar_palabras_v3(cadena, n))