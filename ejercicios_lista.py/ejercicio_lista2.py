# Crea una lista con 5 números enteros. 
# Luego solicita un nuevo número y reemplaza el tercer elemento de la lista por el número ingresado. 
# Finalmente imprime todos los números
lista = [10,5,6,5,8]
numero_ingresado = input("ingresa numero ")
numero_casteado = int(numero_ingresado)

lista[2] = numero_casteado
print(lista) 
