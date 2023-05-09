import json
import re
from data_stark import lista_personajes
#==========================================================================================
def imprimir_dato(texto_a_colocar,dato):
      '''
      imprime un dato por consola
      recibe como parametro un texto y un dato 
      no tiene retorno
      '''
      print(texto_a_colocar,dato)
#==========================================================================================
# 1.1-Crear la función "imprimir_menu_desafio_5" que imprima el menú de opciones por pantalla 
# (las opciones son las que se van a utilizar para acceder a la funcionalidad de los puntos 
#  A hasta el O y Z para salir).  Reutilizar la función 'imprimir_dato' realizada en una práctica 
# anterior.
def imprimir_menu_desafio_5():
        '''
        imprime un menu
        no tiene parametro
        no retorna nada 
        
        '''
        imprimir_dato("Menú de opciones:","")
        imprimir_dato("1. Mostrar los nombres de todos los superheroes del genero M ","")
        imprimir_dato("2. Mostrar los nombres de todos los superheroes del genero F","")
        imprimir_dato("3. Mostrar superheroe mas alto del genero M ","")
        imprimir_dato("4. Mostrar superheroe mas alto del genero F ","")
        imprimir_dato("5. Mostrar superheroe mas bajo del genero M ","")
        imprimir_dato("6. Mostrar superheroe mas bajo del genero F ","")
        imprimir_dato("7. Mostrar altura promedio de los  superhéroes de género M ","")
        imprimir_dato("8. Mostrar altura promedio de los  superhéroes de género F ","")
        imprimir_dato("9. Mostrar altura promedio de los  superhéroes de género M ","")
        imprimir_dato("9. Mostrar nombre superhéroe más alto de género M y superhéroe más bajo  de género F  ","")
        imprimir_dato("10. Mostrar cuántos superhéroes tienen cada tipo de color de ojos ","")
        imprimir_dato("11. Mostrar cuántos superhéroes tienen cada tipo de color de pelo. ","")
        imprimir_dato("12. Mostrar cuántos superhéroes tienen cada tipo de inteligencia. ","")
        imprimir_dato("13. Listar todos los superhéroes agrupados por color de ojos. ","")
        imprimir_dato("14. Listar todos los superhéroes agrupados por color de pelo. ","")
        imprimir_dato("15. Listar todos los superhéroes agrupados por tipo de inteligencia ","")
        imprimir_dato("0. Salir del programa","")
#==========================================================================================
# 1.2-Crear la funcion 'stark_menu_principal_desafio_5' la cual se encargará de imprimir el menú 
# de opciones y le pedirá al usuario que ingrese la letra de una de las opciones elegidas, 
# deberá validar la letra usando RegEx y en caso de ser correcta tendrá que retornarla, 
# Caso contrario retornará -1. El usuario puede ingresar tanto letras minúsculas como mayúsculas 
# y ambas se deben tomar como válidas
# Reutilizar la función 'imprimir_menu_Desafio_5'

