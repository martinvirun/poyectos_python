# Crea una lista de palabras y pide al usuario que ingrese una palabra.
# Luego, muestra todas las palabras de la lista que tienen la misma longitud que la palabra ingresada.

lista = ["hola","chau","sol","calculadora","homero","bart","lisa"]
palabra = input("ingrese palabra: ")
tamaño = len(palabra)

for i in range(len(lista)):
    if(len(lista[i]) == tamaño):
        print(lista[i])