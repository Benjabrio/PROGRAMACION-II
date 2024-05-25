import random
def invertir(lista):
    lista2 = list(reversed(lista))
    return lista2

lista1 = []
cont = 0
while cont < 15:
    num = random.randint(1,10)
    lista1.append(num)
    cont+= 1

print("La lista es:",lista1)
resultado = invertir(lista1)
print("La lista invertida es:", resultado)
