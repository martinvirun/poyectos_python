'''Dada una cadena de texto, imprimir cada uno de los caracteres en la cadena.'''
cadena = input("ingrese palabra")
tamaño_cadena = len(cadena)
indice = 0 


while(tamaño_cadena > 0):
    print(cadena[indice])
    tamaño_cadena = tamaño_cadena-1
    indice = indice + 1 