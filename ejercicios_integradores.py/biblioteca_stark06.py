from data_stark import lista_personajes
import json
#==========================================================================================
def imprimir_dato(texto_a_colocar,dato):
      '''
      imprime un dato por consola
      recibe como parametro un texto y un dato 
      no tiene retorno
      '''
      print(texto_a_colocar,dato)
#==========================================================================================
def imprimir_menu_desafio_6():
        '''
        imprime un menu
        no tiene parametro
        no retorna nada 
        
        '''
        imprimir_dato("Menú de opciones:","")
        imprimir_dato("1. Mostrar superheroes odenados por altura de menor a mayor ","")
        imprimir_dato("2. Mostrar superheroes odenados por peso de menor a mayor","")
        imprimir_dato("3. Mostrar superheroes odenados de forma alfabética ascendente ","")
        imprimir_dato("4. Mostrar superheroes odenados por largo del nombre de forma descendente","")
        imprimir_dato("5. Mostrar superheroes odenados segun se elija","")
        imprimir_dato("0. Salir","")


def stark_menu_principal_desafio_6():
      '''
      imprime el menu principal y le pide al usuario una opcion y la valida con la funcion de 
      validacion de enteros
      no tiene parametros
      retnorna la opcion casteada a entero si es posible , sino retorna -1
      '''
      imprimir_menu_desafio_6()
      opcion = input("\nIngrese la opción deseada: ")
      if ( validar_entero(opcion) == True):
            return  int(opcion)
      else:
            return -1
#==========================================================================================
def validar_entero(string):
      '''
      valida si un string esta compuesto por enteros usando la tabla ascii
      recibe un str como parametro
      retorna true si todo el str esta compuesto por numero, y false si no es asi 
      '''
      flag = None
      for letra in string:
            if (ord(letra)>= 48 and ord(letra)<= 57):
                  flag= True
            else :
                  flag = False
      return flag
#==========================================================================================

def stark_marvel_app_desafio_6(lista_heroes,opcion):
      '''
      tiene las opcines con sus respectivas funciones dentro de los if
      recibe una lista como párametro y la opcion a ejecutar
      retorna la accion de la opcion que se a elegido 
      '''
      #Mostrar los nombres de todos los superheroes del genero M
      if (opcion == 1 ):
          crear_archivo_json(ordenar_por_altura(lista_personajes),"Lista_ordenada_por_altura")
      elif(opcion == 2):
            crear_archivo_json(ordenar_por_peso(lista_personajes),"Lista_ordenada_por_peso")
      elif(opcion == 3):
           crear_archivo_json(ordenar_por_nombre(lista_personajes),"Lista_ordenada_alfabeticamente")
      elif(opcion == 4):
         crear_archivo_json(ordenar_por_largo_nombre(lista_personajes),"Lista_ordenada_por_longitud_nombre")
      elif(opcion == 5):
         key = input("elija key: ")
         sentido = input("elija sentido como A para ascendente o D para descendente: ")
         if(sentido == "A"):
              sentido = True
         if(sentido == "D"):
              sentido = False
         crear_archivo_json(ordenar_por_key(lista_personajes,key,sentido),"lista_ordenada_por_{0}_semtido_{1}".format(key,sentido))
      elif(opcion == 0):
            
            return 0
#===============================================================================================
def normalizar_dato(lista):
    for personaje in lista:
                personaje["altura"] = float(personaje["altura"]) 
                personaje["peso"] = float(personaje["peso"])
                personaje["fuerza"] = float(personaje["fuerza"])
  
    return lista
#===============================================================================================
# 1-Crear una función llamada ‘ordenar_por_altura’ que reciba como parámetro la lista de héroes 
# y devuelva la lista ordenada por la altura de cada personaje de menor a mayor. 
def ordenar_por_altura(lista:list):
    '''
    ordena por altura de menor a mayor la lista de diccionarios
    toma como parametor una lista
    retorna una lista ordenada de menor a mayor
    '''
    lista_normalizada = normalizar_dato(lista)
    rango_a = len(lista_normalizada)
    flag_swap = True

    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1

        for indice_A in range(rango_a):
            if  lista_normalizada[indice_A]["altura"] > lista_normalizada[indice_A+1]["altura"]:
                lista_normalizada[indice_A] ,lista_normalizada[indice_A+1] = (lista_normalizada[indice_A+1]) ,(lista_normalizada[indice_A])
                flag_swap = True

    return lista_normalizada
#===============================================================================================
# 2-Crear una función llamada ‘ordenar_por_peso’ que reciba como parámetro la lista de héroes
# y devuelva la lista ordenada por el peso de cada personaje mayor a mayor. 
def ordenar_por_peso(lista:list):
    '''
    ordena por peso de mayor a menor la lista de diccionarios
    toma como parametor una lista
    retorna una lista ordenada de mayor a menor
    '''
    lista_normalizada = normalizar_dato(lista)
    rango_a = len(lista_normalizada)
    flag_swap = True

    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1

        for indice_A in range(rango_a):
            if  lista_normalizada[indice_A]["peso"] < lista_normalizada[indice_A+1]["peso"]:
                lista_normalizada[indice_A] ,lista_normalizada[indice_A+1] = lista_normalizada[indice_A+1] ,lista_normalizada[indice_A]
                flag_swap = True

    return lista_normalizada
