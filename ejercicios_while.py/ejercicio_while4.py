'''Dada una lista de números, imprimir la suma de todos los elementos de la lista.'''

lista_numeros = [1,2,33,45,5,6]
indice = 0 
tamaño_lista = len(lista_numeros)
suma = 0

while(indice < tamaño_lista ):
    suma = suma + lista_numeros[indice]
    indice = indice + 1 
print(suma)