import random

def encajonar(cajones, naranjas):
    cajones.append(sum(naranjas)/1000)
    naranjas.clear()

def encamionar(cajones):
    camiones = 0
    kilos = 0
    aux = []
    for cajon in cajones:
        if kilos + cajon < 500:
            kilos += cajon
        else:
            camiones += 1
            aux.append(kilos)
            kilos = cajon
    if kilos > 500 * 0.8:
        camiones += 1
        aux.append(kilos)
        kilos = 0
    return (kilos, camiones, aux)

cantidad = int(input('Ingrese la cantidad de naranjas: '))
naranjas = []
naranjas_jugo = 0
cajones = []

for i in range(cantidad):
    aux = random.randint(150, 350)
    if  200 <= aux <= 300 and len(naranjas) < 100:
        naranjas.append(aux)
    elif len(naranjas) == 100:
        encajonar(cajones, naranjas)
        naranjas.append(aux)
    else:
        naranjas_jugo += 1
encajonar(cajones, naranjas)
cantidad_cajones = len(cajones)
sobrante = encamionar(cajones)[0]
camiones = encamionar(cajones)[1]
aux = encamionar(cajones)[2]
print(cantidad_cajones)
print(naranjas_jugo)
print(cajones)
print(sum(cajones))
print(camiones,aux)
print(sobrante)