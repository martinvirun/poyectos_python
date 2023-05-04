# Crea un diccionario que represente una lista de tareas pendientes,
# donde las claves son las tareas y los valores son "True" si están completadas y "False" si no lo están.
# Solicita al usuario el nombre de una tarea y modifica el valor para marcarla como completada.
# Imprimir el listado de tareas pendientes

dict_tareas = {"lavar":False,"limpiar":False,"cocinar":True,"ordenar":True}

tareas = input("ingrese la tarea que quiera marcar como completa")

for tarea in dict_tareas:
    if (tarea == tareas):
        dict_tareas[tarea] = True
for tarea in dict_tareas:
    if (dict_tareas[tarea]== True):
      print("{0}...completa ".format(tarea))