def stark_menu_principal_desafio_5():
      '''
      imprime el menu principal y le pide al usuario una opcion y la valida con la funcion de 
      validacion de enteros
      no tiene parametros
      retnorna la opcion casteada a entero si es posible , sino retorna -1
      '''
      imprimir_menu_desafio_5()
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
# 1.3-Crear la función 'stark_marvel_app_5' la cual recibirá por parámetro la lista de héroes y 
# se encargará de la ejecución principal de nuestro programa. (usar if/elif o match según prefiera) 
# Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.
def stark_marvel_app_desafio_5(lista_heroes,opcion):
      '''
      tiene las opcines con sus respectivas funciones dentro de los if
      recibe una lista como párametro y la opcion a ejecutar
      retorna la accion de la opcion que se a elegido 
      '''
      #Mostrar los nombres de todos los superheroes del genero M
      if (opcion == 1 ):
            stark_guardar_heroe_genero(lista_heroes,"m")
         
            
      elif(opcion == 2):
            #Mostrar los nombres de todos los superheroes del genero F
            stark_guardar_heroe_genero(lista_heroes,"f")
           
            
      elif(opcion == 3):
           # Mostrar superheroe mas alto del genero M "
            print(calcular_max_genero(lista_personajes,"altura","m"))
           
            
      elif(opcion == 4):
            #Mostrar superheroe mas alto del genero F "
            print(calcular_max_genero(lista_personajes,"altura","f"))
            pass
           
      elif(opcion == 5):
            #Mostrar superheroe mas bajo del genero M
            print(calcular_min_genero(lista_personajes,"altura","m"))
            pass
            
      elif(opcion == 6):
            #Mostrar superheroe mas bajo del genero f
             print(calcular_min_genero(lista_personajes,"altura","f"))
      elif(opcion == 7):
             #Mostrar altura promedio de los  superhéroes de género M
             print(calcular_promedio_genero(lista_personajes,"altura","m"))
      elif(opcion == 8):
           #Mostrar altura promedio de los  superhéroes de género F 
           print(calcular_promedio_genero(lista_personajes,"altura","f"))
           
      elif(opcion == 9):
             #Mostrar nombre superhéroe más alto de género M y superhéroe más bajo  de género F 
             imprimir_dato("la chica mas baja es :","")
             print(calcular_min_genero(lista_personajes,"altura","f"))
             imprimir_dato("el hombre mas alto es :","")
             print(calcular_max_genero(lista_personajes,"altura","m"))
           
      elif(opcion == 10):
           #Mostrar cuántos superhéroes tienen cada tipo de color de ojos
           print(calcular_cantidad_tipo(lista_personajes,"color_ojos"))
           pass
      elif(opcion == 11):
           #Mostrar cuántos superhéroes tienen cada tipo de color de pelo.
           print(calcular_cantidad_tipo(lista_personajes,"color_pelo"))
           pass
      elif(opcion == 12):
           #Mostrar cuántos superhéroes tienen cada tipo de inteligencia
           print(calcular_cantidad_tipo(lista_personajes,"inteligencia"))
           pass
      elif(opcion == 13):
           #Listar todos los superhéroes agrupados por color de ojos.
           print(obtener_heroes_por_tipo(lista_personajes,obtener_lista_de_tipos(lista_personajes,"color_ojos"),"color_ojos"))
           pass
      elif(opcion == 14):
           #Listar todos los superhéroes agrupados por color de pelo
           print(obtener_heroes_por_tipo(lista_personajes,obtener_lista_de_tipos(lista_personajes,"color_pelo"),"color_pelo"))
           pass
      elif(opcion == 15):
           #Listar todos los superhéroes agrupados por inteligencia
           print(obtener_heroes_por_tipo(lista_personajes,obtener_lista_de_tipos(lista_personajes,"inteligencia"),"inteligencia"))
           pass
     
      elif(opcion == 0):
          return 0
      else:
            print("Opcion ingresada es invalida") 
#==========================================================================================
# 1.4-Crear la función 'leer_archivo' la cual recibirá por parámetro un string que indicará el nombre 
# y extensión del archivo a leer (Ejemplo: archivo.json). Dicho archivo se abrirá en modo lectura 
# únicamente y retornará la lista de héroes como una lista de diccionarios.
def leer_archivo(string:str):
    lista = []
    with open(string) as file:
     data = json.load(file)
     lista = data["heroes"]
     return lista
      
#==========================================================================================
# 1.5-Crear la función 'guardar_archivo' la cual recibirá por parámetro un string que indicará el 
# nombre con el cual se guardará el archivo junto con su extensión (ejemplo: 'archivo.csv') y 
# como segundo parámetro tendrá un string el cual será el contenido a guardar en dicho archivo. 
# Debe abrirse el archivo en modo escritura+, ya que en caso de no existir, lo creara y en caso 
# de existir, lo va a sobreescribir La función debera retornar True si no hubo errores, caso 
# contrario False, además en caso de éxito, deberá imprimir un mensaje respetando el formato:
# .Se creó el archivo: nombre_archivo.csv
# En caso de retornar False, el mensaje deberá decir: ‘Error al crear el archivo: nombre_archivo’
# Donde nombre_archivo será el nombre que recibirá el archivo a ser creado, conjuntamente con su 
# extensión.
def guardar_archivo(nombre_archivo:str,lista):
      flag = False
      with open(nombre_archivo,"w") as archivo:
            
            for personaje in lista:
                  mensaje = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}\n"
                  mensaje = mensaje.format(personaje["nombre"],
                                          personaje["identidad"],
                                          personaje["empresa"],
                                          personaje["altura"],
                                          personaje["peso"],
                                          personaje["genero"],
                                          personaje["color_ojos"],
                                          personaje["color_pelo"],
                                          personaje["fuerza"],
                                          personaje["inteligencia"])
                  archivo.write(mensaje)
            flag = True
      if(flag == True):
           return print("Se creo el archivo {0} correctamente".format(nombre_archivo))
      else:
           return print("Error al crear el archivo {0}".format(nombre_archivo))
