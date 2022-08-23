#Dia = 0, 1, 2, 3, 4, 5, 6
#Mes = 0/6, 3/2, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5
#anio = ultimos dos digitos
#siglo: 
# I = 6
# II = 4
# III = 2
# IV = 0


meses_31 = [1, 3, 5, 7, 8, 10, 12]
meses_30 = [4, 6, 9, 11]
def es_bisiesto(anio):
    if (anio % 4 == 0 and not(anio % 100 == 0)) or (anio % 100 ==0 and anio % 400 == 0):
        return True
    else: 
        return False

'''def formula_dia(dia, mes, anio, siglo):
    resultado = (dia + mes + anio + anio // 4 + siglo) 
    print(dia, mes, anio, anio // 4, siglo)
    while resultado - 7 > 0:
        resultado -= 7
    return resultado'''

'''def numero_mes(mes):
    if (es_bisiesto(anio) and mes == 1) or mes == 10:
        resultado = 0
    elif (es_bisiesto(anio) and mes == 2) or mes == 8:
        resultado = 2
    elif (not(es_bisiesto(anio)) and mes == 2) or mes == 3 or mes == 11:
        resultado = 3
    elif mes == 6:
        resultado = 4
    elif mes == 9 or mes == 12:
        resultado = 5
    elif mes == 4 or mes == 7:
        resultado = 6
    else:
        resultado = 1
    return resultado'''

'''def numero_siglo(siglo):
    while siglo > 4:
        siglo -= 4
    if siglo == 1:
        resultado = 6
    elif siglo == 2:
        resultado = 4
    elif siglo == 3:
        resultado = 2
    elif siglo == 4:
        resultado = 0
    return resultado'''

def es_valido(dia=1, mes=1, anio=1):
    if mes in meses_31:
        if dia <= 31:
            return True
    elif mes in meses_30:
        if dia <= 30:
            return True
    elif mes == 2 and es_bisiesto(anio):
        if dia <= 29:
            return True
    elif mes == 2 and not(es_bisiesto(anio)):
        if dia <= 28:
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

#dia = int(input('Ingrese el dia: '))
mes = int(input('Ingrese el mes: '))
anio = int(input('Ingrese el año: '))

if es_valido(1, mes, anio):
    if mes in meses_30:
        iteraciones = 30
    elif mes in meses_31:
        iteraciones = 31
    elif es_bisiesto(anio):
        iteraciones = 29
    else:
        iteraciones = 28

'''siglo = numero_siglo((anio // 100) + 1)
nro_mes = numero_mes(mes)
anio = anio % 100
resultado = formula_dia(dia, mes, anio, siglo)'''
#print(resultado)
if mes in meses_31:
    dias = 31
else:
    dias = 30

for i in range(1, dias + 1):
    print(dia_de_la_semana(i, mes, anio))