'''Dada una lista de palabras, imprimir todas las palabras que tengan una longitud mayor a 5 caracteres.'''
lista_palabras = ["solaaaa","calaaaa","cacacaa","salaaaa","unaaaa","una","holaaa"]
tamaño_lista = len(lista_palabras)

while(tamaño_lista > 0 ):
    if(len(lista_palabras[tamaño_lista-1]) >= 5 ):
        print(lista_palabras[tamaño_lista-1])
    tamaño_lista = tamaño_lista-1

