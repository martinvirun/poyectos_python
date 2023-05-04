# 9 Crear una función que cuente la cantidad de veces que aparece un elemento en una lista. 
# Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que 
# aparece en la lista.

def calcular_veces_que_aparece_un_elementor(lista_elementos,elemento):

    '''
    calcula cauantas veces aparace un elementro
    recibe una lista de elementos como parametro y un elemento a buscar
    retorna la cantidad de veces que aparece 
    '''
    contador = 0 
    for ele in lista_elementos:
        if(elemento == ele ):
            contador = contador + 1 
    return contador

lista = [5,5,5,5,8,9,7]

numero_str = input("ingresa numero")
numero = int(numero_str)

cantidad = (calcular_veces_que_aparece_un_elementor(lista,numero))

print("la cantidad de veces que aparece ese numero es {0}".format(cantidad))
