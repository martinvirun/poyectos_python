

# Crea un diccionario que represente los gastos de una persona en diferentes categorías,
# donde las claves son los nombres de las categorías y los valores son los gastos correspondientes.
# Calcula el total de gastos de la persona.

dict_gastos = {"gastos comida":5000,"gastos ropa":3500,"gastos nafta":3500,"gastos plomero":7500}
gastos_totales = 0

for gasto in dict_gastos:
    gastos_totales = gastos_totales + dict_gastos[gasto]

print("el gasto total es de : ${0}".format(gastos_totales))