'''Crea una lista vacía y pide al usuario que ingrese una palabra. 
Luego, muestra la primera letra de la palabra. Repite este proceso hasta que el usuario ingrese una palabra
 que comience con la letra "z".
'''
flag = True
while(flag == True): 
    palabra = input("ingrese una palabra ")
    if (palabra[0]=="z"):
        flag = False
    else:
        print(palabra[0])
