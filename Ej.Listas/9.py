import random
def Crear():
    lista1 = []
    cont = 0
    while cont < 5:
        num = random.randint(1,10)
        lista1.append(num)
        cont+= 1
    return lista1

def producto(lista):
    multi = 1
    for i in lista:
        multi = i * multi
    return multi
        

lista1 = Crear()
print(lista1)
resultado = producto(lista1)
print("El producto de esa lista es:", resultado)