# Industrias Stark es principalmente una empresa de defensa que desarrolla y 
# fabrica armas avanzadas y tecnologías militares.

# Recientemente ha decidido ampliar su departamento de IT y para acceder a las 
# entrevistas es necesario completar el siguiente desafío, el cual estará dividido en etapas. Cada semana recibiremos un nuevo pedido de parte de la empresa.



# La empresa compartió con todos los participantes cierta información confidencial 
# de un grupo de superhéroes.  Y semana a semana enviará una lista con los nuevos requerimientos.
# Quien supere todas las etapas accedera a una entrevista con el director para  de la compañía.

# Set de datos

# La información a ser analizada se encuentra en el archivo data_stark.py,
# por tratarse de una lista, bastará con incluir dicho archivo en el proyecto 
# de la siguiente manera:

# from data_stark import lista_personajes

# Formato de los datos recibidos

# lista_heroes =
# [
#  {
#    "nombre": "Howard the Duck",
#    "identidad": "Howard (Last name unrevealed)",
#    "empresa": "Marvel Comics",
#    "altura": "79.349999999999994",
#    "peso": "18.449999999999999",
#    "genero": "M",
#    "color_ojos": "Brown",
#    "color_pelo": "Yellow",
#    "fuerza": "2",
#    "inteligencia": "average"
#  },
#  {
#    "nombre": "Rocket Raccoon",
#    "identidad": "Rocket Raccoon",
#    "empresa": "Marvel Comics",
#    "altura": "122.77",
#    "peso": "25.73",
#    "genero": "M",
#    "color_ojos": "Brown",
#    "color_pelo": "Brown",
#    "fuerza": "5",
#    "inteligencia": "average"
#  }
# ]




# Desafío #00:

# Analizar detenidamente el set de datos
# Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
# Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
# Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
# Calcular e informar cual es el superhéroe más y menos pesado.
# Ordenar el código implementando una función para cada uno de los valores informados.
# Construir un menú que permita elegir qué dato obtener
# Mostrar color de ojos de cada superheroe con su dentidad 
from data_stark import lista_personajes


def mostrar_nombre_todos_los_superheroes():
    for nombre in lista_personajes:
      print("el nombre es :{0}".format(nombre["nombre"]))
#======================================================================================================================================
def mostrar_nombre_y_altura_superheroes():
    for nombre in lista_personajes:
      print("el nombre es :{0}u su altura es :{1}".format(nombre["nombre"],nombre["altura"]))
#======================================================================================================================================
def mostrar_superheroe_mas_alto():
    for ind in range(len(lista_personajes)):
        if (ind == 0 ):
            mas_alto = float(lista_personajes[ind]["altura"])
            index = ind
        else: 
            if(float(mas_alto)< (float(lista_personajes[ind]["altura"]))):
              mas_alto = float(lista_personajes[ind]["altura"])
              index = ind
    print("el superheroe mas alto es :{0} y su altura es:{1}".format(lista_personajes[index]["nombre"],mas_alto))
#======================================================================================================================================
def mostrar_superheroe_mas_bajo():
    for i in range(len(lista_personajes)):
        if (i == 0 ):
            mas_bajo = float(lista_personajes[i]["altura"])
            index = i
        else: 
            if(float(mas_bajo) > (float(lista_personajes[i]["altura"]))):
              mas_bajo= float(lista_personajes[i]["altura"])
              index = i
    print("el superheroe mas bajo es :{0} y su altura es:{1}".format(lista_personajes[index]["nombre"],mas_bajo))
#======================================================================================================================================
def mostrar_altura_promedio():
    
    acumulador = 0
    for altura in lista_personajes:
        acumulador = acumulador + float(altura["altura"])
    promedio = acumulador / len(lista_personajes)
    print("el promedio de altura de los superheroes es de :{0}".format(promedio))
