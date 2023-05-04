'''Dada una cadena de texto, imprimir la cantidad de vocales en la cadena.'''
cadena = input("ingrese cadena  ")
tamaño_cadena = len(cadena)
contador_vocales = 0


while(tamaño_cadena > 0):
   if(cadena[tamaño_cadena-1]== "a" or cadena[tamaño_cadena-1]== "e" or cadena[tamaño_cadena-1]== "i"
       or cadena[tamaño_cadena-1]== "o"
       or cadena[tamaño_cadena-1]== "u"  ):
         contador_vocales = contador_vocales + 1
   tamaño_cadena = tamaño_cadena - 1 
   
print(contador_vocales)