#===============================================================================================
# 3-Crear una función llamada ‘ordenar_por_nombre’ que reciba como parámetro la lista de héroes 
# y la devuelva la lista de héroes ordenada por nombres de forma alfabética ascendente (de la A a la Z)
def ordenar_por_nombre(lista:list):
    '''
    odena alfabeticamente de manera ascendente la lista de diccionarios por su nombre
    toma como parametro una lista
    retorna la lista ordenada 
    
    '''   
    rango_a = len(lista)
    flag_swap = True

    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1

        for indice_A in range(rango_a):
            if  ord(lista[indice_A]["nombre"][0]) > ord(lista[indice_A+1]["nombre"][0]):
                lista[indice_A] ,lista[indice_A+1] = (lista[indice_A+1]) ,(lista[indice_A])
                flag_swap = True

    return lista
#===============================================================================================
# 4-Crear una función llamada ‘ordenar_por_largo_nombre’ que reciba como parámetro la lista de 
# héroes y la devuelva la lista de héroes ordenada por el largo del nombre de forma descendente
def ordenar_por_largo_nombre(lista:list):
    '''
    odena por longitud de manera descendente la lista de diccionarios por su nombre
    toma como parametro una lista
    retorna la lista ordenada 
    '''
    
    rango_a = len(lista)
    flag_swap = True

    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1

        for indice_A in range(rango_a):
            if  len(lista[indice_A]["nombre"]) < len(lista[indice_A+1]["nombre"]):
                lista[indice_A] ,lista[indice_A+1] = (lista[indice_A+1]) ,(lista[indice_A])
                flag_swap = True

    return lista

#===============================================================================================
# 5-Crear una función llamada ‘ordenar_por_key’ la misma recibirá tres parámetros: 
'''
ordena segun el key elegido y el sentido elegido la lista
toma como parametro una lista, el key por el cual se quiere ordenar y el sentido (ascendente o descendente)
retorna la lista ya ordenada 
'''

# La lista de héroes 
# Un string que represente el nombre de una key
# Un booleano que represente el sentido de ordenamiento (por defecto debe tomar el valor True)

# La función deberá ordenar la lista de personajes según la key especificada. El sentido de
# ordenamiento lo determina el tercer parámetro, en caso de ser True el orden va a ser ascendente
# (de menor a mayor) y en el caso de ser False el sentido es descendente (mayor a menor)
def ordenar_por_key(lista:list,key:str,sentido:bool=True):
    lista_normalizada = normalizar_dato(lista)
    lista_key=["altura","fuerza","peso"]
    rango_a = len(lista)
    flag_swap = True
    
    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1
        if(key in lista_key):
            if(sentido == True):
                  for indice_A in range(rango_a):
                        if  lista_normalizada[indice_A][key] <  lista_normalizada[indice_A+1][key] :
                              lista_normalizada[indice_A], lista_normalizada[indice_A+1] =  lista_normalizada[indice_A+1], lista_normalizada[indice_A]
                              flag_swap = True
            else:
                  for indice_A in range(rango_a):
                        if  lista_normalizada[indice_A][key]  >  lista_normalizada[indice_A+1][key] :
                              lista_normalizada[indice_A], lista_normalizada[indice_A+1] =  lista_normalizada[indice_A+1], lista_normalizada[indice_A]
                              flag_swap = True
        if(key == "nombre"):
             if(sentido == True):
                  for indice_A in range(rango_a):
                        if  ord(lista_normalizada[indice_A]["nombre"][0]) > ord(lista_normalizada[indice_A+1]["nombre"][0]):
                              lista_normalizada[indice_A] ,lista_normalizada[indice_A+1] = lista_normalizada[indice_A+1] ,lista_normalizada[indice_A]
                              flag_swap = True
             else:
                  for indice_A in range(rango_a):
                        if  ord(lista_normalizada[indice_A]["nombre"][0]) < ord(lista_normalizada[indice_A+1]["nombre"][0]):
                              lista_normalizada[indice_A] ,lista_normalizada[indice_A+1] = lista_normalizada[indice_A+1] ,lista_normalizada[indice_A]
                              flag_swap = True      

             
    return lista_normalizada
             

#===============================================================================================
def crear_archivo_json(lista,nombre_archivo):
      '''
      esta funcion guarda los diccionarios en un archivo .json
      recibe como parametro una lista y el nombre a poner al archivo
      no tiene retorno 
      '''

      with open("{0}.json".format(nombre_archivo),"w") as archivo:
      
            lista_vacia = []
            for personaje in lista:
                  
                  lista_vacia.append(personaje)
            json.dump(lista_vacia, archivo, indent=4, ensure_ascii=False )
