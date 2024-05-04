cont = 0
while cont == 0: 
    nro = int(input("Ingrese 1 si desea pasar de Celsius a Fahrenheit, Ingrese 2 si es al revés."))
    if nro == 1:
        TempCel = float(input("Ingrese la temperatura actualmente en Celsius: "))
        TempFahr = (TempCel * (9/5) + 32)
        print("Si la temperatura actual en celsius es:", TempCel, "entonces la temperatura en grados Fahrenheit es:", TempFahr)
        cont = 1
    elif nro == 2:
        TempFahr = float(input("Ingrese la temperatura actualmente en Fahrenheit:"))
        TempCel =  (TempFahr - 32) * (5/9)
        print("Si la temperatura actual en grados Fahrenheit es:", TempFahr, "entonces la temperatura en celsius es:", TempCel)
        cont = 1
    else: 
        print("Numero desconocido, por favor, ingrese 1 o 2")
        cont = 0