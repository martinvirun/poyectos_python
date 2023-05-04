# 8 Crear una función que verifique si un número es par o impar. 
# Recibe un número como parámetro y devuelve True si es par o False si es impar.


def verificar_si_es_par(numero):
    '''
    verifica si un numero es par o no
    recibe como parametro un numero
    retorna true si es par o false si no lo es 

    '''
    if (numero % 2 == 0 ):
    
        return  True
    else:
        return False


numero_str = input("ingresa numero")
numero = int(numero_str)

print(verificar_si_es_par(numero))