clave_maestra = input('Ingrese la clave maestra: ')
clave1 = ''
clave2 = ''

for i in range(len(clave_maestra)):
    if int(i) % 2 == 0:
        clave1 += clave_maestra[i]
    else:
        clave2 += clave_maestra[i]

print(clave_maestra)
print(clave1)
print(clave2)