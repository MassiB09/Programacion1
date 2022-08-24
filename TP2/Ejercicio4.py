def sin_repetidos(lista):
    resultado = []
    for i in lista:
        if i not in resultado:
            resultado.append(i)
    return resultado

palabras = ['hola','chau','luna','sol','chau']
repetidas = ['chau','luna','tonto','luna','chau']
resultado = []

for i in palabras:
    for j in repetidas:
        if i == j:
            resultado.append(i)
            break
print(palabras)
print(repetidas)
print(sin_repetidos(resultado))