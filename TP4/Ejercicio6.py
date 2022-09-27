def sub_cadena_v1(cadena, posicion, cantidad):
    resultado = cadena[posicion:cantidad + posicion]
    return resultado

def sub_cadena_v2(cadena, posicion, cantidad):
    resultado = ''
    for i in range(posicion, cantidad + posicion):
        resultado += cadena[i]
    return resultado

print(sub_cadena_v2('El numero de telefono es 4356-7890', 25, 9))