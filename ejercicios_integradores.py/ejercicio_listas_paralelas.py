# Gimnasio - Listas paralelas
# Un gimnasio desea llevar el control de sus miembros. Cada miembro tiene un número de identificación, 
# nombre, edad y tipo de membresía (por ejemplo, mensual o anual). 
# La información se encuentra almacenada en cuatro listas paralelas:
#  una lista con los números de identificación, otra lista con los nombres,
#  una lista con las edades y una lista con los tipos de membresía.

# Escriba un programa que permita a los usuarios realizar las siguientes operaciones:

# Agregar un nuevo miembro: el programa debe pedir al usuario que ingrese el número de identificación, 
# nombre, edad y tipo de membresía del nuevo miembro. La información debe ser agregada a las listas paralelas.


# Mostrar toda la información de todos los miembros (número de identificación, nombre, edad y tipo de membresía).

# Actualizar el tipo de membresía de un miembro: el programa debe pedir al usuario que ingrese el número de identificación
# del miembro y el nuevo tipo de membresía. El programa debe buscar el número 
# de identificación en la lista de números de identificación 
# y actualizar el tipo de membresía correspondiente en la lista de tipos de membresía.
# En caso de no encontrar al miembro informar con un mensaje de que el mismo no se encontró

# Buscar información de un miembro: el programa debe pedir al usuario que ingrese el número de identificación del miembro.
# El programa debe buscar el número de identificación en la lista de números de identificación y mostrar el nombre,
# edad y tipo de membresía correspondientes en las listas de nombres, edades y tipos de membresía.


# Calcular el promedio de edad de los miembros: el programa debe recorrer la lista de edades y calcular el promedio 
# de edad de los miembros.

# Buscar el miembro más joven y el más viejo: el programa debe buscar la edad máxima y mínima en la lista de edades
# y mostrar el nombre y número de identificación correspondientes en las listas de nombres y números de identificación.

# El programa debe permitir al usuario realizar estas operaciones tantas veces como desee, hasta que decida salir del programa.
# El programa debe mostrar un menú de opciones para que el usuario pueda elegir la operación que desea realizar.

nombre_miembros = ["martin","carlos","luis"]
edad_miembros = [25,35,20]
id_miembros = [1000,1001,1002]
membresia_miembros = ["anual","anual","mensual"]

contador = 1003
flag_si_hay_un_miembro = False
flag_membresia = False

contador_edad = 0
acumulador_edad = 0

while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")


    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":
        nombre_miembros.append(input("ingrese nombre del nuevo socio"))
        edad_miembros.append(input("ingrese edad del nuevo socio"))
        membresia_miembros.append(input("ingrese tipo de membresia del nuevo socio"))
        id_miembros.append(contador)
        contador = contador + 1
        flag_si_hay_un_miembro = True
        

        pass
       
    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        if(flag_si_hay_un_miembro==True):
            for i in range(len(nombre_miembros)):
                print("nombre : {0} , edad : {1} , membresia : {2} , id : {3}".format(nombre_miembros[i],
                                                                                      edad_miembros[i],
                                                                                      membresia_miembros[i],
                                                                                      id_miembros[i]))
        else:
            print("todavia no hay socios ingresados")
            pass
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        id = input("ingrese id del socio al que le quieres cambiar la membresia")
        id_casteado = int(id)
        for i in range(len(nombre_miembros)):
            if(id_casteado == id_miembros[i]):
                membresia_miembros[i]= input("cual es la nueva membresia?")
                flag_membresia = True
        if (flag_membresia != True):
            print("no se encontro ningun socio con ese id")
        pass


    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        id_opcion_4 = input("ingrese id del socio al que le quieres cambiar la membresia")
        id_opcion_4_casteado = int( id_opcion_4)
        for i in range(len(nombre_miembros)):
            if(id_opcion_4_casteado == id_miembros[i]):
                print("nombre :{0} edad: {1} membresia : {2}".format(nombre_miembros[i],
                                                                     edad_miembros[i],
                                                                     membresia_miembros[i]))
        pass


    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        for i in range(len(nombre_miembros)):
            contador_edad = contador_edad + 1 
            acumulador_edad = acumulador_edad + int(edad_miembros[i])
        
        promedio_edad = acumulador_edad / contador_edad
        print("el promedio de las edades es de {0}".format(round( promedio_edad,2)))
        
        pass


    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        if(len(nombre_miembros)>0):
            edad_joven = edad_miembros[0]
            edad_viejo = edad_miembros[0]
            indice_joven = 0
            for ind in range(len(nombre_miembros)):
                if (edad_miembros[ind]< edad_joven):
                    edad_joven = edad_miembros[ind]
                    indice_joven = ind
            for i in range(len(nombre_miembros)):
                if (edad_miembros[i] > edad_viejo):
                    edad_viejo = edad_miembros[i]
                    indice_viejo = i
        print("el mas viejo se llama :{0} de edad :{1} membresia :{2} id :{3} ".format(nombre_miembros[indice_viejo],
                                                                                       edad_miembros[indice_viejo],
                                                                                       membresia_miembros[indice_viejo],
                                                                                       id_miembros[indice_viejo]))
        
        print("el mas joven se llama :{0} de edad :{1} membresia :{2} id :{3} ".format(edad_miembros[indice_joven],
                                                                                       edad_miembros[indice_joven],
                                                                                       membresia_miembros[indice_joven],
                                                                                       id_miembros[indice_joven]))
            

        pass


    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")
