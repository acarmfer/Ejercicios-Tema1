cadena = "zeréP nauJ,01"

# Voltear la cadena
cadena_invertida = cadena[::-1]

# Dividir la cadena invertida en nombre y nota
nombre_invertido, nota = cadena_invertida.split(',')

# Voltear el nombre
nombre = nombre_invertido[::-1]

# Formatear la cadena
cadena_formateada = f"{nombre.capitalize()} ha sacado un Nota de {nota.strip()}."

print(cadena_formateada)
