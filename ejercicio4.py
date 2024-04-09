cantidad_numeros = int(input("Ingrese cuántos números desea introducir: "))
suma = 0

for i in range(cantidad_numeros):
    numero = float(input("Ingrese un número: "))
    suma += numero

media = suma / cantidad_numeros
print("La media aritmética de los números ingresados es:", media)
