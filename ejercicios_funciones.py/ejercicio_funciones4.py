# 4 Crear una función que calcule el promedio de edad de un grupo de personas. 
# Recibe una lista de edades y devuelve el promedio.

def calcular_promedio_edades(lista_edades):
    acumulador = 0
    for edades in lista_edades:
        acumulador = acumulador + edades
    promedio = acumulador / len(lista_edades)


    return promedio

lista_edades = [15,16,17,25,45,74,11,5]
promedio = calcular_promedio_edades(lista_edades)
print("el promedio de las edades es de {0}".format(promedio))