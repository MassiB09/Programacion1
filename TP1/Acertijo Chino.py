cabezas = 35
conejo = 4
gallina = 2
patas = gallina * cabezas

while patas < 94:
    cabezas -= 1
    patas += 2

print(f'Hay {cabezas} gallinas y {35 - cabezas} conejos')