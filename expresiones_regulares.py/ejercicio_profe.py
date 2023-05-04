import re
texto = "QUEVEDO || BZRP Music Sessions #52 JUAN || BZRP Music Sessions #2 Q  || BZRP Music Sessions #22" 
fecha = "2022-07-06 00\\00:00"

print(re.split(r'[\\]+', fecha))     

print(re.findall(r"([a-zA-Z ]{2,})[|;]{2} BZRP Music Sessions #([0-9]+)",texto))
