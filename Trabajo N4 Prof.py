from random import (randint)

intento = 0
respuesta = 0
num_s= randint(1, 100)
nom= input("Hola, como se llama? ")


print(f"Bienvenido {nom}, he elegido un numero entre 1 y 100. \n Tenes 6 intenos para adivinarlo.")


while intento<6:
    respuesta = int(input("Cual es el número? "))
    intento += 1
    if respuesta < 1 or respuesta > 100:
        print("El numero debe estar entre comprendido entre 1 y 100")
    elif respuesta < num_s:
        print("Mi numero es mas alto, intentalo de nuevo.")
    elif respuesta > num_s:
        print("Mi numero es mas bajo, intentalo de nuevo.")
    else:
        print(f"¡Felicidades {nom}! \n Mi numero secreto era {num_s} y lo adivinaste en {intento}")
        break


if respuesta != num_s:
    print(f"Se te termino los intentos. El nuúmero secreto era {num_s}")