#========================================================================================== 
# 1.6-Crear la función 'capitalizar_palabras' la cual recibirá por parámetro un string que puede 
# contener una o muchas palabras. La función deberá retornar dicho string en el cual todas y 
# cada una de las palabras que contenga, deberán estar capitalizadas (Primera letra en mayúscula).
def capitalizar_palabras(string:str):
     nuevo_string =""
     lista = re.split(" ",string)
     contador = 0
     for palabra in lista:
        if (contador == 0):
            nuevo_string = nuevo_string + palabra.capitalize()  
        elif(contador == len(lista)) :
            nuevo_string = nuevo_string + palabra.capitalize() 
        else:
             nuevo_string = nuevo_string + " "+palabra.capitalize()
        contador = contador + 1 
     return nuevo_string
#========================================================================================== 
# 1.7-Crear la función 'obtener_nombre_capitalizado' la cual recibirá por parámetro un diccionario 
# el cual representará a un héroe y devolverá un string el cual contenga su nombre formateado 
# de la siguiente manera:
# Nombre: Venom
# Reutilizar 'capitalizar_palabras'
def obtener_nombre_capitalizado(diccionario:dict):
      string_nombre = ""
      for key in diccionario.keys():
           if ( key == "nombre"):
                string_nombre = capitalizar_palabras(key) +": "+ capitalizar_palabras(diccionario[key])

      return string_nombre

#==========================================================================================
# 1.8-Crear la función 'obtener_nombre_y_dato' la cual recibirá por parámetro un diccionario el 
# cual representará a un héroe y una key (string) la cual representará la key del héroe a imprimir. 
# La función devolverá un string el cual contenga el nombre y dato (key) del héroe a imprimir. 
# El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.
# El string resultante debe estar formateado al estilo: (suponiendo que la key es fuerza)
# Nombre: Venom | Fuerza: 500
# Reutilizar 'obtener_nombre_capitalizado'
def obtener_nombre_y_dato(diccionario:dict,key_a_traer):
     string_nuevo =obtener_nombre_capitalizado(diccionario)
     for key in diccionario.keys():
          if(key == key_a_traer):
               string_nuevo = string_nuevo +" | "+key +": "+ diccionario[key]
     return string_nuevo

#==========================================================================================
# 2.1-Crear la función 'es_genero' la cual recibirá por parámetro un diccionario que 
# representará un héroe y un string el cual será usado para evaluar si el héroe coincide 
# con el género buscado (El string puede ser M, F o NB). retornará True en caso de que cumpla,
# False caso contrario.
def es_genero(diccionario:dict,genero):
     
     if(diccionario["genero"] == genero.upper()):
          return True
     else:
          return False
#==========================================================================================
# 2.2-Crear la función 'stark_guardar_heroe_genero' la cual recibira por parámetro la lista de héroes
# y un string el cual representará el género a evaluar (puede ser M o F). Deberá imprimir 
# solamente los héroes o heroínas que coincidan con el género pasado por parámetro y además, 
# deberá guardar dichos nombres en un archivo con extensión csv (cada nombre deberá ir separado 
# or una coma)

def stark_guardar_heroe_genero(lista_superheroes,genero):
     string_personajes =""
     flag = False
     contador = 0
     for personaje in lista_superheroes:
          
          if (es_genero(personaje,genero) == True):
               if(contador == 9):
                    string_personajes =   string_personajes +obtener_nombre_capitalizado(personaje)+",\n"
                    contador = 0
               else:
                    string_personajes =   string_personajes +obtener_nombre_capitalizado(personaje)+","
                    contador = contador + 1 
     with open("Lista_de_Genero_{0}.csv".format(genero),"w") as archivo:
        archivo.write("Listado de personajes con genero {0}\n".format(genero))
        archivo.write(string_personajes.replace("Nombre: ",""))
        print(string_personajes)
        flag = True
        if (flag == True):
             return print("Se creo el arrchivo Lista_de_Genero_{0}.csv correctamente".format(genero))
        else:
             return print("error al crear el archivo Lista_de_Genero_{0}.csv ".format(genero))

