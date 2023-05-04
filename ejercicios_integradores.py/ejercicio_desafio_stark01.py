# Desafío #01:
# Agregar al código elaborado para cumplir el desafío #01 los siguientes puntos, -
# utilizando un menú que permita acceder a cada uno de los puntos por separado.-
# Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M-
# Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F-
# Recorrer la lista y determinar cuál es el superhéroe más alto de género M -
# Recorrer la lista y determinar cuál es el superhéroe más alto de género F -
# Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M -
# Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F -
# Recorrer la lista y determinar la altura promedio de los  superhéroes de género M-
# Recorrer la lista y determinar la altura promedio de los  superhéroes de género F-
# Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores 
# (ítems C a F)-
# Determinar cuántos superhéroes tienen cada tipo de color de ojos.-
# Determinar cuántos superhéroes tienen cada tipo de color de pelo.-
# Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener,
#  Inicializarlo con ‘No Tiene’). -
# Listar todos los superhéroes agrupados por color de ojos.
# Listar todos los superhéroes agrupados por color de pelo.
# Listar todos los superhéroes agrupados por tipo de inteligencia
'''
"nombre": "Howard the Duck",
   "identidad": "Howard (Last name unrevealed)",
   "empresa": "Marvel Comics",
   "altura": "79.349999999999994",
   "peso": "18.449999999999999",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Yellow",
   "fuerza": "2",
   "inteligencia": "average"
'''
from data_stark import lista_personajes
def mostrar_nombre_superheroe_masculino(lista_personajes):
    for nombre in lista_personajes:
        if (nombre["genero"] == "M"):
            print(nombre["nombre"])
#===============================================================================================
def mostrar_nombre_superheroe_femenino(lista_personajes):
        for nombre in lista_personajes:
            if (nombre["genero"] == "F"):
             print(nombre["nombre"])

#===============================================================================================
def mostrar_nombre_superheroe_mas_alto_masculino(lista_personajes):
 contador = True
 superheroe_masculino_mas_alto = None
 for personaje in lista_personajes:
   if (personaje["genero"] == "M" and contador == True ):
        superheroe_masculino_mas_alto = personaje["nombre"]
        altura_mas_alto = float(personaje["altura"])
        contador = False
   elif(personaje["genero"] == "M" and contador  == False):
       if(float(altura_mas_alto) < float(personaje["altura"])):
          superheroe_masculino_mas_alto = personaje["nombre"] 
          altura_mas_alto = float(personaje["altura"]) 
 return superheroe_masculino_mas_alto

#===============================================================================================
def mostrar_nombre_superheroe_mas_alto_femenino(lista_personajes):
 contador = True
 superheroe_femenino_mas_alto = None
 for personaje in lista_personajes:
   if (personaje["genero"] == "F" and contador == True ):
        superheroe_femenino_mas_alto = personaje["nombre"]
        altura_mas_alto = float(personaje["altura"])
        contador = False
   elif(personaje["genero"] == "F" and contador  == False):
       if(float(altura_mas_alto) < float(personaje["altura"])):
          superheroe_femenino_mas_alto = personaje["nombre"] 
          altura_mas_alto = float(personaje["altura"]) 
 return superheroe_femenino_mas_alto



#===============================================================================================

def mostrar_nombre_superheroe_mas_bajo_masculino(lista_personajes):
 contador = True
 superheroe_masculino_mas_bajo = None
 for personaje in lista_personajes:
   if (personaje["genero"] == "M" and contador == True ):
        superheroe_masculino_mas_bajo = personaje["nombre"]
        altura_mas_bajo = float(personaje["altura"])
        contador = False
   elif(personaje["genero"] == "M" and contador  == False):
       if(float(altura_mas_bajo) > float(personaje["altura"])):
          superheroe_masculino_mas_bajo = personaje["nombre"] 
          altura_mas_bajo = float(personaje["altura"]) 
 return superheroe_masculino_mas_bajo

