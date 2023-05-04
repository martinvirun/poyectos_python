
# 5 Crear una función que determine si un número es primo o no. Recibe un parámetro (número)
# y devuelve True si es primo y False si no lo es.

def calcular_si_es_primo(numero):
    '''
    calcula si es primo o no 
    recibe como parametro un numero
    retorno true si es primoo false si no lo es 
    '''
    contador = 0 
    while(numero > 2):
        numero = numero - 1 
        if (numero % numero == 0):
            contador = contador + 1 
    if(contador !=0):
      return True
    else:
      return  False
    
numero_str = input("ingrese numero ")
numero = int(numero_str)
print(calcular_si_es_primo(numero))