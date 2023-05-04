

# Crea un diccionario que represente los juegos de una consola,
# donde las claves son los nombres de los juegos y los valores son las puntuaciones correspondientes.
# Solicita al usuario el nombre de un juego y luego su puntuación,
# si el juego no existe agregarlo y si existe actualizar su puntuación 
dict_juegos = {"gta":"1566pts","tetris":"1899pts","gt auto":"9566pts"}
nombre_juego = input("ingrese nombre de juego ")
nueva_puntacion = input("ingresa nueva puntuacion")
flag = False

for juego in dict_juegos:
    if (juego == nombre_juego):
        dict_juegos[juego]=nueva_puntacion
        flag = True
if(flag == False):
    dict_juegos[nombre_juego]= nueva_puntacion
print(dict_juegos)