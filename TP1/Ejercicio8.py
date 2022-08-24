def es_bisiesto(anio):
    '''Esta funcion recibe un año y nos devuelve si es bisiesto o no (True or False)'''
    if (anio % 4 == 0 and not(anio % 100 == 0)) or (anio % 100 ==0 and anio % 400 == 0): #Compruebo si el año es bisiesto
        return True
    else:
        return False

def es_valido(dia, mes, anio):
    '''Esta funcion recibe una fecha en forma de 3 parametros y nos devuelve un valor booleano que confirma si la fecha es valida o no'''
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12: #Compruebo si el mes tiene 31 dias
        if 0 < dia <= 31:
            return True
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11: #Compruebo si el mes tiene 30 dias
        if 0 < dia <= 30:
            return True
    elif mes == 2 and es_bisiesto(anio): #Compruebo si el mes tiene 29 dias
        if 0 < dia <= 29:
            return True
    elif mes == 2 and not(es_bisiesto(anio)): #Compruebo si el mes tiene 28 dias
        if 0 < dia <= 28:
            return True
    return False

def dia_de_la_semana(dia, mes, anio):
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo)) % 7
    if diasem < 0:
        diasem = diasem + 7
    return diasem 

mes = int(input('Ingrese el mes: '))
anio = int(input('Ingrese el año: '))

while not(es_valido(1, mes, anio)):
    print('\nEl mes o el año ingresado es incorrecto \n')
    mes = int(input('Ingrese el mes: '))
    anio = int(input('Ingrese el año: '))


if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    iteraciones = 30
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    iteraciones = 31
elif es_bisiesto(anio):
    iteraciones = 29
else:
    iteraciones = 28

aux = dia_de_la_semana(1, mes, anio)
espacio = '   ' * aux #Cantidad de espacios que va tener al principio el calendario

print('\nDo Lu Ma Mi Ju Vi Sa:')
print(espacio, end = '') #Imprimo el espacio 
for i in range(1, iteraciones + 1):
    print('%2d' %i, end=' ') #Imprimo cada fecha del calendario y luego un espacio
    if i == 7 - aux or i == 14 - aux or i == 21 - aux or i == 28 - aux or i == 35 - aux:
        print('') #Imprimo un salto de linea para que mantenga el formato