#==========================================================================================
# 2.3-Reutilizar las funciones 'es_genero', 'obtener_nombre_capitalizado', 'imprimir_dato' y 
# 'guardar_archivo'.
# En el caso de 'guardar_archivo', cuando se llame a esta función el nombre de archivo a 
# guardar deberá respetar el formato: heroes_M.csv, heroes_F.csv o heroes_NB según corresponda.
# La función retornará True si pudo guardar el archivo, False caso contrario.

#=====================================================================================================
# 3.1-Basandote en la función 'calcular_min', crear la función 'calcular_min_genero' la cual
# recibirá como parámetro extra un string que representa el género de la heroína/héroe a buscar.
# modificar un poco la lógica para que dentro no se traiga por defecto al primer héroe de la lista 
# sino que mediante un flag, se traiga el primer héroe que COINCIDA con el género pasado por parámetro.
# A partir de allí, podrá empezar a comparar entre héroes o heroínas que coincidan con el género pasado
# por parámetro. La función retornará el héroe o heroína que cumpla la condición de tener el mínimo
# (peso, altura u otro dato)
def calcular_min_genero(lista_personajes,key_a_calcular,genero):
     flag = True
     min = None
     dato_personaje =""
     genero = genero.upper()
     for personaje in lista_personajes:
          if (personaje["genero"] == genero and flag == True):
              min = float(personaje[key_a_calcular])
              dato_personaje = obtener_nombre_y_dato(personaje,key_a_calcular)
              flag = False
          else:
               if (personaje["genero"]== genero and float(min) > float(personaje[key_a_calcular])):
                   min = float(personaje[key_a_calcular])
                   dato_personaje = obtener_nombre_y_dato(personaje,key_a_calcular) 

     return dato_personaje
#=====================================================================================================
# 3.2-Basandote en la función 'calcular_max', crear la función 'calcular_max_genero' la cual 
# recibirá como parámetro extra un string que representará el género de la heroína/héroe a buscar. 
# modificar un poco la lógica para que dentro no se traiga por defecto al primer héroe de la lista 
# sino que mediante un flag, se traiga el primer héroe que COINCIDA con el género pasado por parámetro.
# A partir de allí, podrá empezar a comparar entre héroes o heroínas que coincidan con el género pasado 
# por parámetro. La función retornará el héroe o heroína que cumpla la condición de tener el máximo 
# (peso, altura u otro dato)
def calcular_max_genero(lista_personajes,key_a_calcular,genero):
     flag = True
     max = None
     dato_personaje =""
     genero = genero.upper()
     for personaje in lista_personajes:
          if (personaje["genero"] == genero and flag == True):
              max = float(personaje[key_a_calcular])
              dato_personaje = obtener_nombre_y_dato(personaje,key_a_calcular)
              flag = False
          else:
               if (personaje["genero"]== genero and float(max) < float(personaje[key_a_calcular])):
                   max = float(personaje[key_a_calcular])
                   dato_personaje = obtener_nombre_y_dato(personaje,key_a_calcular) 

     return dato_personaje
#=====================================================================================================
# 3.3-Basandote en la funcion 'calcular_max_min_dato', crear una funcion con la misma lógica la cual
# reciba un parámetro string que representará el género del héroe/heroína a buscar y renombrarla 
# a 'calcular_max_min_dato_genero'. La estructura será similar a la ya antes creada, 
# salvo que dentro de ella deberá llamar a 'calcular_max_genero' y 'calcular_min_genero',
# pasandoles el nuevo parámetro. Esta función retornará el héroe o heroína que cumpla con 
# las condiciones pasados por parámetro. Por ejemplo, si se le pasa 'F' y 'minimo', 
# retornará la heroína que tenga el mínimo (altura, peso u otro dato)
def calcular_max_min_dato_genero(lista_personajes,key_a_calcular,genero,valor_string):
        if(valor_string == "minimo"):
                   
            return calcular_min_genero(lista_personajes,key_a_calcular,genero)
            
        elif(valor_string == "maximo"):
           return calcular_max_genero(lista_personajes,key_a_calcular,genero)
            
        else :
              return -1  

