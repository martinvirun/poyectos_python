
# 1.Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.

# 2.Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas.

# 3.Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos 
# strings concatenados, separados por un espacio.

# 4.Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.

# 5.Escribir una función que tome un string y un carácter y devuelva el número de veces que 
# aparece ese carácter en el string.

# 6.Escribir una función que tome un string y un carácter y devuelva una lista con todas las 
# palabras en el string que contienen ese carácter.

# 7.Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados

# 8.Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario 
# con el nombre y apellido, eliminando los espacios del comienzo y el final y colocando la primer 
# letra en mayúscula


# 9.Escribir una función que tome una lista de nombres y los una en una sola cadena separada por
# un salto de línea, por ejemplo: ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".

# 10.Escribir una función que tome un nombre y un apellido y devuelva un email en formato 
# "inicial_nombre.apellido@utn-fra.com.ar".

# 11.Escribir una función que tome una lista de palabras y devuelva un string que contenga 
# todas las palabras concatenadas con comas y "y" antes de la última palabra.
# Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"],
# el string resultante debería ser "manzanas, naranjas y bananas"..

# 12.Escribir una función que tome un número de tarjeta de crédito como input, 
# verificar que todos los caracteres sean numéricos y devolver los últimos
# cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234". 

# 13.Escribir una función que tome un correo electrónico y elimine cualquier carácter después del
# símbolo @, por ejemplo: "usuario@gmail.com" -> "usuario".

# 14.Escribir una función que tome una URL y devuelva solo el nombre de dominio, 
# por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..

# 15.Escribir una función que tome una cadena de texto y devuelva solo los caracteres alfabéticos, 
# eliminando cualquier número o símbolo, por ejemplo: "H0l4, m4nd0!" -> "Hl, mnd.

# 16.Escribir una función que tome una cadena de texto y la convierta en un acrónimo,
# tomando la primera letra de cada palabra, por ejemplo: "Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.

# 17.Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits, 
# rellenando con ceros a la izquierda si es necesario, por ejemplo: "101" -> "00000101".


# 18.scribir una función que tome una cadena de caracteres y reemplace todas las letras mayúsculas 
# por letras minúsculas y todas las letras minúsculas por letras mayúsculas,
# por ejemplo: "HoLa" -> "hOlA"


# 19.Escribir una función que tome una cadena de caracteres y cuente la cantidad 
# de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.


# 20.Escribir una función que tome una lista de direcciones de correo electrónico y 
# las una en una sola cadena separada por punto y coma, 
# por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".


# 21.Crear una función que reciba como parámetro un string y devuelva un diccionario 
# donde cada clave es una palabra y cada valor es un entero que indica cuántas veces 
# aparece esa palabra dentro del string.
#================================================================================================
# 1.Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.
def pasar_a_mayuscula(string:str):
   return string.upper()
#===============================================================================================
# 2.Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas.
def pasar_a_minuscula(string:str):
   return string.lower()
#===============================================================================================
# 3.Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos 
# strings concatenados, separados por un espacio.
def concatenar_dos_strings(lista):
   string = " "
   string = string.join(lista)
   return string
lista = ["hola","mundo"]
#================================================================================================
# 4.Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.
def calcular_tamaño_string(string:str):
   return len(string)
#================================================================================================
# 5.Escribir una función que tome un string y un carácter y devuelva el número de veces que 
# aparece ese carácter en el string.

def calcular_aparicin_de_caracter_en_string(string:str,caracter):
   return string.count(caracter)
#================================================================================================
# 6.Escribir una función que tome un string y un carácter y devuelva una lista con todas las 
# palabras en el string que contienen ese carácter.

def calcular_y_crear_lista_con_letra_a_buscar(string:str,caracter):
    lista = string.split(" ")
    nueva_lista = []

    for palabra in lista:
       for letra in palabra:
          if (caracter == letra):
             nueva_lista.append(palabra)
             break
    return nueva_lista

#================================================================================================
# 7.Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados
def eliminar_espacios_string(string:str):
   nuevo_string = string.replace(" ","")
   return nuevo_string 

#================================================================================================
# 8.Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario 
# con el nombre y apellido, eliminando los espacios del comienzo y el final y colocando la primer 
# letra en mayúscula

def crear_diccionaro_con_nombre_y_apellido(nombre:str,apellido:str):
   nombre = nombre.capitalize().strip()
   apellido = apellido.capitalize().strip()

   diccionario = {}
   diccionario["nombre"] = nombre
   diccionario["apellido"] = apellido
   return diccionario

print(crear_diccionaro_con_nombre_y_apellido("   martin   ","   virun   " ))
#================================================================================================
# 9.Escribir una función que tome una lista de nombres y los una en una sola cadena separada por
# un salto de línea, por ejemplo: ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".
def crear_lista_con_salto(lista):
   cadena = "\n"
   cadena = cadena.join(lista)

   return cadena
