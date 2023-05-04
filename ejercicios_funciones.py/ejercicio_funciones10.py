# 10 Crea una función que reciba como parámetros una lista de palabras y devuelva 
# la palabra más larga.


def calcular_palabra_mas_larga(lista_palabras):

    '''
    calucula la palabra mas larga en una lista
    recibe como parametro una lista de palabras
    retorna la palabra mas larga 
    '''

    for i in range(len(lista_palabras)):
        if (i == 0):
           palabra_mas_larga =  lista_palabras[i]
           
        else :
            if ( len(lista_palabras[i]) > len(palabra_mas_larga)):
                palabra_mas_larga = lista_palabras[i]
    return  palabra_mas_larga

lista= ["hola","holaaaaa"]
print(calcular_palabra_mas_larga(lista))