# Crea una lista vacía y pide al usuario que ingrese una palabra. Luego, 
# agrega la palabra a la lista si no se encuentra ya en la lista.
# Repite este proceso hasta que la lista tenga al menos 5 palabras.

lista = []
flag = True
flag_dos = True
contador = 0
while(flag==True):
    palabra = input("ingrese palabra")
    if(flag_dos == True):
     lista.append(palabra)
     print(lista)
     flag_dos = False
    else:
       for i in lista:
          if(i != palabra):
              lista.append(palabra)
              contador = contador + 1
          else:
           break
              
    if (contador == 5):
       flag = False
print(lista)
