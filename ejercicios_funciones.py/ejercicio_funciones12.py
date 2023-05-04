# 12 Crea una función que reciba dos listas de nombres, y devuelva una lista con los
# nombres que aparecen en ambas listas

def identificar_misma_palabra_en_dos_listas(lista_uno , lista_dos):
    '''
    identifica si en dos listas hay palabras repetidas y crea una nueva lista con esas palabras
    recibe como parametro dos listas 
    retorna la nueva lista de palabras con las palabras que se repiten en ambas listas 
    '''
    nueva_lista = []
    for palabra in lista_uno :
        for palabra_dos in lista_dos:
            if (palabra == palabra_dos):
                nueva_lista.append(palabra)
    return nueva_lista

lista_uno = ["hola","chau"]
lista_dos = ["chau","hola"]

print(identificar_misma_palabra_en_dos_listas(lista_uno , lista_dos))
