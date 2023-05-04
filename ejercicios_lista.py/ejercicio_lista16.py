# Crea dos listas con la misma cantidad de elementos y luego crea una tercera lista que
#  contenga los elementos de ambas listas intercalados. Por ejemplo, si las dos listas son [1, 2, 3] y ["a", "b", "c"],
# la tercera lista debería ser [1, "a", 2, "b", 3, "c"].
lista_uno = [1,2,3,4,5]
lista_dos = ["a","B","c","D","e"]
lista_tres = []

for i in range(len(lista_uno)):
    lista_tres.append(lista_uno[i])
    lista_tres.append(lista_dos[i])
print(lista_tres)