#======================================================================================================================================
def mostrar_identidad_mas_bajo_mas_alto():
    for i in range(len(lista_personajes)):
        if (i == 0 ):
            mas_bajo=float(lista_personajes[i]["altura"])
            index = i
        else: 
            if(float(mas_bajo) > (float(lista_personajes[i]["altura"]))):
              mas_bajo= float(lista_personajes[i]["altura"])
              index = i
    print("la identidad del superheroe mas bajo es :{0} y su altura es:{1}".format(lista_personajes[index]["identidad"],mas_bajo))
    
    for ind in range(len(lista_personajes)):
        if (ind== 0 ):
            mas_alto=float(lista_personajes[ind]["altura"])
            index = ind
        else: 
            if(float(mas_alto) < (float(lista_personajes[ind]["altura"]))):
              mas_alto = float(lista_personajes[ind]["altura"])
              index = ind
    print("La identidad del superheroe mas alto es :{0} y su altura es:{1}".format(lista_personajes[index]["identidad"],mas_alto))
#======================================================================================================================================
def mostrar_superheroe_mas_y_menos_pesado():
    for i in range(len(lista_personajes)):
        if (i == 0 ):
            mas_liviano=float(lista_personajes[i]["peso"])
            index = i
        else: 
            if(float(mas_liviano) > (float(lista_personajes[i]["peso"]))):
              mas_liviano= float(lista_personajes[i]["peso"])
              index = i
    print("la identidad del superheroe mas liviano es :{0} y su peso es  es:{1}".format(lista_personajes[index]["nombre"],mas_liviano))
    
    for ind in range(len(lista_personajes)):
        if (ind == 0 ):
            mas_pesado = float(lista_personajes[ind]["peso"])
            index = ind
        else: 
            if(float(mas_pesado)< (float(lista_personajes[ind]["peso"]))):
              mas_pesado = float(lista_personajes[ind]["peso"])
              index = ind
    print("La identidad del superheroe mas pesado es :{0}y su peso de  es:{1}".format(lista_personajes[index]["nombre"],mas_pesado))
#======================================================================================================================================
def mostrar_color_ojos_e_identidad():
    for identidad in lista_personajes:
        print("el superheroe es : {0} \n- su identidad es {1} \n- y su color de ojos es {2}\n".format(
            identidad["nombre"],
            identidad["identidad"],
            identidad["color_ojos"]))
        print("--------------------------------------------------------")
#======================================================================================================================================
def buscar_y_mostrar_superheroe():
    nombre_input = input("ingresa el nombre a buscar")
    flag = False
    for nombre in lista_personajes:
        if(nombre_input == nombre["nombre"]):
            print(nombre)
            flag =True
    if(flag == False):
        print("no se encontro el superheroe ")
#======================================================================================================================================
        
def main():

    while True:
        print("Menú de opciones:")
        print("1. Mostrar los nombres de todos los superheroes ")
        print("2. Mostrar nombre del superheroe con su altura")
        print("3. Mostrar superheroe mas alto")
        print("4. Mostrar superheroe mas bajo")
        print("5. Mostrar altura promedio de los superheroes ")
        print("6. Mostrar identidad mas bajo y mas alto ")
        print("7. Mostrar superheroe mas y menos pesado ")
        print("8. Mostrar todos los supeheroes con su identidad y color de ojos ")
        print("9. Buscar superheroe por su nombre y mostrar todos los datos")
        print("0. Salir del programa")
        opcion = input("\nIngrese la opción deseada: ")
        opcion_int= int(opcion)
        if (opcion_int== 1 ):
            mostrar_nombre_todos_los_superheroes()
            
        elif(opcion_int ==2):
            mostrar_nombre_y_altura_superheroes()
            
        elif(opcion_int == 3):
            mostrar_superheroe_mas_alto()
            pass
        elif(opcion_int == 4):
            mostrar_superheroe_mas_bajo()
            pass
        elif(opcion_int == 5):
            mostrar_altura_promedio()
            pass
        elif(opcion_int == 6):
            mostrar_identidad_mas_bajo_mas_alto()
            pass
        elif(opcion_int == 7):
            mostrar_superheroe_mas_y_menos_pesado()
            pass
        elif(opcion_int == 8):
            mostrar_color_ojos_e_identidad()
            pass
        elif(opcion_int == 9):
            buscar_y_mostrar_superheroe()

        elif(opcion_int == 0):
            break
        else:
            print("Opcion ingresada es invalida")
            
#======================================================================================================================================
main()