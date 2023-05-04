# Crea un diccionario que represente las notas de un examen de varios estudiantes, 
# donde las claves son los nombres de los estudiantes y los valores son sus notas.
# Imprime el promedio de las notas.
dict_notas = {"martin":10,"laura":5,"carla":8,"lolo":9,"marcos":6}
aculador = 0
contador = 0

for notas in dict_notas.keys():
    contador = contador + 1 
    aculador = aculador + dict_notas[notas]
promedio = aculador / contador 

print("el promedio de las notas es de : {0}".format(promedio))
