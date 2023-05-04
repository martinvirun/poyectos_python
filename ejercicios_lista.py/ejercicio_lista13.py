# Crea una lista de números y encuentra el promedio de todos los números en la lista.
lista = [1,2,3,6,5,85,75,85,98,100,112,12]
acumulador = 0


for i in range(len(lista)):
    acumulador = acumulador + lista[i]
promedio = acumulador / len(lista)
print(promedio)
#,6,5,85,75,85,98,100,112,12
