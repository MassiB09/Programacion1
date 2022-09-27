def es_capicua(cadena):
    resultado = True
    for i in range(len(cadena)):
        if cadena[i] != cadena[-i-1]:
            resultado = False
    return resultado

print(es_capicua('jijij'))