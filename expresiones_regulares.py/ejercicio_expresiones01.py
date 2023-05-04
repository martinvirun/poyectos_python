
import re
import expresiones_regulares_biblioteca
from expresiones_regulares_biblioteca import es_mayuscula
from expresiones_regulares_biblioteca import es_minuscula
from expresiones_regulares_biblioteca import es_entero
from expresiones_regulares_biblioteca import es_solo_texto
from expresiones_regulares_biblioteca import es_decimal
from expresiones_regulares_biblioteca import es_alfanumerico
from expresiones_regulares_biblioteca import es_binario
from expresiones_regulares_biblioteca import devolver_palabra_comienza_u
from expresiones_regulares_biblioteca import devolver_palabra_mas_3_caracteres
from expresiones_regulares_biblioteca import devolver_palabras_terminadas_cion
from expresiones_regulares_biblioteca import devolver_lista_palabras_comiezan_vocal
from expresiones_regulares_biblioteca import obtener_oraciones
from expresiones_regulares_biblioteca import correjir_falta_ortografia_mv
from expresiones_regulares_biblioteca import es_fecha
from expresiones_regulares_biblioteca import es_hora
from expresiones_regulares_biblioteca import validar_codigo_postal
from expresiones_regulares_biblioteca import validar_patente
from expresiones_regulares_biblioteca import obtener_direcciones_email
from expresiones_regulares_biblioteca import validar_password
from expresiones_regulares_biblioteca import validar_ip
#================================================================================================
# 1.Crear una función llamada es_mayuscula que reciba un string y devuelva True en caso de 
# que todas las letras sean mayúsculas o False en el caso contrario
print("================== ej 1 ====================================")
print(es_mayuscula("hola"))
print(es_mayuscula("HOLA"))
print(es_mayuscula("holA"))
#================================================================================================
# 2.Crear una función llamada es_minuscula que reciba un string y devuelva True en caso 
# de que todas las letras sean mayúsculas o False en el caso contrario
print("================== ej 2 ====================================")
print(es_minuscula("hola"))
print(es_minuscula("HOLA"))
print(es_minuscula("holA"))
#================================================================================================
# 3.Crear una función llamada es_entero que reciba un string y devuelva True en caso de 
# que se trate de un número entero y False en caso contrario.
print("===================ej 3 ===================================")
print(es_entero("1525"))
print(es_entero("15.55"))
#================================================================================================
# 4.Crear una función llamada es_solo_texto que reciba un string y devuelva True en caso 
# de que trate solo de caracteres alfabéticos y el espacio y False en el caso contrario
print("=====================ej 4 ================================")
print(es_solo_texto("hola1"))
print(es_solo_texto("hola Martin"))
print(es_solo_texto("hola"))
#================================================================================================
# 5.Crear una función llamada es_decimal que reciba dos strings: el primero representa la 
# expresión a evaluar y el segundo el separador decimal (puede ser punto . o coma ,). 
# Debe devolver True en caso que se trate de un número decimal y False en el caso contrario.
print("======================ej 5 ================================")
print(es_decimal("15.50","."))
print(es_decimal("15","."))
#================================================================================================
# 6.Crear una función llamada es_alfanumerico que devuelva True en caso de tratarse de 
# solo letras y números y False en el caso contrario (es decir que contenga caracteres especiales)
print("=====================ej 6 =================================")
print(es_alfanumerico("hola martin **")) 
print(es_alfanumerico("hola martin 25")) 
print(es_alfanumerico("hola martin")) 
#================================================================================================
# 7.Crear una función llamada es_binario que devuelva True en caso de un número binario 
# válido (solo ceros y unos) o False en el caso contrario
print("=====================ej 7 =================================")
print(es_binario("011011100"))
print(es_binario("011011x00"))
print(es_binario("011011200"))
#================================================================================================
# 8.Crear una función que reciba una lista de palabras y devuelva otra lista con las palabras 
#  que comienzan con la letra ‘U’
print("=====================ej 8=================================")
lista = ["ulala","lala","uno","onuuuu"]
print(devolver_palabra_comienza_u(lista))
#================================================================================================
# 9.Crear una función que reciba un texto y devuelva una lista con las palabras que contienen
#  entre 3 y 6 caracteres de largo
print("=====================ej 9=================================")
print(devolver_palabra_mas_3_caracteres("hola martin como re ssdaasdad esras"))
#================================================================================================
# 10.Crear una función que reciba un texto y devuelva una lista de todas las palabras que 
# terminan con ‘ción’. Ejemplo de texto: https://onlinegdb.com/swyremkF6
print("=====================ej 10=================================")
texto = "La tecnología de la información ha revolucionado la comunicación en todas sus formas. La digitalización y la automatización de procesos han permitido la optimización de los recursos y la mejora en la eficiencia de los sistemas. La cibernética, la robótica y la inteligencia artificial son algunas de las áreas de la informática que se han desarrollado en las últimas décadas y han transformado la forma en que vivimos y trabajamos. La interconexión de dispositivos y la transmisión de datos en tiempo real han permitido la creación de nuevas industrias y modelos de negocio que antes eran impensables. La educación, la salud, el transporte y la logística son algunos de los sectores que han sido beneficiados por la innovación tecnológica. En conclusión, la tecnología ha generado una revolución en nuestra sociedad que ha llevado a la transformación y evolución de la misma."
print(devolver_palabras_terminadas_cion(texto))
#================================================================================================
# 11.Crear una función que reciba un texto y devuelva una la lista de palabras encuentra que 
# comienzan con una vocal
print("=====================ej 11=================================")
print(devolver_lista_palabras_comiezan_vocal(texto))
#================================================================================================
# 12.Crear una función llamada obtener_oraciones que reciba como parámetro un string y que 
# devuelva una lista con las oraciones (delimitadores, ‘.’, ‘!’, ‘?’). Ejemplo de texto: 
# https://onlinegdb.com/UMdr3hI3G
print("=====================ej 12=================================")
texto_B = "¿Bello es mejor que feo? Explícito es mejor que implícito. Simple es mejor que complejo. Complejo es mejor que complicado. Plano es mejor que anidado. Espaciado es mejor que denso. La legibilidad es importante. Los casos especiales no son lo suficientemente especiales como para romper las reglas. Sin embargo la practicidad le gana a la pureza. Los errores nunca deberían pasar silenciosamente. A menos que se silencien explícitamente. Frente a la ambigüedad, evitar la tentación de adivinar. Debería haber una, y preferiblemente solo una, manera obvia de hacerlo. A pesar de que eso no sea obvio al principio a menos que seas Holandés. Ahora es mejor que nunca. A pesar de que nunca es muchas veces mejor que *ahora* mismo. Si la implementación es difícil de explicar, es una mala idea. Si la implementación es fácil de explicar, puede que sea una buena idea. Los espacios de nombres son una gran idea, ¡tengamos más de esos!"
print(obtener_oraciones(texto_B))
#================================================================================================
# 13.Crear una función que reciba un texto como parámetro y que corrija los errores de ortografía
#  que no cumplan con la regla ortográfica que indica que antes de V se escribe N y que antes 
#  de B se escribe M. 
# Por ejemplo, si el texto es: "Mi comvicción me hace sentir que es el momento de imvertir 
# tiempo para finalmente envarcar en esta nueva aventura." La función debería devolver:
# “Mi convicción me hace sentir que es el momento de invertir tiempo para finalmente embarcar 
# en esta nueva aventura."
print("=====================ej 13=================================")
texto_c = "Mi comvicción me hace sentir que es el momento de imvertir tiempo para finalmente envarcar en esta nueva aventura."
print(correjir_falta_ortografia_mv(texto_c))
#================================================================================================
# 14.Crear la función es_fecha que reciba dos string, el primero representa la expresión a evaluar y 
# el segundo el separador de la fecha (puede ser la barra / o el guión -) y que devuelva True 
# en caso de tratarse de una fecha válida y False en el caso contrario. Los formatos admitidos 
# son: ‘dd/mm/aaaa’ o ‘dd-mm-aaaa’
print("=====================ej 14=================================")
print(es_fecha("25-05-2022","-"))
print(es_fecha("25/05/2022","/"))
print(es_fecha("25-05/2022","/"))

