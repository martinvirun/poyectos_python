# Gimnasio - Lista de diccionarios
# Un gimnasio desea llevar el control de sus miembros. Cada miembro tiene un número de identificación,
# nombre, edad y tipo de membresía (por ejemplo, mensual o anual). La información se encuentra almacenada en una 
# lista de listas, donde cada sublista representa a un miembro y contiene los siguientes elementos: 
# número de identificación, nombre, edad y tipo de membresía.

# Escriba un programa que permita a los usuarios realizar las siguientes operaciones:

# Agregar un nuevo miembro: el programa debe pedir al usuario que ingrese el número de identificación,
# nombre, edad y tipo de membresía del nuevo miembro. La información debe ser agregada a la lista de diccionarios.


# Mostrar toda la información de todos los miembros (número de identificación, nombre, edad y tipo de membresía).

# Actualizar el tipo de membresía de un miembro: el programa debe pedir al usuario que ingrese el número de 
# identificación del miembro y el nuevo tipo de membresía. El programa debe buscar el miembro en la lista de
# diccionario y actualizar el tipo de membresía correspondiente.

# Buscar información de un miembro: el programa debe pedir al usuario que ingrese el número de identificación del miembro.
# El programa debe buscar el miembro en la lista de diccionarios y mostrar su nombre, edad y tipo de membresía.

# Calcular el promedio de edad de los miembros: el programa debe recorrer la lista de diccionarios y calcular el 
# promedio de edad de los miembros.

# Buscar el miembro más joven y el más viejo: el programa debe buscar la edad máxima y mínima en la lista de diccionarios
# y mostrar el nombre y número de identificación correspondientes.

# El programa debe permitir al usuario realizar estas operaciones tantas veces como desee, hasta que decida salir del programa.
# El programa debe mostrar un menú de opciones para que el usuario pueda elegir la operación que desea realizar.


lista_miembros = [{"Nombre":"Martin","edad":25,"Membresia":"anual","id":1000},
                  {"Nombre":"Carlos","edad":20,"Membresia":"mensual","id":1001},
                  {"Nombre":"juan","edad":22,"Membresia":"anual","id":1002}]

contador_id = 1003
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
        aux_miembro = {}
        aux_miembro["Nombre"]= input("ingrese nombre nuevo socio ")
        edad = input("ingrese su edad")
        edad_casteada = int(edad)
        aux_miembro["edad"] = edad_casteada
        aux_miembro["Membresia"]= input("ingrese membresia nuevo socio ")
        aux_miembro["id"]= contador_id
        contador_id = contador_id + 1 
        lista_miembros.append(aux_miembro)

        pass
       
    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        for i in range(len(lista_miembros)):
          print("el nombre es:{0} edad:{1} membresia:{2},id:{3}".format(lista_miembros[i]["Nombre"],
                lista_miembros[i]["edad"],
                lista_miembros[i]["Membresia"],
                lista_miembros[i]["id"]))
          print("___________________________________________________________________________________")
       
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        id = input("ingrese id del socio al que le quieres cambiar la membresia")
        id_casteado = int(id)
        for i in range(len(lista_miembros)):
            if(id_casteado == lista_miembros[i]["id"]):
                lista_miembros[i]["Membresia"]= input("ingrese nueva membresia")
                flag_membresia = True
        if (flag_membresia != True):
            print("no se encontro ningun socio con ese id")
        pass


    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        id_opcion_4 = input("ingrese id del socio ")
        id_opcion_4_casteado = int( id_opcion_4)
        for i in range(len(lista_miembros)):
            if(id_opcion_4_casteado == lista_miembros[i]["id"]):
                print("nombre :{0} edad: {1} membresia : {2}".format(lista_miembros[i]["Nombre"],
                                                                     lista_miembros[i]["edad"],
                                                                     lista_miembros[i]["Membresia"]))
        pass


    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        for i in range(len(lista_miembros)):
            contador_edad = contador_edad + 1 
            acumulador_edad = acumulador_edad + int(lista_miembros[i]["edad"])
        
        promedio_edad = acumulador_edad / contador_edad
        print("el promedio de las edades es de {0}".format(round( promedio_edad,2)))
        pass


    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        if(len(lista_miembros)>0):
            edad_joven = lista_miembros[0]["edad"]
            edad_viejo = lista_miembros[0]["edad"]
            indice_joven = 0
            indice_viejo = 0
            for ind in range(len(lista_miembros)):
                if (lista_miembros[ind]["edad"]< edad_joven):
                    edad_joven = lista_miembros[ind]["edad"]
                    indice_joven = ind
            for i in range(len(lista_miembros)):
                if (lista_miembros[i]["edad"] > edad_viejo):
                    edad_viejo = lista_miembros[i]["edad"]
                    indice_viejo = i
        print("el mas viejo se llama :{0} de edad :{1} membresia :{2} id :{3} ".format(lista_miembros[indice_viejo]["Nombre"],
                                                                                       lista_miembros[indice_viejo]["edad"],
                                                                                       lista_miembros[indice_viejo]["Membresia"],
                                                                                       lista_miembros[indice_viejo]["id"]))
        
        print("el mas joven se llama :{0} de edad :{1} membresia :{2} id :{3} ".format(lista_miembros[indice_joven]["Nombre"],
                                                                                       lista_miembros[indice_joven]["edad"],
                                                                                       lista_miembros[indice_joven]["Membresia"],
                                                                                       lista_miembros[indice_joven]["id"]))
        pass


    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")