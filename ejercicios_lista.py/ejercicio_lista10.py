# Crea una lista de palabras y muestra las palabras que tienen más de 5 letras.

lista = ["holas","chau","palacio","teatro","calculadora","locura","lolaaa"]

for i in range(len(lista)):
    if(len(lista[i])>=5):
        print(lista[i])