# Crea una lista vacía y pide al usuario que ingrese números enteros hasta que ingrese un número negativo.
# Luego, muestra la suma de todos los números ingresados.
lista = []
flag = True
acumulador = 0 
while(flag == True):
   numero_ingresado = input("ingresa un numero: ")
   numero_casteado = int(numero_ingresado)
   if(numero_casteado > 0):
      lista.append(numero_casteado)
   else:
      flag = False
for indice in range(len(lista)):
   acumulador = acumulador + lista[indice]
print(acumulador)