#=====================================================================================================
# 3.4-Basandote en la función 'stark_calcular_imprimir_heroe' crear la función 
# ‘stark_calcular_imprimir_guardar_heroe_genero’ que además reciba un string el 
# cual representará el género a evaluar.  El formato de mensaje a imprimir deberá ser estilo:

# Mayor Altura: Nombre: Gamora | Altura: 183.65

# Además la función deberá guardar en un archivo csv el resultado obtenido.

# Reutilizar: 'calcular_max_min_dato_genero', 'obtener_nombre_y_dato', 'imprimir_dato' y
# 'guardar_archivo'. 

# En el caso de 'guardar_archivo' el nombre del archivo debe respetar el formato:

# heroes_calculo_key_genero.csv

# Donde:
# cálculo: representará el string máximo o mínimo
# key: representará cual es la key la cual se tiene que hacer el cálculo
# genero: representará el género a calcular.


# Ejemplo: para calcular el héroe más alto femenino, el archivo se deberá llamar:

# heroes_maximo_altura_F.csv

# Esta función retornará True si pudo guardar el archivo, False caso contrario

def stark_calcular_imprimir_guardar_heroe_genero(lista,calculo,key,genero):
     string = "{0} {1}: {2}".format(calculo,key,calcular_max_min_dato_genero(lista,key,genero,calculo))
     flag = False
     with open("heroes_{0}_{1}_{2}.csv".format(calculo,key,genero),"w") as archivo:
          archivo.write(string)
          flag = True
     return flag
#=====================================================================================================
# 4.1-Basandote en la función 'sumar_dato_heroe', crear la función llamada 'sumar_dato_heroe_genero'
# la cual deberá tener un parámetro extra del tipo string que representará el género con el que 
# se va a trabajar.

# Esta función antes de realizar la suma en su variable sumadora, deberá validar lo siguiente:

# El tipo de dato del héroe debe ser diccionario.
# El héroe actual de la iteración no debe estar vacío (ser diccionario vacío)
# El género del héroe debe coincidir con el pasado por parámetro.

# Una vez que cumpla con las condiciones, podrá realizar la suma. La función deberá retornar
# la suma del valor de la key de los héroes o heroínas que cumplan las condiciones o -1 en caso 
# de que no se cumplan las validaciones

def sumar_dato_heroe_genero(lista_personajes,key_A_sumar,genero):
     acumulador  = 0.00
     string = "El acumulador de {0} del genero {1} es de {2} :".format(key_A_sumar,genero,acumulador)
     for personaje in lista_personajes:
          if(personaje["genero"] == genero.upper()):
               acumulador = acumulador + float(personaje[key_A_sumar])
     string = "El acumulador de {0} del genero {1} es de {2} :".format(key_A_sumar,genero,acumulador)
     return  acumulador
     
#==================================================================================================
# 4.2- Crear la función 'cantidad_heroes_genero' la cual recibirá por parámetro la lista de héroes 
# y un string que representará el género a buscar. La función deberá iterar y sumar la cantidad 
# de héroes o heroínas que cumplan con la condición de género pasada por parámetro,
# retornará dicha suma.
def cantidad_heroes_genero(lista_personajes,genero):
     contador = 0
     for personaje in lista_personajes:
          if(personaje["genero"] == genero.upper()):
               contador = contador + 1
     return contador

#===================================================================================================
# 4.3-Basandote en la función 'calcular_promedio', crear la función 'calcular_promedio_genero' la 
# cual tendrá como parámetro extra un string que representará el género a buscar. la lógica es
# similar a la función anteriormente mencionada en el enunciado. Reutilizar las funciones:
# 'sumar_dato_heroe_genero', 'cantidad_heroes_genero' y 'dividir'.
# retornará el promedio obtenido, según la key y género pasado por parámetro.
def calcular_promedio_genero(lista_personajes,key_a_promediar,genero):
     cantidad = cantidad_heroes_genero(lista_personajes,genero)
     acumulador = sumar_dato_heroe_genero(lista_personajes,key_a_promediar,genero)

     promedio = acumulador / float(cantidad)
     string = "el promedio del genero {0} de la key {1} es de {2}".format(genero,key_a_promediar,promedio)
     return string
