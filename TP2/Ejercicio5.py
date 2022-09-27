def orden_lista (lista):
    aux = sorted(lista)
    if aux == lista:
        return True
    return False

print(orden_lista(['A','A','B']))