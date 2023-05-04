# Crea una lista de números enteros y pide al usuario que ingrese otro número entero.
# Luego, busca el número ingresado en la lista y muestra la posición en la que se encuentra. 
# Si el número no se encuentra en la lista, muestra un mensaje indicando que no se encontró
lista = [2,5,6,7,8,9,48,57,22,65,45,58,99,17]
contador = 0
numero_ingresado = input("ingresa el numero")
numero_casteado = int(numero_ingresado)
flag = False

for i in range(len(lista)):
   if(numero_casteado == lista[i]):
        print(i)
        flag = True
if(flag==False):
       print("no se encontro numero ")
   