'''Dado un número entero n, imprimir si el número es primo o no.'''
numero_ingresado = input("ingresar numero")
numero_casteado = int(numero_ingresado)
contador = 0 
numero = numero_casteado

while(numero > 2):
    numero = numero - 1 
    if (numero_casteado % numero == 0):
        contador = contador + 1 
if(contador !=0):
    print("el numero no es primo")
else:
    print("el numero es primo")
    
