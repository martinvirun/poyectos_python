# Crea un diccionario que contenga el nombre como clave y el puntaje como valor de varios jugadores en un juego. 
# Luego, pedirle al usuario el nombre del jugador y nuevo puntaje y actualizar el valor correspondiente en el diccionario.

dict_puntaje = {"martin":100,"lolo":20,"carlos":55,"angeles":99}
nombre = input("ingrese el nombre")
puntaje_ingresado = input("ingrese nuevo puntaje")
puntaje_parceado = int(puntaje_ingresado)
flag = False

for nom in dict_puntaje:
    if (nom == nombre):
        dict_puntaje[nom] = puntaje_parceado
        flag = True
if (flag == True): 
    print("el nombre ingresado es {0} y su nuevo puntaje es {1}".format(nombre,dict_puntaje[nombre]))
    print(dict_puntaje)
else:
    print("nombre no encontrado")