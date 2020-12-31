# no hay un orden
# no permite python que haya duplicados
# dentro de una coleccion NO puede haber otra colección

#el set se pone para hacer referencia que vamos a crear un cojunto
conjunto = set()
conjunto = {2,"Python",True,'1',20,20}
conjunto.add(False)
conjunto.discard(2)
conjunto.discard(20)
#conjunto.clear()
print(2 not in conjunto)
print(conjunto)


