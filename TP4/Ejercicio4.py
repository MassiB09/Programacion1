'''numero = int(input('Ingrese el numero: '))
cadena = ''

while numero > 0:
    if numero - 1000 >= 0:
        cadena += 'M'
        numero -= 1000
    elif numero - 500 >= 0:
        cadena += 'D'
        numero -= 500
    elif numero - 100 >= 0:
        cadena += 'C'
        numero -= 100
    elif numero - 50 >= 0:
        cadena += 'L'
        numero -= 50
    elif numero - 10 >= 0:
        cadena += 'X'
        numero -= 10
    elif numero - 5 >= 0:
        cadena += 'V'
        numero -= 5
    else:
        cadena += 'I'
        numero -= 1

print(cadena)'''