numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    numero = int(input("Ingrese un número entero del 0 al 9: "))
    if numero in numeros:
        print("El número se encuentra en la lista.")
        break
    else:
        print("El número no es válido. Inténtelo nuevamente.")