def sumatoria(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma
    

lista2 = []
cont = 0
while cont < 5:
    num = int(input("Ingrese 5 numeros para la lista:"))
    lista2.append(num)
    cont+= 1

print(lista2)
resultado = sumatoria(lista2)
print(resultado)


    