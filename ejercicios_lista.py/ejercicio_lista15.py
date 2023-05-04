# Crea una lista de números enteros y luego encuentra la suma de los números en índices impares.
lista = [1,2,3,6,5,85,75,85,98,100,112,12]
acumulador = 0

for i in range(len(lista)):
    if(i %2 !=0):
        acumulador = acumulador + lista[i]
print(acumulador)
