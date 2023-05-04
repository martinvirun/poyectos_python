
# 2 Crear una función que calcule el área de un círculo. Recibe un parámetro (radio) 
# y devuelve el área del círculo.

def calcular_area_circulo(radio):
    '''
    calcula area de un circulo
    recibe como parametro el radio 
    retorna el area
    '''
    area = radio*radio*3.14
    return area

radiostr = input("ingrese radio de un circulo")
radio = float(radiostr)
print("el area es {0}".format(calcular_area_circulo(radio)))