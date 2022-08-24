def mayor_estricto(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            return n1
    elif n2 > n1:
        if n2 > n3:
            return n2
    elif n3 > n1:
        if n3 > n2:
            return n3
    return -1

print(mayor_estricto(1,2,1))