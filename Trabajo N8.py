datos_personales={"nombre":"Flores", "apellido":"Gomez", "DNI":35632135, "domicilio":"Panama 850", "ciudad":"Bahía Blanca"}

print(datos_personales["nombre"], datos_personales["apellido"], datos_personales["DNI"], datos_personales["domicilio"], datos_personales["ciudad"])
print("Su nombre: ", datos_personales["nombre"])
print("Su apellido: ", datos_personales["apellido"])
print("Su documento: ", datos_personales["DNI"])
print("Su documento: ", datos_personales["domicilio"])
print("Su ciudad: ", datos_personales["ciudad"])

print("Los datos actualizados son:")
datos_personales["domicilio"]="Via Apia 2432"
datos_personales["ciudad"]="Napoles"
datos_personales["pais"]="Italia"
print(datos_personales["nombre"],",",datos_personales["apellido"],",",datos_personales["DNI"],",",datos_personales["domicilio"],",",datos_personales["ciudad"],"y",datos_personales["pais"])
print("Su nombre: ", datos_personales["nombre"],"\nSu apellido: ", datos_personales["apellido"],"\nSu documento: ",datos_personales["DNI"])
print("Su documento: ", datos_personales["domicilio"])
print("La ciudad: ", datos_personales["ciudad"])
print("El pais: ", datos_personales["pais"])