#===============================================================================================
def mostrar_nombre_superheroe_mas_bajo_femenino(lista_personajes):
 contador = True
 superheroe_femenino_mas_bajo = None
 for personaje in lista_personajes:
   if (personaje["genero"] == "F" and contador == True ):
        superheroe_femenino_mas_bajo = personaje["nombre"]
        altura_mas_bajo = float(personaje["altura"])
        contador = False
   elif(personaje["genero"] == "F" and contador  == False):
       if(float(altura_mas_bajo) > float(personaje["altura"])):
          superheroe_femenino_mas_bajo = personaje["nombre"] 
          altura_mas_bajo = float(personaje["altura"]) 
 return superheroe_femenino_mas_bajo



#===============================================================================================
def mostrar_altura_promedio_superheroe_masculino(lista_personajes):
 acumulador = 0
 contador  = 0
 
 for personaje in lista_personajes:
   if (personaje["genero"] == "M"):
       acumulador = acumulador + float(personaje["altura"])
       contador = contador + 1
 promedio = acumulador/ contador 
 return promedio
#===============================================================================================
def mostrar_altura_promedio_superheroe_femenino(lista_personajes):
 acumulador = 0
 contador  = 0
 
 for personaje in lista_personajes:
   if (personaje["genero"] == "F"):
       acumulador = acumulador + float(personaje["altura"])
       contador = contador + 1
 promedio = acumulador/ contador 
 return promedio
#===============================================================================================
def mostrar_superheroes_por_color_de_ojos(lista_personajes):
    dic_color_ojos = {}
    for personaje in lista_personajes:
        
        if(personaje["color_ojos"] in dic_color_ojos ):
            dic_color_ojos[personaje["color_ojos"]] = dic_color_ojos[personaje["color_ojos"]] +1 
        else:
            dic_color_ojos[personaje["color_ojos"]] = 1
       
    return dic_color_ojos


#===============================================================================================       

def mostrar_superheroes_por_color_de_pelo(lista_personajes):
    dic_color_pelo = {}
    for personaje in lista_personajes:
        
        if(personaje["color_pelo"] in dic_color_pelo ):
            dic_color_pelo[personaje["color_pelo"]] = dic_color_pelo[personaje["color_pelo"]] +1 
        else:
            dic_color_pelo[personaje["color_pelo"]] = 1
       
    return dic_color_pelo


#======================================================================================================
def mostrar_superheroes_por_inteligencia(lista_personajes):
    dic_inteligencia = {}
    for personaje in lista_personajes:
        
        if(personaje["inteligencia"] in dic_inteligencia ):
            dic_inteligencia[personaje["inteligencia"]] = dic_inteligencia[personaje["inteligencia"]] +1 
        else:
            dic_inteligencia[personaje["inteligencia"]] = 1
       
    return dic_inteligencia


#======================================================================================================
def agrupar_superheroes_por_color_de_ojos(lista_personajes):
    dic_color_ojos = {}
    # lista_color_ojos = []
    # for personaje in lista_personajes:
    #     if (personaje["color_ojos"] in lista_color_ojos):
    #         pass
    #     else:
    #         lista_color_ojos.append(personaje["color_ojos"])
    # print(lista_color_ojos)
    for personaje in lista_personajes:
        color_ojos = personaje["color_ojos"]
        nombre = personaje["nombre"]
        
        if(color_ojos in dic_color_ojos ):
          
          dic_color_ojos[color_ojos].append(nombre)
         
        else:
          aux_lista = []
          aux_lista.append(nombre)
          dic_color_ojos[color_ojos] = aux_lista
    return dic_color_ojos 
   
#======================================================================================================
def agrupar_superheroes_por_color_de_pelo(lista_personajes):
    dic_color_pelo = {}
    
    for personaje in lista_personajes:
        color_pelo = personaje["color_pelo"]
        nombre = personaje["nombre"]
        
        if(color_pelo in dic_color_pelo ):
          
          dic_color_pelo[color_pelo].append(nombre)
         
        else:
          aux_lista = []
          aux_lista.append(nombre)
          dic_color_pelo[color_pelo] = aux_lista
    return dic_color_pelo 
  
