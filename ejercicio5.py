matriz = [ 
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

# Recorrer cada fila de la matriz
for fila in matriz:
    # Calcular la suma de los tres primeros elementos de la fila
    suma = sum(fila[:3])
    # Actualizar el cuarto elemento de la fila con la suma calculada
    fila[3] = suma

print(matriz)
