import random
def Crear():
    lista1 = []
    cont = 0
    while cont < 15:
        num = random.randint(1,10)
        lista1.append(num)
        cont+= 1
    return lista1

def concatenar(lista1, lista2):
    lista3 = lista1 + lista2
    return lista3


lista1 = Crear()
lista1.sort()
lista2 = Crear()
lista2.sort()
print(lista1)
print(lista2)
resultado = concatenar(lista1, lista2)
resultado.sort()
print("La concatenación de estas listas es:", resultado)
