# Dada una cadena de texto, imprimir la cantidad de veces que aparece una letra específica en la cadena.
cadena = input("ingrese cadena ")
letra = input("ingrese letra a buscar")
tamaño_cadena = len(cadena)
contador = 0

while(tamaño_cadena > 0):
    if(cadena[tamaño_cadena-1]== letra):
        contador = contador + 1 
    tamaño_cadena = tamaño_cadena-1
print(contador)
