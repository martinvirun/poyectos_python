# Crea un diccionario que represente una lista de tareas por hacer. 
# Cada clave del diccionario debe ser el nombre de una tarea y cada valor debe ser su estado
# (los estados son:  pendiente, en proceso, completada). Imprimir todas las tareas seguido de su estado
dict_tareas = {"lavar":"pendiente","planchar":"en proceso","estudiar":"completada",
               "trabajar":"pendiente","cocinar":"en proceso"}

for tareas in dict_tareas:
    print("la tarea es {0} y su estado es {1}".format(tareas,dict_tareas[tareas]))