'''Dada una lista de números, imprimir todos los números que son mayores que el promedio de la lista.'''
lista = [2,5,6,8,78,98,58,65,45,65]
tamaño_lista= len(lista)
indice = tamaño_lista
acumulador =0
promedio=0

for i in range(0,tamaño_lista-1):
    acumulador = acumulador + lista[i]
promedio = acumulador/tamaño_lista

while(indice >= 0):
    if (lista[indice-1] > promedio ):
        print(lista[indice-1])
    indice = indice - 1