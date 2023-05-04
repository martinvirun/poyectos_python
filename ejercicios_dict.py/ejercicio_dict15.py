# Crea un diccionario que contenga el nombre y el sueldo de varios empleados. 
# Luego, permite al usuario aumentar el sueldo de un empleado y actualizar
# el valor correspondiente en el diccionario.

dict_sueldos = {"martin":225000,"carlos":85999,"soledad":15000,"mateo":175000}
empleado = input("ingresa empleado")
sueldo = input("ingresa aumento")
sueldo_parceado = int(sueldo)
flag = False
for empl in dict_sueldos:
    if (empl == empleado):
        dict_sueldos[empl] = dict_sueldos[empl] + sueldo_parceado
        flag = True
print(dict_sueldos)
