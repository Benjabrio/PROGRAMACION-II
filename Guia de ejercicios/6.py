mayus = False
minus = False
num = False
carEsp = False
long = False
cont = 0

while cont == 0:
    contra = input("Ingrese contraseña: ")
    if len(contra) >= 8:
        long = True
    for i in contra:
        if i in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
            mayus = True
        if i in "abcdefghijklmnñopqrstuvwxyz":
            minus = True
        if i in "0123456789":
            num = True
        if i in "!#$%&/()=?¿¡'":
            carEsp = True
    if long and mayus and minus and num and carEsp:
        print("La contraseña es válida")
        cont = 1
    else:
        print("La contraseña no es valida. Ingresar nuevamente.")