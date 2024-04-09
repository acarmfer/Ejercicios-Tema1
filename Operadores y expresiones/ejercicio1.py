numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

son_iguales = numero1 == numero2
son_diferentes = numero1 != numero2
primero_es_mayor = numero1 > numero2
segundo_es_mayor_o_igual = numero2 >= numero1

print("Los dos números son iguales:", son_iguales)
print("Los dos números son diferentes:", son_diferentes)
print("El primero es mayor que el segundo:", primero_es_mayor)
print("El segundo es mayor o igual que el primero:", segundo_es_mayor_o_igual)