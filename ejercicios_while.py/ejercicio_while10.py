'''Dada una lista de números, imprimir la cantidad de números pares en la lista.'''
lista_numeros = [1,5,8,9,6,10,18,16,11,14,15,16,8]

tamano_lista = len(lista_numeros)
contador_pares = 0

while(tamano_lista > 0):
    if(lista_numeros[tamano_lista-1] %2 == 0):
        contador_pares = contador_pares + 1 
    tamano_lista = tamano_lista-1
print(contador_pares)

