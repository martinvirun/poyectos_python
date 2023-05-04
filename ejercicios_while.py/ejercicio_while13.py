'''Dada una lista de números, imprimir la cantidad de números negativos en la lista.'''
lista_numeros = [-1,-5,-3,-5,-19,6,5,8,9,-6]
tamaño_lista = len(lista_numeros)

while(tamaño_lista > 0):
    if(lista_numeros[tamaño_lista-1]<0):
        print(lista_numeros[tamaño_lista-1])
    tamaño_lista = tamaño_lista-1