#(1) Escribir una función a la que se le pase una 
#cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

def saludar(nombre):
    return "Hola {}".format(nombre)

print(saludar("Jose"))
