
# 13 Crear una función que recibe una lista de palabras y 
# devuelve un diccionario con las palabras como llaves y su longitud como valores.

def convertir_lista_en_diccionario(lista_de_palabras):
    '''
    convierte una lista en un diccionario con la logitud de las palabras 
    recibe como parametro una lista de palabras 
    retorna el nuevo diccionario con los datos de la lista 
    '''

    nuevo_dic = {}

    for palabra in lista_de_palabras:
        nuevo_dic[palabra]=len(palabra)
    return nuevo_dic

lista = ["hola","chau"]
print(convertir_lista_en_diccionario(lista))