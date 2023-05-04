# 15 Crear una función que recibe una lista de diccionarios con información de películas
# (título, género, director) y devuelve un diccionario con la cantidad de películas por género.

def mostrar_peliculas_por_genero(lista_peliculas):
    dic_nuevo = {}
    for pelicula in lista_peliculas:
        if (pelicula["genero"]in dic_nuevo ):
            dic_nuevo[pelicula["genero"]] = dic_nuevo[pelicula["genero"]] + 1
        else :
            dic_nuevo[pelicula["genero"]] = 1
    return dic_nuevo

lista_pelicula = [{"titulo":"titanic","genero":"drama","director":"martin"},
                 {"titulo":"matrix","genero":"accion","director":"carlos"},
                 {"titulo":"cars","genero":"animado","director":"luis"},
                 {"titulo":"lost","genero":"drama","director":"pedro"}]

resultado = mostrar_peliculas_por_genero(lista_pelicula)
print(resultado)