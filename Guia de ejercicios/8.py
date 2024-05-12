import random

contra = []
mayus = "ABCDEFGHIJKLMNÑOPQRSTYUVWXYZ"
minus = "abcdefghijklmnñopqrstuvwxyz"
num = "0123456789"
carEsp = "!#$%&/()=?¡¿'@"
cont = 0
contra.append(random.choice(mayus))
contra.append(random.choice(minus))
contra.append(random.choice(num))
contra.append(random.choice(carEsp))


while cont == 0:
    if len(contra) < 12:
        contra.append(random.choice(mayus+minus+num+carEsp))
    if len(contra) >= 12:
        cont = 1

random.shuffle(contra)
contra = "".join(contra)
print (contra)
    
    