#===================================================================================================
# 4.4-Basandote en la función ‘stark_calcular_imprimir_promedio_altura', desarrollar la función 
# 'stark_calcular_imprimir_guardar_ promedio_altura_genero' la cual tendrá como parámetro 
# extra un string que representará el género de los héroes a buscar. 

# La función antes de hacer nada, deberá validar que la lista no esté vacía. 
# En caso de no estar vacía: calculará el promedio y lo imprimirá formateado al estilo:

# Altura promedio género F: 178.45

# En caso de estar vacía, imprimirá como mensaje: 

# Error: Lista de héroes vacía. 

# Luego de imprimir la función deberá guardar en un archivo los mismos datos. 
# El nombre del archivo debe tener el siguiente formato:

# 		heroes_promedio_altura_genero.csv

# 		Donde:
# genero: será el género de los héroes a calcular, siendo M y F únicas opciones posibles.

# Ejemplos:
# 	heroes_promedio_altura_F.csv
# 	heroes_promedio_altura_M.csv

# Reutilizar las funciones: 'calcular_promedio_genero', 'imprimir_dato' y 'guardar_archivo'.
# Esta función retornará True si pudo la lista tiene algún elemento y pudo guardar el archivo,
# False en caso de que esté vacía o no haya podido guardar el archivo.
def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes,key,genero):
      flag = False
      if ( len(lista_personajes)> 0):
          with open("heroes_promedio_{0}_{1}.csv".format(key,genero),"w") as archivito:
              archivito.write(calcular_promedio_genero(lista_personajes,key,genero))
              flag = True
     
      print(calcular_promedio_genero(lista_personajes,key,genero))
      return flag

#===================================================================================================
# 5.1-Crear la función 'calcular_cantidad_tipo' la cual recibirá por parámetro la lista de héroes 
# y un string que representará el tipo de dato/key a buscar (color_ojos, color_pelo, etc) 
# Antes de hacer nada, deberá validar que la lista no esté vacía. En caso de estarlo devolver 
# un diccionario con la siguiente estructura:
# {
#     "Error": “La lista se encuentra vacía”
# }
# La función deberá retornar un diccionario con los distintos valores del tipo de dato 
# pasada por parámetro y la cantidad de cada uno (crear un diccionario clave valor).
# Por ejemplo, si el tipo de dato fuese color_ojos, devolverá un diccionario de la siguiente manera:
# {
#     "Celeste": 4,
#     "Verde": 8,
#     "Marron": 6
# }
# Reutilizar la función 'capitalizar_palabras' para capitalizar los valores de las keys.
def calcular_cantidad_tipo(lista_personajes,key):
     diccionario = {}
     flag = None
     if ( len(lista_personajes) > 0):
          flag = True
          for personaje in lista_personajes:
                clave = capitalizar_palabras(personaje[key])
                if (clave  in diccionario):
                   diccionario[clave]= diccionario[clave] + 1
                else:
                   diccionario[clave] = 1
     else:
          flag = False
     
          
               
     return diccionario

#===================================================================================================
# 5.2-Crear la función 'guardar_cantidad_heroes_tipo' la cual recibirá como parámetro un 
# diccionario que representará las distintas variedades del tipo de dato (distintos colores de ojos,
#  pelo, etc) como clave con sus respectivas cantidades como valor. Como segundo parámetro recibirá 
# el dato (color_pelo, color_ojos, etc) el cual tendrás que usarlo únicamente en el mensaje final 
# formateado. Esta función deberá iterar cada key del diccionario y variabilizar dicha key con su 
# valor para luego formatearlos en un mensaje el cual deberá guardar en archivo.
# Por ejemplo: 
# "Caracteristica: color_ojos Blue - Cantidad de heroes: 9"

# Reutilizar la función 'guardar_archivo'. El nombre del archivo final deberá respetar el formato:

# heroes_cantidad_tipoDato.csv

# Donde:

# tipoDato: representará el nombre de la key la cual se está evaluando la cantidad de héroes.

# Ejemplo:
# heroes_cantidad_color_pelo.csv
# heroes_cantidad_color_ojos.csv

