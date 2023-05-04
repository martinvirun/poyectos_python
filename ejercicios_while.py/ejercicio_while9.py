'''Dado un número entero n, imprimir todos los números impares menores o iguales a n.'''
numero_ingreado = input("ingresa el numero ")
numero_casteado = int(numero_ingreado)


while(numero_casteado > 0 ):
    if ( numero_casteado % 2 != 0):
        print(numero_casteado)
    numero_casteado = numero_casteado - 1