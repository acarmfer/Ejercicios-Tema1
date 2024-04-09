# Lista de tareas con sus prioridades
tareas = [
    (3, "Tarea C"),
    (1, "Tarea A"),
    (2, "Tarea B")
]

# Ordenar la lista de tareas por prioridad
tareas.sort()

# Crear una nueva lista solo con los nombres de las tareas
cola_tareas = [tarea[1] for tarea in tareas]

# Imprimir la cola de tareas
print(cola_tareas)