#================================================================================================
# 15.Crear la función es_hora que reciba un string y que devuelva True en caso de tratarse de una 
# hora válida y False en el caso contrario. El formato admitido es ‘hh:mm:ss’
print("=====================ej 15=================================")
print(es_hora("02/02:60"))
print(es_hora("02:02:60"))

#================================================================================================
# 16.Crear la función validar_codigo_postal que reciba un string como parámetro y devuelva True
#  en caso de tratarse de código postal válido o False en caso contrario. 
print("=====================ej 16=================================")
print(validar_codigo_postal("B1636FDA"))
print(validar_codigo_postal("B1636FD"))
print(validar_codigo_postal("B166FDA"))
print(validar_codigo_postal("B1636F1A"))
#================================================================================================
# 17.Crear la función validar_patente que reciba un string como parámetro y devuelva 
# True en caso de tratarse de un número de patente válido o False en caso contrario.  
# Debe poder admitir estos dos tipos:
print("=====================ej 17=================================")
print(validar_patente("af136da"))
print(validar_patente("afl136"))
print(validar_patente("afl13l"))
#================================================================================================
# 18.Crear una función que se llame obtener_direcciones_email que reciba un texto y 
# devuelva una lista con todas las direcciones de email válidas que encuentren en el mismo.
#  Acá dejamos un texto de ejemplo: https://onlinegdb.com/Ln0jhatKeI
print("=====================ej 18=================================")
mails =" <Alberto, Cervantes> acervantes@gmx.com <Ana, Jimenez> ajimenez@hotmail.com <Antonio, Castillo> acastillo@gmail.com <Armando, Vega> avega@yahoo.com <Arturo, Arredondo> aarredondo@gmail.com <Beatriz, Vargas> bvargas@outlook.com <Berenice, Rios> bribos@yahoo.com <Brenda, Gonzalez> bgonzalez@terra.com <Brian, Hernandez> bhernandez@outlook.com <Camila, Reyes> creyes@terra.com <Carlos, Gallegos> cgallegos@gmail.com <Carolina, Alvarado> calvarado@outlook.com <Cesar, Rosales> crosales@terra.com <Christian, Moreno> cmoreno@gmail.com <Clara, Serrano> cserrano@yahoo.com <Cristian, Huerta> chuerta@terra.com <Cristina, Ochoa> cochoa@yahoo.com <Dalia, Rivas> drivas@outlook.com <Daniel, Perez> dperez@yahoo.com <Daniela, Ruiz> druiz@outlook.com <David, Velasco> dvelasco@gmail.com <Diana, Andrade> dandrade@yahoo.com <Diego, Ortiz> dortiz@terra.com <Eduardo, Vazquez> evazquez@gmail.com <Elisa, Castillo> ecastillo@outlook.com <Elizabeth, Cruz> ecruz@yahoo.com <Emmanuel, Pacheco> epacheco@terra.com <Enrique, Fuentes> efuentes@gmail.com <Erika, Cabrera> ecabrera@yahoo.com <Erick, Zavala> ezavala@outlook.com <Esmeralda, Valdes> evaldes@gmx.com <Esteban, Montes> emontes@gmail.com <Evelyn, Vera> evera@yahoo.com <Fabian, Rangel> frangel@terra.com <Fatima, De La Cruz> fdela@gmx.com <Felipe, Salas> fsalas@outlook.com <Fernanda, Guerrero> fguerrero@gmail.com <Fernando, Olvera> folvera@yahoo.com <Francisco, Hernandez> fhernandez@terra.com <Gabriela, Acosta> gacosta@gmail.com <Gael, Maldonado> gmaldonado@outlook.com <Gerardo, Flores> gflores@yahoo.com <Giselle, Alvarado> galvarado@terra.com <Gloria, Tapia> gtapia@gmx.com <Gonzalo, Zamora> gzamora@yahoo.com <Graciela, Ochoa> gochoa@outlook.com <Guadalupe, Aguilar> gaguilar@gmail.com <Guillermo, Garza> ggarza@yahoo.com <Gustavo, Mora> gmora@terra.com <Heidi, Hernandez> hhernandez@gmx.com <Hector, Barrios> hbarrios@outlook.com <Hugo, Villarreal> hvillarreal@yahoo.com <Ignacio, Soto> isoto@gmail.com <Ingrid, Vidal> ividal@yahoo.com <Irma, Garza> igarza@terra.com <Isaac, Palacios> ipalacios@gmail.com <Ivan, Rojas> irojas@yahoo.com <Jacqueline, Fuentes> jfuentes@outlook.com <Jaime, Huerta> jhuerta@yahoo"

