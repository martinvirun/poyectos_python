# Crea una lista con los nombres de tus 5 libros favoritos y luego imprime solo los primeros 3 libros de la lista.
contador = 0 
lista = []
while(contador < 5):
    palabra = input("ingrese nombre de libro : ")
    lista.append(palabra)
    contador = contador + 1
for i in range(0,3):
    print(lista[i])