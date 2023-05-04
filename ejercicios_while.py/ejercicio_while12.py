'''Dado un número entero n, imprimir la suma de todos los números impares menores o iguales a n.'''
numero_ingresado = input("ingresar numer ")
numero_casteado = int(numero_ingresado)
acumulador = 0

while(numero_casteado > 0):
    if(numero_casteado % 2 != 0):
        acumulador = acumulador + numero_casteado
    numero_casteado = numero_casteado - 1
print(acumulador)