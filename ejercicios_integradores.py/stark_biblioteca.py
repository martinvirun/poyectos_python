
from data_stark import lista_personajes


#=========================================================================================
def imprimir_dato(texto_a_colocar,dato):
      '''
      imprime un dato por consola
      recibe como parametro un texto y un dato 
      no tiene retorno
      '''
      print(texto_a_colocar,dato)
#=========================================================================================
def obtener_nombre(dic_heroes):
        '''
        obtiene un nombre de un diccionario
        recibe como parametro un diccionario 
        retorna el nombre en el diccionario 
        '''
        return dic_heroes["nombre"]
#=========================================================================================
def stark_imprimir_nombres_heroes(lista_personajes):
        '''
        imprime todos los nombres en una lista 
        recibe como parametro una lista
        no retorna nada 
        '''
        for nombre in lista_personajes:
                imprimir_dato("el nombre es :",obtener_nombre(nombre))
# stark_imprimir_nombres_heroes(lista_personajes)
#=========================================================================================
def obtener_nombre_y_dato(dic_heroes,dato_a_obtener):
        '''
        obtiene un nombre y un dato 
        recibe como parametro un diccionario y un dato a obtener de el 
        no retorna nada 
        '''
        for datos in dic_heroes:
                if (datos == dato_a_obtener):
                      imprimir_dato("el nombre es ",dic_heroes["nombre"])
                      imprimir_dato("la altura es ",dic_heroes[dato_a_obtener])
#=========================================================================================
def stark_imprimir_nombres_alturas(lista_personajes):
        '''
        imprime  nombnre y altura de una lista 
        recibe una lista como parametro
        si la lista esta vacia retorna 0 sino imprime nombre y altura 
        '''
           
        if(len(lista_personajes) <1 ):
            return 0
        else:
            for dic_heroes in lista_personajes:
                obtener_nombre_y_dato(dic_heroes,"altura")
#=========================================================================================
def calcular_max(lista_personajes,key_a_calcular):
       '''
       calcula el maximo de un key a eleccion
       recibe como parametro una lista y el key al que se le quiere buscar el mayot 
       retorna el dato mas alto y su nombre 
       '''
       flag = True
       dato_mas_alto = None 
       nombre_dato_mas_alto = None
       
       for dato in lista_personajes:
              if(flag == True):
                   nombre_dato_mas_alto = dato["nombre"]
                   dato_mas_alto= float(dato[key_a_calcular])
                   flag=False
              else:
                     if(float(dato_mas_alto ) < float(dato[key_a_calcular])):
                          dato_mas_alto= float(dato[key_a_calcular])  
                          nombre_dato_mas_alto = dato["nombre"]
       return  nombre_dato_mas_alto        
#=========================================================================================
def calcular_min(lista_personajes,key_a_calcular):
       '''
       calcula el minimo de un key a eleccion
       recibe como parametro una lista y el key al que se le quiere buscar el menor 
       retorna el dato menor  y su nombre 
       '''
       flag = True
       dato_mas_bajo = None 
       nombre_dato_mas_bajo = None
       
       for dato in lista_personajes:
              if(flag == True):
                   nombre_dato_mas_bajo = dato["nombre"]
                   dato_mas_bajo= float(dato[key_a_calcular])
                   flag=False
              else:
                     if(float(dato_mas_bajo ) > float(dato[key_a_calcular])):
                          dato_mas_bajo= float(dato[key_a_calcular])  
                          nombre_dato_mas_bajo = dato["nombre"]
       return  nombre_dato_mas_bajo   
#=========================================================================================    
def calcular_max_min_dato(lista_heroes,valor_string:str,key_a_calcular:str):
      '''
      calcula el minimo y maximo utilizando otras dos funciones 
      toma como parametro lista , si se busca minimo o maximo , y de cual key se busca el mismo
      '''
      if(valor_string == "minimo"):
                   
            return calcular_min(lista_personajes,key_a_calcular)
            
      elif(valor_string == "maximo"):
           return calcular_max(lista_personajes,key_a_calcular)
            
      else :
            return -1     
#=========================================================================================    
def stark_calcular_imprimir_heroe(lista_heroes,caluculo_a_Realizar,key_a_calcular):
      '''
      verifica si la lista contiene algo , si es asi , imprime nombre calcula con otras dos funciones
      el minimo o maximo , segun lo que se quiera buscar
      recibe como parametro lista , que se caluclara (minimo o maximo) y de cual key se quiere buscar 
      el mismo
      si la lista esta vacia retorna -1 
      '''
      if(len(lista_heroes)==0):
            return -1
      else:
            imprimir_dato("el nombre :",calcular_max_min_dato(lista_heroes,caluculo_a_Realizar,key_a_calcular))
            for nombre in lista_heroes:
             if (nombre["nombre"] == calcular_max_min_dato(lista_heroes,caluculo_a_Realizar,key_a_calcular) ):
                imprimir_dato(key_a_calcular,nombre[key_a_calcular])
      pass      
