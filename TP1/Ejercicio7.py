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

def dia_siguiente(dia, mes, anio):
    '''Esta funcion suma un dia a la fecha ingresada (en 3 parametros)'''
    dia += 1
    return arreglar_fecha(dia, mes, anio)

def sumar_n_dias(n, dia, mes, anio):
    '''Esta funcion suma n dias a la fecha ingresada (en 4 parametros)'''
    for i in range(n):
        dia, mes, anio = dia_siguiente(dia, mes, anio)
    return dia, mes, anio


def arreglar_fecha(dia, mes, anio):
    '''Esta funcion se encarga de pasar de mes o año si es necesario'''
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia > 31:
            dia -= 31
            mes +=1
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30:
            dia -= 30
            mes +=1
    else:
        if not(es_bisiesto(anio)):
            if dia > 28:
                dia -= 28
                mes +=1
        else:
            if dia > 29:
                dia -= 29
                mes +=1
    if mes > 12:
        mes -= 12
        anio += 1
    return dia, mes, anio

def pasar_a_dias(mes, anio):
    '''Esta funcion recibe un mes y un año y los pasa a dias'''
    dias = 0
    flag = False #Defino un indicador para saber si estoy sumando 1 dia de mas por los anios bisiestos
    while mes != 0:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            dias += 31
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            dias += 30
        else:
            if es_bisiesto(anio): 
                dias += 29
                flag = True #Si se ejecuta esta parte de codigo el indicador pasa a ser True
            else:
                dias += 28
        mes -= 1
    while anio != 0:
        if es_bisiesto(anio):
            dias += 366
        else:
            dias += 365
        if anio > 0:
            anio -= 1
        else:
            anio +=1
    if flag: #Si el indicador es True entonces tengo que restar al total el dia que se sumo 2 veces anteriormente en el codigo
        dias -= 1
    return dias

def dias(dia1, mes1, anio1, dia2, mes2, anio2):
    '''Esta funcion recibe dos fechas y devuelve la cantidad de dias que hay entre cada una'''
    dias = dia1 + pasar_a_dias(mes1, anio1) 
    dias -= dia2 + pasar_a_dias(mes2, anio2)
    abs(dias) #Convierto la cantidad de dias en un numero positivo
    return dias

opcion = 0

while opcion != 1 and opcion != 2 and opcion != 3: #Hicimos un menu sencillo para decidir que parte del codigo se desea ejecutar
    print('1.Para sumar n dias a una fecha ingrese "1"\n2.Para calcular los dias que hay entre dos fechas ingrese "2"\n3.Para finalizar el programa ingrese "3"')
    opcion = int(input())
    if opcion == 1:
        dia = int(input('Ingrese el dia: '))
        mes = int(input('Ingrese el mes: '))
        anio = int(input('Ingrese el año: '))

        while not(es_valido(dia, mes, anio)):
            print('\nLa fecha ingresada no es valida, ingrese otra!\n')
            dia = int(input('Ingrese el dia: '))
            mes = int(input('Ingrese el mes: '))
            anio = int(input('Ingrese el año: '))

        iteraciones = int(input('Ingrese la cantidad de dias que le sumara a la fecha: '))
        while iteraciones < 0:
            print('\nEl numero de dias debe ser positivo: \n')
            iteraciones = int(input('Ingrese la cantidad de dias que le sumara a la fecha: '))

        dia, mes, anio = sumar_n_dias(iteraciones, dia, mes, anio)

        print('%02d'%dia, '/%02d'%mes, '/%04d'%anio,'\n', sep='')
        opcion = 0

    elif opcion == 2:
        print('Ingrese los datos de la primera fecha')
        dia1 = int(input('Ingrese el dia: '))
        mes1 = int(input('Ingrese el mes: '))
        anio1 = int(input('Ingrese el año: '))
        
        print('Ingrese los datos de la segunda fecha')
        dia2 = int(input('Ingrese el dia: '))
        mes2 = int(input('Ingrese el mes: '))
        anio2 = int(input('Ingrese el año: '))

        print(dias(dia1, mes1, anio1, dia2, mes2, anio2),'dias\n')
        opcion = 0
    elif opcion == 3:
        print('Programa finalizado!')
    else:
        print('\nLa opcion es invalida!!\n')