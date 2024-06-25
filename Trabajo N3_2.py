#Comparar las variables num1 y num2, obtenidas por el usuario;
#imprimir los msj num1 es mayor que num2 si es el caso
#debe imprimir en esos msj el calor de las variables ingresadas

num1= round(float(input("Ingrese el primer número: ")))
num2= round(float(input("Ingrese el segundo número: ")))

if num1>num2:
    print(f"{num1} es mayor a {num2}")
elif num1==num2:
    print(f"{num1} es igual a {num2}")
elif num1<num2:
    print(f"{num1} es menor a {num2}")
else:
    print("Porfavor ingrese números")