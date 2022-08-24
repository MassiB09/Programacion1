def pared_asteriscos(num):
    for i in range(num):
        print('**********')

def escalera_asteriscos(num):
    asterisco = ''
    for i in range(num):
        asterisco += '**'
        print(asterisco)

pared_asteriscos(5)
escalera_asteriscos(12)