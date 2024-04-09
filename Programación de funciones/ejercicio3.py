def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

# Ejemplos de uso
print(relacion(5, 10))  # Devuelve 1
print(relacion(10, 5))  # Devuelve -1
print(relacion(5, 5))   # Devuelve 0