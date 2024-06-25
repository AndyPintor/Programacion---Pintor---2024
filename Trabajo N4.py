#Generar un número secreto al azar del 1 al 100
#Informar al usuario que tiene que adivinar, y tiene 6 oporunidades
#Si el núm ingresado por el usuario es menos a 1 o mayor a 100, se le informara que el num elegido no esta permitido.
#Si el num ingresado por el usuario, es menor se le informa que es incorrecto y debe intentar con un numero mayor
#Si el numero ingresado es mayor debe informar que intente con un numero menor
#Si el usuario acierta con el num, se le informa que gana y se le indicara cuadno intentos le tomo.

import random

nom = input("Bienvenido, porfavor ingrese su nombre: ")
num1 = int(random.uniform(1, 100))
print("Debe adivinar un número del 1 al 100, y tiene 6 oportunidades...")
num = float(input(f"Porfavor {nom} ingrese un número: "))
#print(num1)

x=1
while x<6:
    if num < 1:
        print("Porfavor ingrese un número mayor a 1")
        num = float(input("Porfavor ingrese otro número: "))
    elif num > 100:
        print("Porfavor ingrese un número menor a 100")
        num = float(input("Porfavor ingrese otro número: "))
    elif num != num1:
        print("Número erroneo! Vuelva a intentarlo...")
        if num < num1:
            print("Intenta con un número mas \"ALTO\" ")
            num = float(input("Porfavor ingrese otro número: "))
        else:
            print("Intente con un número mas \"BAJO\" ")
            num = float(input("Porfavor ingrese otro número: "))
    else:
        print(f"Felicidades {nom} has ganado el juego!!!")
        print(f"Tus cantidades de intentos fueron: {x}")
        break
    x += 1
else:
    print(f"Has usado todos tus intentos {nom}, has perdido!")
    print(f"El numero era {num1}")