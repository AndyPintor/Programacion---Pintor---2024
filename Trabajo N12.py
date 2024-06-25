pais=["Argentina", "BRasil", "Francia", "Alemania", "Italia", "España", "Inglaterra", "Uruguay"]
jugadores = ["Lionel Messi", "Neymar Jr.", "Kylian Mbappe", "Thomas Muller", "Mateo Retegui", "Alvaro Morata", "Harry Kane", "Luis Suarez"]
capitales=["Buenos Aires", "Brasilia", "Paris", "Berlin", "Roma", "Madrid", "Londres", "Montevideo"]

for pais, jugadores, capitales in zip(pais, jugadores, capitales):
    print(f"El capitan de {pais} es {jugadores} y el equipo ejerce la localia en {capitales}")