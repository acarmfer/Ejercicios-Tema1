lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

# Convertir las listas en conjuntos
set_1 = set(lista_1)
set_2 = set(lista_2)

# Obtener la intersección de los conjuntos
interseccion = set_1.intersection(set_2)

# Convertir la intersección en una lista
lista_3 = list(interseccion)

print(lista_3)