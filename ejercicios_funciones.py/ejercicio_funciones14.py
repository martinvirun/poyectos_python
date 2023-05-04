# 14 Crear una función que recibe una lista de números y 
# devuelve un diccionario con el valor mínimo, el valor máximo y el 
# promedio de los números en la lista.

def calcular_min_max_promedio_en_lista(lista_numeros):
    acumulador = 0
    for i in range(len(lista_numeros)):
        acumulador = acumulador + lista_numeros[i]
        if (i == 0):
            numero_min = lista_numeros[i]
            numero_max = lista_numeros[i]
        else:
            if(numero_min > lista_numeros[i]):
                numero_min = lista_numeros[i]
            if(numero_max < lista_numeros[i]):
                numero_max =lista_numeros[i]
    promedio = acumulador/ len(lista_numeros)
    dic={}
    dic["maximo"]=numero_max
    dic["minimo"]=numero_min
    dic["promedio"]=promedio
    return dic

lista =[1,2,6,5]

print(calcular_min_max_promedio_en_lista(lista))