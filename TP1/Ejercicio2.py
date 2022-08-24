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

dia = int(input('Ingrese el dia: '))
mes = int(input('Ingrese el mes: '))
anio = int(input('Ingrese el año: '))

print(es_valido(dia, mes, anio))