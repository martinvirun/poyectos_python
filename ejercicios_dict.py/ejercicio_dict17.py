# Crea un diccionario que represente las películas de un cine,
# donde las claves son los nombres de las películas y los valores son los horarios correspondientes. 
# Modifica el horario de la película "Avengers: Endgame" a las 19:30.

dict_peliculas = {"Avengers: Endgame":"a las 18hs","poly":"a las 17hs","nemo":"a las 22hs"}
nombre_pelicula = input("nombre de la peli que quieras cambiar")
nuevo_horario = input("ingrese nuevo horario")

for nombre_peli in dict_peliculas:
    if (nombre_peli == nombre_pelicula):
        dict_peliculas[nombre_pelicula] = nuevo_horario
        flag = True
print(dict_peliculas) 