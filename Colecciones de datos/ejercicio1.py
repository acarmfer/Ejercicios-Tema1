# Crea el conjunto de usuarios
usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}

# Crea el conjunto de administradores
administradores = {"Juan", "Marta"}

# Borra al administrador Juan del conjunto de administradores
administradores.discard("Juan")

# Añade a Marcos como un nuevo administrador
administradores.add("Marcos")

# Muestra todos los usuarios por pantalla
for usuario in usuarios:
    if usuario in administradores:
        print(usuario, "es administrador")
    else:
        print(usuario, "no es administrador")