import pandas as pd 

datos = list (range(12))

print (datos)
print (type(datos))

pf = pd.Series(datos)

print (pf)

arreglo = pf.values
print (arreglo)
print (type (arreglo))
