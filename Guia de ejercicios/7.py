import random

num1 = random.randint(1,100)
cont = 0

while cont == 0:
    num2 = int(input("Ingrese un número: "))
    if num1 > num2:
        print("Es un número mayor")
    elif num1 < num2:
        print("Es un número menor")
    else:
        print("NUMERO CORRECTO!")
        cont = 1