# La función retornará True si salió todo bien, False caso contrario.
def guardar_cantidad_heroes_tipo(diccionario:dict,dato:str ):
     flag = False
     with open("Heroes_cantidad_{0}.csv".format(dato),"w") as archivo:
          for datos in diccionario:

               clave = datos
               texto ="Caracteristica: {0} {1} - Cantidad de heroes: {2}\n".format(dato,clave,diccionario[datos])
               archivo.write(texto)
          flat = True
     return flag

#===================================================================================================
# 5.3-Crear la función 'stark_calcular_cantidad_por_tipo' la cual recibirá por parámetro la lista de 
# héroes y un string que representará el tipo de dato/key a buscar (color_ojos, color_pelo, etc).
# Dentro deberás reutilizar 'calcular_cantidad_tipo' y 'guardar_cantidad_heroes_tipo' con la lógica 
# que cada una de esas funciones manejan.
# Esta función retornará True si pudo guardar el archivo, False caso contrario.

def stark_calcular_cantidad_por_tipo(lista:list,key:str):
     if (guardar_cantidad_heroes_tipo(calcular_cantidad_tipo(lista,key),key)== True):
          flag = True
     else:
          flag = False
     return flag

#===================================================================================================
# Sexta Parte
#===================================================================================================
# 6.1-Crear la función 'obtener_lista_de_tipos' la cual recibirá por parámetro la lista de héroes 
# y un string que representará el tipo de dato/key a buscar (color_ojos, color_pelo, etc).
# Esta función deberá iterar la lista de héroes guardando en una lista las variedades del tipo
# de dato pasado por parámetro (sus valores).
# En caso de encontrar una key sin valor (o string vacío), deberás hardcodear con el valor 'N/A'
# y luego agregarlo a la lista donde irás guardando todos los valores encontrados, si el valor del 
# héroe no tiene errores, guardarlo tal cual viene.
# Finalmente deberás eliminar los duplicados de esa lista y retornarla como un set.
# Reutilizar 'capitalizar_palabras' para guardar cada uno de los datos con la primera letra mayúscula.
def obtener_lista_de_tipos(lista:list,key:str):
     lista_de_tipos = []
     for personaje in lista:
          clave = capitalizar_palabras(personaje[key])
          if (clave in lista_de_tipos):
               pass
          else :
               if(personaje[key] == ""):
                    lista_de_tipos.append("N/A")
               else:
                    lista_de_tipos.append(clave)
     return lista_de_tipos
     pass

#===================================================================================================
#6.2- Crear la función 'normalizar_dato' la cual recibirá por parámetro un dato de héroe 
# (el valor de una de sus keys, por ejemplo si la key fuese color_ojos y su valor fuese Verde, 
#  recibira este ultimo) y tambien una variable como string la cual representará el valor por
# defecto a colocar en caso de que el valor está vacío. Deberá validar que el dato no esté vacío,
# en caso de estarlo lo reemplazará con el valor default pasado por parámetro y lo retornará, 
# caso contrario lo retornará sin modificaciones.
def normalizar_dato(dato:str,valor_defecto:str):
    if (dato ==""):
          dato = valor_defecto
          return dato
    else:
          return dato
#===================================================================================================
# 6.3-Crear la función 'normalizar_heroe' la cual recibirá dos parámetros. el primero será un 
# diccionario que representará un solo héroe, el segundo parámetro será el nombre de la key 
# de dicho diccionario la cual debe ser normalizada. 
# La función deberá capitalizar las palabras que tenga dicha key como valor, luego deberá normalizar
# el dato (ya que si viene vacío, habrá que setearlo con N/A). 
# Finalmente deberá capitalizar todas las palabras del nombre del héroe y deberá retornar al Heroe con
# cada palabra de su nombre capitalizados, cada palabra del valor de la key capitalizadas y 
# normalizadas (con N/A en caso de que estuviesen vacías por defecto).
# Reutilizar: 'capitalizar_palabras' y 'normalizar_dato'
def normalizar_heroe(diccionario:dict,dato_a_normalizar):

     if(diccionario[dato_a_normalizar] == ""):
        diccionario[dato_a_normalizar] = "N/A" 
     else:
          diccionario[dato_a_normalizar] = capitalizar_palabras(diccionario[dato_a_normalizar])

     return diccionario
     pass
#===================================================================================================
# 6.4-Crear la funcion 'obtener_heroes_por_tipo' el cual recibira por parámetro:

