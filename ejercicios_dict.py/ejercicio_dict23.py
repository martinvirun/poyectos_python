# Crea un diccionario que represente los contactos de un teléfono,
# donde las claves son los nombres de las personas y los valores son los números de teléfono correspondientes.
# Solicitar al usuario el nombre de un contacto: agregarlo al diccionario en caso de que no exista. 
# En caso de que exista modificar el número de teléfono del contacto.


dict_contactos ={"martin":"114004","agustina":"156455","gaston":"6565654","lalo":"8542351","santi":"325644"}
nombre_contacto = input("ingrese nombre de contacto")
flag = False

for nombre in dict_contactos:
    if (nombre == nombre_contacto):
        dict_contactos[nombre]= input("ingrese nuevo numero")
        flag = True
if (flag == False):
    dict_contactos[nombre_contacto]= input("ingrese numero")
print(dict_contactos)
