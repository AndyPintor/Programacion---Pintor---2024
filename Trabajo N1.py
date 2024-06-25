nombre = input("Nombre: ")
apellido = input("Apellido: ")
can_venta = int(input("Cantidad de venta: "))
comision = round(can_venta*13 /100,2)

print(f"La comusion este mes es ${comision} para el trabajador: {nombre} {apellido}")
print("La comusion este mes es ${} para el trabajador: {} {}" . format(comision, nombre, apellido))
