numero_magico = 12345679
numero_usuario = int(input("Introduce un número entre 1 y 9: "))

numero_usuario *= 9
numero_magico *= numero_usuario

print("El valor final del número mágico es:", numero_magico)