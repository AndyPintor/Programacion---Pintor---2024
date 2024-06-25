lista_socios = ["Julio", "Renata", "Julieta", "Sebastián", "Bruno", "Jésica", "Dario", "Emiliano", "Julián"]
print(lista_socios)

for i, nom in enumerate(lista_socios):
    if nom[0] == "J":
        print(nom) #Indica solo los nombres que empiezan con J


for i, nom in enumerate(lista_socios):
    if nom[0] == "J":
        print(nom[0]) #Solo indica la inicial de los nombres con J

for i, nom in enumerate(lista_socios):
    if nom[0] != "J":
        print(nom) #Indica solo los nombres que no empiezan con J

for i, nom in enumerate(lista_socios, 3):
    if nom[0] == "J":
        print(nom) #Indica solo los nombres que empiezan con la letra J, de la posicion 3

