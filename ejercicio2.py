numero = 0

while True:
    try:
        numero = int(input("Introduce un número impar: "))
        if numero % 2 != 0:
            break
        else:
            print("El número introducido no es impar. Inténtalo de nuevo.")
    except ValueError:
        print("Error: Debes introducir un número entero.")

print("¡Has introducido un número impar correctamente!")
