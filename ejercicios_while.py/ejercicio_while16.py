# Dada una lista de números, imprimir todos los números que son múltiplos de 3.
numero_ingresado = input("ingresar numero please")
numero_casteado = int(numero_ingresado)

while(numero_casteado > 0):
    if(numero_casteado % 3 == 0):
        print(numero_casteado)
    numero_casteado = numero_casteado - 1 
