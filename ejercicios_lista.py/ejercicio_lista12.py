# Crea una lista con los nombres de tus 3 películas favoritas y luego imprime los elementos en orden inverso 
# (sin utilizar el método reverse())
lista = []
contador = 0
contador_dos = 1

while(contador < 3):
    peli = input("ingresa una peli")
    lista.append(peli)
    contador = contador + 1
while((len(lista) - contador_dos ) >= 0):
    print(lista[len(lista)- contador_dos])
    contador_dos = contador_dos + 1 