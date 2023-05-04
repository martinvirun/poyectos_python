# 3 Crear una función que calcule el descuento aplicado a un producto. 
# Recibe dos parámetros (precio original y precio con descuento) y devuelve el 
# porcentaje de descuento aplicado.

def calcular_porcentaje_de_descuento(precio_original,precio_con_descuento):
  porcentaje =  100 / (precio_original / precio_con_descuento)
  return porcentaje

print(calcular_porcentaje_de_descuento(200,100))