#=============================================================================================== 
def agrupar_superheroes_por_inteligencia(lista_personajes):
    dic_inteligencia= {}
    
    for personaje in lista_personajes:
        inteligencia = personaje["inteligencia"]
        nombre = personaje["nombre"]
        
        if(inteligencia in dic_inteligencia ):
          
          dic_inteligencia[inteligencia].append(nombre)
         
        else:
          aux_lista = []
          aux_lista.append(nombre)
          dic_inteligencia[inteligencia] = aux_lista
    return dic_inteligencia 
  
#=============================================================================================== 
def main():

    while True:
        print("Menú de opciones:")
        print("1. Mostrar los nombres de cada superhéroe de género M ")
        print("2. Mostrar nombre de cada superhéroe de género F")
        print("3. Mostrar superhéroe más alto de género M ")
        print("4. Mostrar cuál es el superhéroe más alto de género F ")
        print("5. Mostrar cuál es el superhéroe más bajo  de género M ")
        print("6. Mostrar cuál es el superhéroe más bajo  de género F ")
        print("7. Mostrar la altura promedio de los  superhéroes de género M ")
        print("8. Mostrar la altura promedio de los  superhéroes de género F")
        print("9. Recorrer la lista y determinar cuál es el superhéroe más alto de género M y más bajo  de género F")
        print("10. Mostrar cuántos superhéroes tienen cada tipo de color de ojos.")
        print("11. Mostrar cuántos superhéroes tienen cada tipo de color de pelo.")
        print("12. Mostrar cuántos superhéroes tienen cada tipo de inteligencia")
        print("13. Listar todos los superhéroes agrupados por color de ojos.")
        print("14. Listar todos los superhéroes agrupados por color de pelo.")
        print("15. Listar todos los superhéroes agrupados por tipo de inteligencia")
        print("0. Salir del programa")
        opcion = input("\nIngrese la opción deseada: ")
        opcion_int= int(opcion)
        if (opcion_int== 1 ):
          mostrar_nombre_superheroe_masculino(lista_personajes)
          pass
            
        elif(opcion_int ==2):
             mostrar_nombre_superheroe_femenino(lista_personajes)
             pass
            
        elif(opcion_int == 3):
           print(mostrar_nombre_superheroe_mas_alto_masculino(lista_personajes)) 
            
           
        elif(opcion_int == 4):
            print(mostrar_nombre_superheroe_mas_alto_femenino(lista_personajes))
            pass
        elif(opcion_int == 5):
            print(mostrar_nombre_superheroe_mas_bajo_masculino(lista_personajes))
            
            pass
        elif(opcion_int == 6):
            print(mostrar_nombre_superheroe_mas_bajo_femenino(lista_personajes))
            
            pass
        elif(opcion_int == 7):
            print( mostrar_altura_promedio_superheroe_masculino(lista_personajes))
            
            pass
        elif(opcion_int == 8):
             print(mostrar_altura_promedio_superheroe_femenino(lista_personajes))
             pass
        elif(opcion_int == 9):
             print("mas alto masculino :{0}".format(mostrar_nombre_superheroe_mas_alto_masculino(lista_personajes)))
             print("mas bajo femenino :{0}".format(mostrar_nombre_superheroe_mas_bajo_femenino(lista_personajes)))
             pass
        elif(opcion_int == 10):
             print(mostrar_superheroes_por_color_de_ojos(lista_personajes))
             pass
        elif(opcion_int == 11):
              print(mostrar_superheroes_por_color_de_pelo(lista_personajes))
             
        elif(opcion_int == 12):
             print(mostrar_superheroes_por_inteligencia(lista_personajes))
             pass
        elif(opcion_int == 13):
             print(agrupar_superheroes_por_color_de_ojos(lista_personajes))
             pass
        elif(opcion_int == 14):
              print(agrupar_superheroes_por_color_de_pelo(lista_personajes))
             
        elif(opcion_int == 15):
             print(agrupar_superheroes_por_inteligencia(lista_personajes))
             
        elif(opcion_int == 0):
            break
        else:
            print("Opcion ingresada es invalida")
            
#======================================================================================================================================
main()