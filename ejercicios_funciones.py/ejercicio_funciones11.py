# 11 Crea una función que reciba como parámetro una cadena de texto y devuelva
# la cantidad de vocales que tiene.

def calcular_cantidad_vocales(palabra):
    '''
    calcula la cantidad de vocales en una palabra 
    recibe como parametro una palabra 
    retorna la cantidad de vocales que contiene 
    '''
    vocales = ["a","e","i","o","u"]
    contador = 0
    for letra in palabra:
        if (letra in vocales):
            contador = contador +1
    return contador 

palabra = input("engresa una palabra ")

print(calcular_cantidad_vocales(palabra))