#=========================================================================================   
def sumar_dato_heroe(lista_personajes,key_A_sumar):
      '''
      suma datos de un key a eleccion
      recibe como parametro una lista y el key de lo que se quiere sumar 
      retorna la suma 
      '''
      suma = 0.00
      for superheroe in lista_personajes:
            if(isinstance(superheroe,dict)):
                  suma = suma + float(superheroe[key_A_sumar])
            else :
                  return -1    
      return suma  
#==========================================================================================   
def dividir(dividendo,divisor):
      '''
      hace una division 
      recibe como parametro dividendo y divisor y si el divisor no es 0 hace la cuenta
      retorna 0 si el divisor es 0, sino retorna resultado

      '''
      if (divisor == 0 ):
            return 0 
      else : 
            resultador = dividendo / divisor
            return resultador
     
#==========================================================================================   
def calcular_promedio(lista_heroes,key_a_promediar):
      '''
      calcula el promedio 
      recibe como parametro la lista a promediar y el key de lo que se quiere promediar 
      utiliza otras funciones para resolver el problema
      retorna el promedio 
      
      '''
      suma = sumar_dato_heroe(lista_heroes,key_a_promediar)
      promedio = dividir(suma,len(lista_heroes))
      return promedio
#==========================================================================================    
def stark_calcular_imprimir_promedio_altura(lista_heroes):
      '''
      calcula el promedio de altura utilizando la funcion calcular promedio si es quela lista tiene algo
      recibe la lista de la que se quiere hacer el promedio
      retorna 0 si la lista esta vacia , sino imprime el promedio de altura 
      '''
      if(len(lista_heroes)>0):
            return imprimir_dato("la altura promedio es :",calcular_promedio(lista_heroes,"altura"))
      else:
            return 0     
#==========================================================================================
def imprimir_menu():
        '''
        imprime un menu
        no tiene parametro
        no retorna nada 
        
        '''
        imprimir_dato("Menú de opciones:","")
        imprimir_dato("1. Mostrar los nombres de todos los superheroes ","")
        imprimir_dato("2. Mostrar nombre del superheroe con su altura","")
        imprimir_dato("3. Mostrar superheroe mas alto","")
        imprimir_dato("4. Mostrar superheroe mas bajo","")
        imprimir_dato("5. Mostrar altura promedio de los superheroes ","")
        imprimir_dato("6. Mostrar identidad mas bajo y mas alto ","")
        imprimir_dato("7. Mostrar superheroe mas y menos pesado ","")
        imprimir_dato("0. Salir del programa","")
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
def stark_menu_principal():
      '''
      imprime el menu principal y le pide al usuario una opcion y la valida con la funcion de 
      validacion de enteros
      no tiene parametros
      retnorna la opcion casteada a entero si es posible , sino retorna -1
      '''
      imprimir_menu()
      opcion = input("\nIngrese la opción deseada: ")
      if ( validar_entero(opcion) == True):
            return  int(opcion)
      else:
            return -1
#==========================================================================================
def stark_marvel_app(lista_heroes,opcion):
      '''
      tiene las opcines con sus respectivas funciones dentro de los if
      recibe una lista como párametro y la opcion a ejecutar
      retorna la accion de la opcion que se a elegido 
      '''
      
      if (opcion == 1 ):
            return stark_imprimir_nombres_heroes(lista_personajes)
            
      elif(opcion == 2):
            return stark_imprimir_nombres_alturas(lista_personajes)
            
      elif(opcion == 3):
            return stark_calcular_imprimir_heroe(lista_personajes,"maximo","altura")
            
      elif(opcion == 4):
            return stark_calcular_imprimir_heroe(lista_personajes,"minimo","altura")
           
      elif(opcion == 5):
            return imprimir_dato("la altura promedio es :",calcular_promedio(lista_personajes,"altura"))
            
      elif(opcion == 6):
            for nombre in lista_personajes:
                  if (nombre["nombre"]== calcular_max_min_dato(lista_personajes,"minimo","altura")):
                        print("la identidad del mas bajo es :{0}".format(nombre["identidad"]))
                        break
            for nombre in lista_personajes:
                  if (nombre["nombre"]== calcular_max_min_dato(lista_personajes,"maximo","altura")):
                        print("la identidad del mas alto  es :{0}".format(nombre["identidad"]))
                        break
                  break

      elif(opcion == 7):
           for nombre in lista_personajes:
                  if (nombre["nombre"]== calcular_max_min_dato(lista_personajes,"maximo","peso")):
                        print("la identidad del mas pesado es :{0}".format(nombre["identidad"]))
                        break
           for nombre in lista_personajes:
                  if (nombre["nombre"]== calcular_max_min_dato(lista_personajes,"minimo","peso")):
                        print("la identidad del menos pesado  es :{0}".format(nombre["identidad"]))
                        break
                  
            
      elif(opcion == 0):
          return 0
      else:
            print("Opcion ingresada es invalida") 
#==========================================================================================
def validar_entero_isdigit(string):
      '''
      valida si un string esta compuesto por enteros usando isdigit()
      recibe un str como parametro
      retorna true si todo el str esta compuesto por numero, y false si no es asi 
      '''
      flag = None
      for letra in string:
            if (letra.isdigit() == True):
                  flag= True
            else :
                  flag = False
      return flag
#==========================================================================================