lista = ["hola","chau","martin"]
#================================================================================================
# 10.Escribir una función que tome un nombre y un apellido y devuelva un email en formato 
# "inicial_nombre.apellido@utn-fra.com.ar".
def crear_email(nombre,apellido):
   email = "inicial_nombre.apellido@utn-fra.com.ar"
   email = email.replace("nombre",nombre)
   email = email.replace("apellido",apellido)
   email = email.replace("inicial",nombre[0])
   return email
#================================================================================================
# 11.Escribir una función que tome una lista de palabras y devuelva un string que contenga 
# todas las palabras concatenadas con comas y "y" antes de la última palabra.
# Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"],
# el string resultante debería ser "manzanas, naranjas y bananas"..

def crear_lista_concatenada_con_comas(lista_palabras):
   cadena = ","
   cadena = cadena.join(lista_palabras)
############### falta ####################
#================================================================================================
# 12.Escribir una función que tome un número de tarjeta de crédito como input, 
# verificar que todos los caracteres sean numéricos y devolver los últimos
# cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234". 
def tomar_y_devolver_numero_tarjeta():
   numero = input("ingrese numero de tarjeta")
   if ( numero.isdigit() == True):
       ultimos_digitos = numero[-4:]
   print("el numero es {0} {1}".format("**** **** **** ",ultimos_digitos)) 
tomar_y_devolver_numero_tarjeta()
#================================================================================================
# 13.Escribir una función que tome un correo electrónico y elimine cualquier carácter después del
# símbolo @, por ejemplo: "usuario@gmail.com" -> "usuario".

def tomar_mail_y_eliminar_despues_de_arroba(email):
   nuevo_email = email.split("@")
   return nuevo_email[0]
print(tomar_mail_y_eliminar_despues_de_arroba("usuario@gmail.com"))
#================================================================================================
# 14.Escribir una función que tome una URL y devuelva solo el nombre de dominio, 
# por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..
def devolver_nombre_dominio(url):
   nombre_dominio = url.split(".")
   return nombre_dominio[1]
#================================================================================================
# 15.Escribir una función que tome una cadena de texto y devuelva solo los caracteres alfabéticos, 
# eliminando cualquier número o símbolo, por ejemplo: "H0l4, m4nd0!" -> "Hl, mnd.
def eliminar_caracteres_numericos(string):
   lista = []
   for letra in string:
      if (letra.isalpha() == True):
          lista.append(letra)
   return lista 

print(eliminar_caracteres_numericos("H0l4, m4nd0!"))
#================================================================================================
# 16.Escribir una función que tome una cadena de texto y la convierta en un acrónimo,
# tomando la primera letra de cada palabra, por ejemplo: "Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.

def crear_acronimo(string):
   acronimo = ""
   lista = string.split(" ")
   for palabra in lista :
      acronimo = acronimo + palabra[0]
   return acronimo
print(crear_acronimo("Universidad Tecnológica Nacional Facultad Regional Avellaneda"))
#================================================================================================
# 17.Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits, 
# rellenando con ceros a la izquierda si es necesario, por ejemplo: "101" -> "00000101".
def crear_cade_8_bits(numero):
   numero =  str(numero)
   return numero.zfill(8)

print(crear_cade_8_bits(1001))
#================================================================================================
# 18.scribir una función que tome una cadena de caracteres y reemplace todas las letras mayúsculas 
# por letras minúsculas y todas las letras minúsculas por letras mayúsculas,
# por ejemplo: "HoLa" -> "hOlA"

def cambiar_de_minuscula_A_mayuscula(string):
   nuevo_String = ""
   for letra in string:
      if (letra.isupper()== True):
          nuevo_String = nuevo_String + letra.lower()
      else:
         nuevo_String = nuevo_String + letra.upper()
   return nuevo_String

#================================================================================================
# 19.Escribir una función que tome una cadena de caracteres y cuente la cantidad 
# de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.
def contar_cantidad_digitos(string):
   contador = 0 
   for letra in string:
      if (letra.isdigit()== True):
         contador = contador + 1 
   return contador 
print(contar_cantidad_digitos("1234 Hola Mundo"))
#================================================================================================
# 20.Escribir una función que tome una lista de direcciones de correo electrónico y 
# las una en una sola cadena separada por punto y coma, 
# por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".
def concatenar_emails(lista):
    cadena = ";"
    cadena = cadena.join(lista)
    return cadena 
print(concatenar_emails(["juan@gmail.com", "maria@hotmail.com"]))
#================================================================================================
# 21.Crear una función que reciba como parámetro un string y devuelva un diccionario 
# donde cada clave es una palabra y cada valor es un entero que indica cuántas veces 
# aparece esa palabra dentro del string.
