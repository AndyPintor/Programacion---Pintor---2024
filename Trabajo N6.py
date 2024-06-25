
tex=("Escribir mal código es fácil. Escribir buen código es dificil. Escribir buen código y entenderlo seis meses después es un milagro")
print(f"Analicemos el siguiente texto:  \n \'{tex}\'")
print("")
pal = input("Ingrese una palabra: ")
pos1 = tex.find(pal)
pos_f=(tex.find(pal, pos1+1))
print(f"La posición en la que aparece \'{pal}\' por primera vez es \'{pos1}\'")
print(f"La posición en la que aparece \'{pal}\' por segunda vez es \'{pos_f}\'")
