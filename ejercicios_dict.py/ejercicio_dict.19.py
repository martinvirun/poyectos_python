# Crea un diccionario que represente las temperaturas de una ciudad durante una semana,
# donde las claves son los días de la semana y los valores son las temperaturas correspondientes. 
# Calcula la temperatura promedio de la semana.
dict_temperatura = {"lunes":25,"martes":35,"miercoles":27,"jueves":23,"viernes":31,"sabado":28,"domingo":29}
acumulador = 0 
contador = 0


for dia in dict_temperatura:
    contador = contador + 1 
    acumulador = acumulador + dict_temperatura[dia] 
promedio = acumulador / contador 
print("la temperatura promedio de la seman es de {0}".format(round(promedio,2)))