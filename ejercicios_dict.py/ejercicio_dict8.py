# Crea un diccionario que represente las edades de varias personas, 
# donde las claves son los nombres de las personas y los valores son sus edades. Imprime la edad de la persona más joven.

dict_edades = {"carlos":15,"laura":50,"martin":26,"juan":5}
edad_menor = dict_edades["carlos"]
for edades in dict_edades.keys():

    if (edad_menor >dict_edades[edades]):
        edad_menor = dict_edades[edades]
print(edad_menor)
    