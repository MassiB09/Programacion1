'''Desarrollar una funcion que reciba como parametros dos numeros enteror positivos y devuelva el numero que resulte de concatenar ambos valores. 
Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. 
No se permite utilizar facilidades de pyth no vistas en clase'''

def enlistar(numero):
    lista = []
    while numero >= 1:
        aux = numero % 10
        numero //= 10
        lista.append(aux)
    lista = lista[::-1]
    return lista

def concatenar(n1,n2):
    resultado = 0
    lista = enlistar(n1) + enlistar(n2)
    for potencia, elemento in enumerate(reversed(lista)):
        resultado += elemento * (10 ** potencia)
    return resultado

print(concatenar(123,456))