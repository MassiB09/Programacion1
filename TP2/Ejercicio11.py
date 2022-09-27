def numero_valido(numero_afiliado):
    while numero_afiliado > 9999 or numero_afiliado < 1000:
        print('El numero es invalido, recuerde que su numero tiene 4 digitos')
        numero_afiliado = int(input('Ingrese su numero de afiliado: '))
    return numero_afiliado

def enlistar(numero_afiliado, urgencia):
    if urgencia == 0:
        lista_urgencias.append(numero_afiliado)
    else:
        lista_turnos.append(numero_afiliado)

def buscar_afiliado(numero_afiliado):
    print(f'Se atendio al afiliado {numero_afiliado} de urgencias {lista_urgencias.count(numero_afiliado)} veces')
    print(f'Se atendio al afiliado {numero_afiliado} por turno {lista_turnos.count(numero_afiliado)} veces')

lista_urgencias = []
lista_turnos = []
while True:
    numero_afiliado = int(input('Ingrese su numero de afiliado: '))
    if numero_afiliado == -1:
        break 
    numero_afiliado = numero_valido(numero_afiliado)
    urgencia = int(input('Ingrese 0 si es una urgencia o 1 si viene con turno: '))
    while urgencia != 0 and urgencia != 1:
        print('El vanlor ingresado es invlaido!')
        urgencia = int(input('Ingrese 0 si es una urgencia o 1 si viene con turno: '))
    enlistar(numero_afiliado, urgencia)
print(lista_urgencias)
print(lista_turnos)

while True:
    numero_afiliado = int(input('Ingrese el numero de afiliado que desea buscar: '))
    if numero_afiliado == -1:
        break 
    numero_afiliado = numero_valido(numero_afiliado)
    while numero_afiliado not in lista_urgencias and numero_afiliado not in lista_turnos:
        print('El numero de afiliado no fue atendido')
        numero_afiliado = int(input('Ingrese el numero de afiliado que desea buscar: '))
    buscar_afiliado(numero_afiliado)
print('\nPrograma finalizado')