# Crea un diccionario que represente los asientos de un avión,
# donde las claves son los números de asientos y los valores son "True" si están ocupados y "False" si no lo están.
# Solicita al usuario un número de asiento y modifica su valor para marcarlo como ocupado.
# Luego imprimí la lista de asientos libres

dict_asientos = {"1":False,"2":True,"3":False,"4":False,"5":False}
numero_asiento = input("ingrese numero de asiento")
lista_libres = []


for numero in dict_asientos:
    if (numero_asiento == numero):
        if(dict_asientos[numero] == False ):
            dict_asientos[numero] = True
        else:
            print("este asiento se encuentra ocupado")
for numero in dict_asientos:
    if(dict_asientos[numero]== False):
        lista_libres.append(numero)

print("este haciento esta libre {0}".format(lista_libres))

