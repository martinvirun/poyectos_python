# Crea un diccionario que contenga el nombre y el nivel de dificultad de varios juegos de mesa.
# Luego, pedirle al usuario un nivel de dificultad, buscar los que coinciden e imprimir sus nombres

dict_juegos = {"monopoly":"facil","T.E.G":"dificil","generala":"facil","estanciero":"moderado",
               "truco":"dificil","chin-chon":"moderado"}

print("LAS DIFICULATADES SON : FACIL - MODERADO - DIFICIL ")
dificultad = input("ingrese dificultad a buscar")

for dif in dict_juegos:
    if (dict_juegos[dif] == dificultad):
        print (dif)
