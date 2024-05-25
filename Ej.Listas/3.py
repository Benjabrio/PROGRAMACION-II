def promedio(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    prom = float(suma / len(lista))
    return prom
    

lista2 = []
cont = 0
while cont < 5:
    num = int(input("Ingrese 5 numeros para la lista:"))
    lista2.append(num)
    cont+= 1

print(lista2)
resultado = promedio(lista2)
print("El promedio es: ",resultado)


    