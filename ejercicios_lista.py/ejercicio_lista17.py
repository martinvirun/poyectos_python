#crea dos listas de números y encuentra los elementos que se encuentran en ambas listas.
lista = [1,2,3,6,85]
lista_dos =[85,98,100,112]

for i in range(len(lista)):
  for index in range(len(lista_dos)):
    if (lista[i] == lista_dos[index]):
      print(lista[i])
                  
