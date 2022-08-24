billetes = ['$500', '$100', '$50', '$20', '$10', '$5', '$1']

precio = int(input('Ingrese el monto a cobrar: '))
dinero = int(input('Ingrese el monto con el que paga el cliente: '))
vuelto = []

while dinero > precio:
    if (dinero - 500) >= precio:
        dinero -= 500
        vuelto.append(billetes[0]) 
    elif dinero - 100 >= precio:
        dinero -= 100
        vuelto.append(billetes[1]) 
    elif dinero - 50 >= precio:
        dinero -= 50
        vuelto.append(billetes[2])
    elif dinero - 20 >= precio:
        dinero -= 20
        vuelto.append(billetes[3])
    elif dinero - 10 >= precio:
        dinero -= 10
        vuelto.append(billetes[4])
    elif dinero - 5 >= precio:
        dinero -= 5
        vuelto.append(billetes[5])
    else:
        dinero -= 1
        vuelto.append(billetes[6]) 

print(vuelto)
     
     
    