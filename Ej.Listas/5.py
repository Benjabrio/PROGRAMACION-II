import random
def borrarDup(lista):
    lista2 = []
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    return lista2
    
lista1 = []
cont = 0
while cont < 15:
    num = random.randint(1,10)
    lista1.append(num)
    cont+= 1


print("La lista es:", lista1)
resultado = borrarDup(lista1)
print("La lista nueva sin duplicados es:", resultado)
