import re
import json
def abrir_archivo(ruta:str):
    with open(ruta,"r") as archivo:
        lista_personajes = []
        lista_personajes = json.load(archivo)
    return lista_personajes
personajes = abrir_archivo("/home/martin/Documentos/programacion_1/data_stark.json")
lista_personajes = personajes["heroes"]
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
        imprimir_dato("1. Mostrar superheroes cantidad de superheroes a eleccion ","")
        imprimir_dato("2. Mostrar superheroes odenados por altura ","")
        imprimir_dato("3. Mostrar superheroes odenados por fuerza ","")
        imprimir_dato("4. Mostrar superheroes mayor o menor promedio","")
        imprimir_dato("5. Mostrar superheroes segun inteligencia","")
        imprimir_dato("0. Salir","")
#==========================================================================================
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
           
           cantidad = input("ingrese cantidad de heroes a listar")
           cantidad = int(cantidad)
           listar_cantidad_heroes(lista_personajes,cantidad)
      elif(opcion == 2):
           sentido = input("ingrese sentido como ascendente(‘asc’) o descendente (‘desc’)")
           guardar_archivo_csv(listar_por_altura(lista_personajes, sentido),"diccionario_ordenados_por_altura_{0}".format(sentido))
      elif(opcion == 3):
           sentido = input("ingrese sentido como ascendente(‘asc’) o descendente (‘desc’)")
           guardar_archivo_csv(listar_por_fuerza(lista_personajes,sentido),"diccionario_ordenados_por_fuerza_{0}".format(sentido))
      elif(opcion == 4):
           key = input("ingrese key a eleccion como altura-fuerza-peso")
           sentido = input("ingrese mayor o menor")
           print(promediar_y_mostrar_segun_condicion(lista_personajes,key,sentido))
      elif(opcion == 5):
           inteligencia = input("ingrese inteligencia como -good, average, high-")
           print(buscar_por_inteligencia(lista_personajes,inteligencia))
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

#===============================================================================================
#1- Listar los primeros N héroes. El valor de N será ingresado por el usuario  
# (Validar que no supere max. de lista)
def listar_cantidad_heroes(lista:list,cantidad:int):
      contador = 0
      if(cantidad <= len(lista)):

         for personaje in lista: 
              contador += 1
              print(personaje["nombre"])
              if(contador == cantidad):
                  break
      else:
           print("el valor es invalido")

#====================================================================================================
#2-Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera ascendente 
# (‘asc’) o descendente (‘desc’)
def listar_por_altura(lista:list,sentido:str):
    if(len(lista)>1):
      lista_normalizada = normalizar_dato(lista)
      rango_a = len(lista_normalizada)
      flag_swap = True
      while(flag_swap):
          flag_swap = False
          rango_a = rango_a - 1
          
          if (re.search("asc",sentido)!= None ):
                  
                  for indice_A in range(rango_a):
                        if  lista_normalizada[indice_A]["altura"] > lista_normalizada[indice_A+1]["altura"]:
                              lista_normalizada[indice_A] ,lista_normalizada[indice_A+1] = (lista_normalizada[indice_A+1]) ,(lista_normalizada[indice_A])
                              flag_swap = True
          if(re.search("desc",sentido) != None):
                  for indice_A in range(rango_a):
                        if  lista_normalizada[indice_A]["altura"] < lista_normalizada[indice_A+1]["altura"]:
                              lista_normalizada[indice_A] ,lista_normalizada[indice_A+1] = (lista_normalizada[indice_A+1]) ,(lista_normalizada[indice_A])
                              flag_swap = True
    else:
          return lista
    return lista_normalizada
#=====================================================================================================

#3-Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente 
# (‘asc’) o descendente (‘desc’)
def listar_por_fuerza(lista:list,sentido:str):
    if(len(lista)>1):
      lista_normalizada = normalizar_dato(lista)
      rango_a = len(lista_normalizada)
      flag_swap = True
      while(flag_swap):
          flag_swap = False
          rango_a = rango_a - 1
          
          if (re.search("asc",sentido)!= None ):
                  
                  for indice_A in range(rango_a):
                        if  lista_normalizada[indice_A]["fuerza"] > lista_normalizada[indice_A+1]["fuerza"]:
                              lista_normalizada[indice_A] ,lista_normalizada[indice_A+1] = (lista_normalizada[indice_A+1]) ,(lista_normalizada[indice_A])
                              flag_swap = True
          elif(re.search("desc",sentido) != None):
                  for indice_A in range(rango_a):
                        if  lista_normalizada[indice_A]["fuerza"] < lista_normalizada[indice_A+1]["fuerza"]:
                              lista_normalizada[indice_A] ,lista_normalizada[indice_A+1] = (lista_normalizada[indice_A+1]) ,(lista_normalizada[indice_A])
                              flag_swap = True
    else:
          return lista
    return lista_normalizada

#=====================================================================================================
#4-Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar 
# o no el promedio (preguntar al usuario la condición: ‘menor’ o ‘mayor’) se deberá 
# listar en consola aquellos que cumplan con ser mayores o menores según corresponda.
def promediar_y_mostrar_segun_condicion(lista:list,key,condicion):
      lista_normalizada = normalizar_dato(lista) 
      lista_condicion = []
      acumulador = 0
      for personaje in lista_normalizada:
                  acumulador = acumulador + personaje[key]
      promedio = acumulador/len(lista)
      if(re.search("mayor",condicion)!= None):
            for personaje in lista_normalizada:
                  if (personaje[key]<promedio):
                      lista_condicion.append(personaje["nombre"]) 
      if(re.search("menor",condicion)!= None): 
            for personaje in lista_normalizada:
                  if (personaje[key]>promedio):
                      lista_condicion.append(personaje["nombre"]) 
      print("====={0}".format(promedio))
      return lista_condicion


#=====================================================================================================
#5- Buscar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha
#    búsqueda. (Usando RegEx)
def buscar_por_inteligencia(lista:list,inteligencia:str):
      lista_por_inteligencia = []

      for personaje in lista:
            if(re.search(inteligencia,personaje["inteligencia"])):
                lista_por_inteligencia.append(personaje["nombre"])   
      return lista_por_inteligencia

#======================================================================================================
#6-Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]
def guardar_archivo_csv(lista:list,nombre:str):
    with open("{0}.csv".format(nombre),"w") as file:
          mensaje = ""
          for personaje in lista:
                mensaje = mensaje +"\n"
                for clave in personaje:
                        if(clave == list(personaje.keys())[-1]):
                               mensaje = mensaje + "{0}: {1}.".format(clave,personaje[clave])
                        else:
                               mensaje = mensaje + "{0}: {1},".format(clave,personaje[clave])
          file.write(mensaje)
# Aclaraciones:
# Los puntos deben ser accedidos mediante un menú. Para todas las opciones, validar lo ingresado 
# por consola con RegEx
# El set de datos proviene de un json
# Realizar las validaciones que crea pertinentes
# En todos los casos se deberá trabajar con una copia de la lista original
#================================================================================================
