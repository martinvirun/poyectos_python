'''Dado un número entero n, imprimir todos los números desde n hasta 1 en orden descendente.
'''
numero_ingresado = input("ingresar numero")
numero_casteado = int(numero_ingresado)

while(numero_casteado >=1):
    print(numero_casteado)
    numero_casteado = numero_casteado - 1