import re
#================================================================================================
# 1.Crear una función llamada es_mayuscula que reciba un string y devuelva True en caso de 
# que todas las letras sean mayúsculas o False en el caso contrario
def es_mayuscula(string:str):
    text = re.search('[a-z]+',string)
    if(text == None):
        return True
    else:
        return False
#================================================================================================
# 2.Crear una función llamada es_minuscula que reciba un string y devuelva True en caso 
# de que todas las letras sean mayúsculas o False en el caso contrario
def es_minuscula(string:str):
    text = re.search('[A-Z]+',string)
    if(text == None):
        return True
    else:
        return False
#================================================================================================
# 3.Crear una función llamada es_entero que reciba un string y devuelva True en caso de 
# que se trate de un número entero y False en caso contrario.
def es_entero(string:str):
    text = re.search('[^0-9]+',string)
    if(text == None):
        return True
    else:
        return False
#================================================================================================
# 4.Crear una función llamada es_solo_texto que reciba un string y devuelva True en caso 
# de que trate solo de caracteres alfabéticos y el espacio y False en el caso contrario
def es_solo_texto(string:str):
    text = re.search('[^a-zA-Z ]+',string)
    if(text == None):
        return True
    else:
        return False
#================================================================================================
# 5.Crear una función llamada es_decimal que reciba dos strings: el primero representa la 
# expresión a evaluar y el segundo el separador decimal (puede ser punto . o coma ,). 
# Debe devolver True en caso que se trate de un número decimal y False en el caso contrario.
def es_decimal(numero:str,separador:str):
    text_num = re.search('[^0-9.,]+',numero)
    text_separador = re.search('[.,]{1}',numero)
    if(text_num == None and text_separador != None):
        return True
    else:
        return False
#================================================================================================
# 6.Crear una función llamada es_alfanumerico que devuelva True en caso de tratarse de 
# solo letras y números y False en el caso contrario (es decir que contenga caracteres especiales)

def es_alfanumerico(string:str):
     texto = re.search("[^a-zA-Z0-9 ]+",string)

     if (texto != None):
         return False
     else:
         return True
#================================================================================================
# 7.Crear una función llamada es_binario que devuelva True en caso de un número binario 
# válido (solo ceros y unos) o False en el caso contrario

def es_binario(string:str):
    texto = re.search("[^01]+",string)

    if (texto != None):
         return False
    else:
         return True
#================================================================================================
# 8.Crear una función que reciba una lista de palabras y devuelva otra lista con las palabras 
#  que comienzan con la letra ‘U’

def devolver_palabra_comienza_u(lista:list):
    lista_nueva =[]
    for palabra in lista:
        if(re.search("^u",palabra)):
            lista_nueva.append(palabra)
    return lista_nueva
#================================================================================================
# 9.Crear una función que reciba un texto y devuelva una lista con las palabras que contienen
#  entre 3 y 6 caracteres de largo

def devolver_palabra_mas_3_caracteres(texto):
    lista = re.split(" ",texto)
    nueva_lista = []
    for palabra in lista:
        if(len(palabra)>3 and len(palabra)<=6 ):
            nueva_lista.append(palabra)
      

    return nueva_lista
#================================================================================================
# 10.Crear una función que reciba un texto y devuelva una lista de todas las palabras que 
# terminan con ‘ción’. Ejemplo de texto: https://onlinegdb.com/swyremkF6
def devolver_palabras_terminadas_cion(texto:str):
    lista = re.split(" ",texto)
    nueva_lista = []

    for palabra in lista:
        if(re.search("ción$",palabra) != None):
            nueva_lista.append(palabra)
    return nueva_lista
#================================================================================================
# 11.Crear una función que reciba un texto y devuelva una la lista de palabras encuentra que 
# comienzan con una vocal
def devolver_lista_palabras_comiezan_vocal(texto:str):
    lista = re.split(" ",texto)
    nueva_lista = []
    
    for palabra in lista:
        if(re.search("^a|^e|^i|^o|^u",palabra) != None):
            nueva_lista.append(palabra)
    return nueva_lista
#================================================================================================
# 12.Crear una función llamada obtener_oraciones que reciba como parámetro un string y que 
# devuelva una lista con las oraciones (delimitadores, ‘.’, ‘!’, ‘?’). Ejemplo de texto: 
# https://onlinegdb.com/UMdr3hI3G

def obtener_oraciones(texto:str):
    lista_oraciones = re.split("[.|,|!|?]",texto)
    return lista_oraciones

