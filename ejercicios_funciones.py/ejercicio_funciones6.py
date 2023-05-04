# 6 Crear una función que calcule el área de un triángulo. Recibe dos parámetros (base y altura) 
# y devuelve el área.

def calcular_area_triangulo(base,altura):

    '''
    calcula el area de un triangulo
    recibe como parametro base y altura del mismo
    retorna el area calculada 
    '''

    area = (base*altura)/2
    return area

base_str = input("ingrese base del triangulo")
base = int(base_str)
altura_str =input("ingrese altura")
altura = int(altura_str)
area = calcular_area_triangulo(base,altura)

print("el area de este triangulo es de {0}".format(area))