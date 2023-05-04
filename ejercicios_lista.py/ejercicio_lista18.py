# Solicitar al usuario números enteros hasta que ingrese el 0. Almacenar los números en una lista
# y luego imprimir el mayor (sin utilizar la función max())
lista = []
flag = True


while(flag == True):
    numero_ingresado = input("ingresa numero")
    numero_casteado = int(numero_ingresado)

    if (numero_casteado !=0):
        lista.append(numero_casteado)
    else:
        break
print(lista)
if(len(lista)>0):
    numero_maximo = lista[0]
    for numero in lista:
        if (numero > numero_maximo):
            numero_maximo= numero

print(numero_maximo)


        