#================================================================================================
# 13.Crear una función que reciba un texto como parámetro y que corrija los errores de ortografía
#  que no cumplan con la regla ortográfica que indica que antes de V se escribe N y que antes 
#  de B se escribe M. 
# Por ejemplo, si el texto es: "Mi comvicción me hace sentir que es el momento de imvertir 
# tiempo para finalmente envarcar en esta nueva aventura." La función debería devolver:
# “Mi convicción me hace sentir que es el momento de invertir tiempo para finalmente embarcar 
# en esta nueva aventura."
def correjir_falta_ortografia_mv(texto:str):
    texto_nuevo = re.sub("mv","nv",texto)
    texto_def = re.sub("nb","mb",texto_nuevo)

    return texto_def
#================================================================================================
# 14.Crear la función es_fecha que reciba dos string, el primero representa la expresión a evaluar y 
# el segundo el separador de la fecha (puede ser la barra / o el guión -) y que devuelva True 
# en caso de tratarse de una fecha válida y False en el caso contrario. Los formatos admitidos 
# son: ‘dd/mm/aaaa’ o ‘dd-mm-aaaa’

def es_fecha(fecha:str,separador:str):
    patron = "[0-9]{0}{1}[0-9]{0}{1}[0-9]{2}".format({2},separador,{4})
    if (re.search(patron,fecha) !=None ):
        return True
    else:
        return False
#================================================================================================
# 15.Crear la función es_hora que reciba un string y que devuelva True en caso de tratarse de una 
# hora válida y False en el caso contrario. El formato admitido es ‘hh:mm:ss’
def es_hora(texto:str):

   if (re.search("[0-9]{2}:[0-9]{2}:[0-9]{2}",texto) !=None ):
        return True
   else:
        return False 
#================================================================================================
# 16.Crear la función validar_codigo_postal que reciba un string como parámetro y devuelva True
#  en caso de tratarse de código postal válido o False en caso contrario. 
def validar_codigo_postal(texto:str):
    if (re.search("[A-Za-z]{1}[0-9]{4}[A-Za-z]{3}",texto) !=None ):
        return True
    else:
        return False 

#================================================================================================
# 17.Crear la función validar_patente que reciba un string como parámetro y devuelva 
# True en caso de tratarse de un número de patente válido o False en caso contrario.  
# Debe poder admitir estos dos tipos:
def validar_patente(texto:str):
    if (re.search("[A-Za-z]{2}[0-9]{3}[A-Za-z]{2}",texto) !=None or re.search("[A-Za-z]{3}[0-9]{3}",texto)):
        return True
    else:
        return False 
#================================================================================================
# 18.Crear una función que se llame obtener_direcciones_email que reciba un texto y 
# devuelva una lista con todas las direcciones de email válidas que encuentren en el mismo.
#  Acá dejamos un texto de ejemplo: https://onlinegdb.com/Ln0jhatKeI
def obtener_direcciones_email(texto:str):
    lista = re.split(" ",texto)
    lista_mails = []

    for partes in lista:
        if (re.search("[A-Za-z0-9.]+@[A-Za-z]+.com",partes) != None ) :
            lista_mails.append(partes)

    return lista_mails

#================================================================================================
# 19.Crear una función llamada validar_password que reciba un string y verifique si 
# se trata de una contraseña cumple con los requisitos mínimos de seguridad:
# Al menos 8 caracteres
# Al menos una letra mayúscula y una letra minúscula
# Un número 
# Un carácter especial
# En caso de no cumplir con alguno de los requisitos, imprimir un mensaje informando 
# cual no se cumplio

def validar_password(texto):
    flag = True
    if (re.search("[A-Za-z0-9.|,|/|*|-|!]{8,}",texto)!= None):
        pass
    else:
        flag = False 
        print("no tiene 8 caracteres o mas")
    if (re.search("[A-Z]{1,}",texto)!= None):
        pass
    else:
        flag = False 
        print("no tiene por lo menos una letra mayúscula ")
    if (re.search("[a-z]{1,}",texto)!= None):
        pass
    else:
        flag = False 
        print("no tiene por lo menos una letra minúscula")
    if (re.search("[0-9]{1,}",texto)!= None):
        pass
    else:
        flag = False 
        print("no tiene por lo menos un numero")
    if (re.search("[.|,|/|*|-|!]{1,}",texto)!= None):
        pass
    else:
        flag = False 
        print("no tiene un caracter especial")  
    return flag
#================================================================================================
#20. Crear una función llamada validar_ip que reciba un string como parámetro y verifique 
# si se trata de una dirección IP v4 válida, en caso de serlo retornar True de lo contrario 
# retornar False. 
# Se considera una dirección IP válida si tiene el formato xxx.xxx.xxx.xxx, donde xxx es un número 
# entero entre 0 y 255.
def validar_ip(texto:str):
    if (re.search("[0-2]{1}[0-5]{1}[0-9]{1}.[0-2]{1}[0-5]{1}[0-9]{1}.[0-2]{1}[0-5]{1}[0-9]{1}.[0-2]{1}[0-5]{1}[0-9]{1}",texto)!= None):
        return True
    else:
        return False 
