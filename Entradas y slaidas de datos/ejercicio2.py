import sys

# Verificar si se proporcionaron los argumentos correctos
if len(sys.argv) != 3:
    print("Uso: python tabla.py <filas> <columnas>")
    sys.exit(1)

# Obtener los argumentos
filas = int(sys.argv[1])
columnas = int(sys.argv[2])

# Verificar si los argumentos están dentro del rango válido
if not (1 <= filas <= 9) or not (1 <= columnas <= 9):
    print("Error: Los argumentos deben ser números enteros positivos del 1 al 9.")
    sys.exit(1)

# Imprimir la tabla
for i in range(filas):
    for j in range(columnas):
        print(" * ", end='')
    print()
