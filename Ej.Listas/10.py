import random
def Crear():
    lista1 = []
    cont = 0
    while cont < 10:
        num = random.randint(1,10)
        lista1.append(num)
        cont+= 1
    return lista1

def indice(lista, nro):
    for i in range(len(lista)):
        if nro == lista[i]:
            return i
        
    return -1


lista1 = Crear()
print(lista1)
nro = random.randint(1,10)
print("El numero es:", nro)
resultado = indice(lista1, nro)
print(resultado)