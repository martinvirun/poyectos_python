# Crea dos listas de 10 números enteros cada una y realiza una multiplicación de los elementos
# con el mismo índice en ambas listas.
lista_uno = [1,3,4,5,6,8,5,7,5,6,4,5]
lista_dos = [1,3,4,5,6,8,5,7,5,6,4,5]

for i in range(len(lista_dos)):
    resultado = lista_uno[i] * lista_dos[i]
    print("la multiplicacion {0}".format(resultado))