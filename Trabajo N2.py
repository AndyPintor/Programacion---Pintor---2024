tex = (input("Ingrese un texto: "))
l1= (input("Ingrese una primera letra a su preferencia: "))
l2= (input("Ingrese una segunda letra a su preferencia: "))
l3= (input("Ingrese una tercera letra a su preferencia: "))

#Tranforma todo en minuscula
tex1=(tex.lower())
l1_1=(l1.lower())
l2_1=(l2.lower())
l3_1=(l3.lower())

#Cuenta la cantidad de veces que se repite cada letra

uno=(tex1.count(l1_1))
print(f"La primera letra \"{l1_1}\" se repite {uno}")
t1=(f"la primera letra \"{l1_1}\" se repite {uno}")

dos=(tex1.count(l2_1))
print(f"La segunda letra \"{l2_1}\" se repite {dos}")
t2=(f"la segunda letra \"{l2_1}\" se repite {dos}")

tres=(tex1.count(l3_1))
print(f"La tercera letra \"{l3_1}\" se repite {tres}")
t3=(f"la tercera letra \"{l3_1}\" se repite {tres}")

print(f"Podriamos decir que: {t1}, {t2}, {t3}" )

#Cantinda de palabras de tex

lis=(tex1.split())
cantidad=(len(lis))
print(f"La cantidad de palabras del texto es {cantidad}")

#cual es la primera y ultima letra del texto

pri=(tex1[0])
tex2=(tex1[::-1])
seg=(tex2[0])

print(f"La primera letra es \"{pri}\" y la ultima \"{seg}\"")

#otra manera de resolver

print("\n")
print("Letras de inicio y de fin")
letra_inicio = tex1[0]
letra_final = tex1[-1]
print(f"La primera letra es '{letra_inicio}' y la letra final '{letra_final}'")


