# 1 Crear una función que convierta grados Celsius a grados Fahrenheit. 
# Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.

def convertir_celsius_a_Fahrenheit(grados_a_convertir):
    '''
    Convierte de grados Celsius a grados Fahrenheit. 
    Esta funcion recibe como parametro los grados a convertir a Fahrenheit
    retorna la transformacion de grados

    '''
    resultado = grados_a_convertir * 1.8 + 32
    return round(resultado,2)
grados_str=input("ingresar grados")
grados_a_convertir = float(grados_str)
print(convertir_celsius_a_Fahrenheit(grados_a_convertir))