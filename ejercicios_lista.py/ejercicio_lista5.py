'''Crea una lista con los nombres de 5 ciudades y luego imprime el último elemento de la lista.
'''
contador = 0 
lista = []

while(contador < 5):
    palabra = input("ingrese nombre de ciudad ")
    lista.append(palabra)
    contador = contador + 1 
print(lista[len(lista)-1])
