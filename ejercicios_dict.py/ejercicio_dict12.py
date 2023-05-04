# Crea un diccionario que represente una lista de las compras. 
# Cada clave del diccionario debe ser el nombre de un producto y cada valor debe ser su cantidad.
# Pedir al usuario que ingrese el nombre del producto e imprimir la cantidad

dict_lista_compra = {"leche":3.75,"agua":2.78,"sal":0.75,"carne":5.96,"verduras":2.05,"yerba":1.30}

producto = input("ingrese prdocuto")
flag = False

for prod in dict_lista_compra:
    if (prod == producto):
        print(dict_lista_compra[prod])
        flag = True
if(flag == False):
    print("no se encotro producto")      