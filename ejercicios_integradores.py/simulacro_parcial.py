import biblioteca_simulacro_parcial
from biblioteca_simulacro_parcial import stark_marvel_app_desafio_6
from biblioteca_simulacro_parcial import stark_menu_principal_desafio_6
from biblioteca_simulacro_parcial import abrir_archivo
personajes = abrir_archivo("/home/martin/Documentos/programacion_1/data_stark.json")
lista_personajes = personajes["heroes"]
while(stark_marvel_app_desafio_6(lista_personajes,stark_menu_principal_desafio_6()) != 0):
      pass
