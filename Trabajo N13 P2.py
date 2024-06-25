import random
colores=["Rojo", "Verde", "Azul", "Amarillo", "Naranja", "Violeta", "Rosa", "Marron", "Negro", "Blanco", "Gris","Violeta", "Celeste"]

while True:
    num1 = (random.choice(colores))
    num2 = (random.choice(colores))
    num3 = (random.choice(colores))
    if num1 != num2 != num3:
        print(num1, num2, num3)
    break