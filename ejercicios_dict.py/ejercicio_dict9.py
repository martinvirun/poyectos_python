# Crea un diccionario que contenga las capitales de los países de América del Sur. 
# Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.

dict_capitales = {"argentina":"la plata","bolivia":"la paz","paraguay":"asuncion","brasil":"brazilia"}
pais = input("ingrese pais")
flag = True
for paises in dict_capitales:
    if (pais == paises):
        print(dict_capitales[paises])
        flag = False

if(flag == True):
    print("este pais no se encuentra en la lista ")   
