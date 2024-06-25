num=(list(range(1, 16)))
#print(num)
suma_cuadrados = [num**2 for num in range(16) if 0 < num < 16]
print(suma_cuadrados)