print(obtener_direcciones_email(mails))
#================================================================================================
# 19.Crear una función llamada validar_password que reciba un string y verifique si 
# se trata de una contraseña cumple con los requisitos mínimos de seguridad:
# Al menos 8 caracteres
# Al menos una letra mayúscula y una letra minúscula
# Un número 
# Un carácter especial
# En caso de no cumplir con alguno de los requisitos, imprimir un mensaje informando 
# cual no se cumplio
print("=====================ej 19=================================")
if(validar_password("mARTIN7.852")==True):
    print("La contraceña es valida")
#================================================================================================
#20. Crear una función llamada validar_ip que reciba un string como parámetro y verifique 
# si se trata de una dirección IP v4 válida, en caso de serlo retornar True de lo contrario 
# retornar False. 
# Se considera una dirección IP válida si tiene el formato xxx.xxx.xxx.xxx, donde xxx es un número 
# entero entre 0 y 255.
print("=====================ej 20=================================")

if (validar_ip("255.025.255.055")==True):
    print("IP valido")
else:
    print("IP invalido")
if (validar_ip("265.025.255.055")==True):
    print("IP valido")
else:
    print("IP invalido")
if (validar_ip("255.025.265.055")==True):
    print("IP valido")
else:
    print("IP invalido")
if (validar_ip("255.025.255.665")==True):
    print("IP valido")
else:
    print("IP invalido")