# La lista de héroes
# Un set de tipos/variedades (colores de ojos, de pelo, etc)
# El tipo de dato a evaluar (la key en cuestion, color_ojos, color_pelo, etc)

# PRESTAR ATENCIÓN:

# Deberá iterar el set de tipos/variedades y por cada tipo tendrá evaluar si ese tipo existe 
# como key en un diccionario el cual deberás armar. (contendrá cada variedad como key y una lista 
# 						   de nombres de héroes como valor de cada una de ellas).

# En caso de no existir dicha key en el diccionario, agregarla con una lista vacía como valor.

# Dentro de la iteración de variedades, iterar la lista de héroes (for anidado) 'normalizando' 
# el posible valor que tenga la key evaluada, ya que podría venir vacía (qué función usarias aca? 
# guiño guiño)

# Una vez normalizado el dato, evaluar si dicho dato coincide con el tipo pasado por parámetro.

# En caso de que coincida, agregarlo a la lista (inicialmente vacía) de la variedad iterada en el 
# primer bucle.
# Esta función retornará un diccionario con cada variedad como key y una lista de nombres como valor.

# Por ejemplo:
# {
#     "Celestes": ["Capitan America", "Tony Stark"],
#     "Verdes": ["Hulk", "Viuda Negra"]
#     ....
# }
def obtener_heroes_por_tipo(lista,tipo_valor,key):
     dic = {}

     for personaje in lista:
          for tipo in tipo_valor:
             if(personaje[key] == tipo):
                    if (tipo in dic):
                         dic[tipo].append(personaje["nombre"])
                    else:
                         dic[tipo] = []
                         dic[tipo].append(personaje["nombre"])
          
     return dic
#===================================================================================================
# 6.5-Crear la funcion 'guardar_heroes_por_tipo' la cual recibira por parámetro un diccionario 
# que representará los distintos tipos como clave y una lista de nombres como valor 
# (Lo retorna la función anterior) y además como segundo parámetro tendrá un string el 
# cual representará el tipo de dato a evaluar (color_pelo, color_ojos, etc).
# Deberá recorrer cada key y cada valor (lista) que esta contenga para finalmente crear 
# un string el cual será un mensaje que deberás imprimir formateado.
# Por ejemplo:
# "color_ojos Green: Black Widow | Hulk"

# Reutilizar la función 'guardar_archivo'. El archivo final deberá respetar el formato:
# heroes_segun_TipoDato.csv

# Donde:
# TipoDato: es la key la cual indicará qué cosas se deben guardar en el archivo.

# Ejemplo:
# 		heroes_segun_color_pelo.csv (Agrupados por color de pelo)
# 		heroes_segun_color_ojos.csv (Agrupados por color de ojos)

# Esta función retorna True si salió todo bien, False caso contrario.
def guardar_heroes_por_tipo(diccionario:dict,tipo_de_datos):
     
     with open("heroes_segun_{0}.csv".format(tipo_de_datos),"w") as archivo:
          contador = 0 
          texto ="{0}".format(tipo_de_datos)
          flag = False
          for dato in diccionario:
               print(dato)
               texto = texto +"\n"+ dato +": "
               for nombre in diccionario[dato]:
                     print(nombre)
                     if(contador == 0):
                          texto = "{0}: {1} ".format(dato,nombre)
                          contador = 1
                     else:
                          texto = texto + nombre +"| "
          archivo.write(texto)
          flag = True
          return flag 
#===================================================================================================
# 6.6-Crear la función 'stark_listar_heroes_por_dato' la cual recibirá por parámetro la lista de 
# héroes y un string que representará el tipo de dato a evaluar (color_pelo, color_ojos, etc). 
# Dentro deberás reutilizar las funciones:

# 'obtener_lista_de_tipos'
# 'obtener_heroes_por_tipo'
# 'guardar_heroes_por_tipo'

# Pasando por parámetro lo que corresponda según la lógica de las funciones usadas.

# Esta función retornará True si pudo guardar el archivo, False caso contrario.
def stark_listar_heroes_por_dato(lista,tipo):

     return guardar_heroes_por_tipo(obtener_heroes_por_tipo(lista,obtener_lista_de_tipos(lista,tipo),tipo),tipo)
    