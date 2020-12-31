class Coche:
    def __init__(self):
        self.__marca = "Audi"
        self.__color = "rojo"
        self.__ruedas = 4 #al poner __ (dos guines bajo) se indica que no se puede cambiar ese atributo desde el exterior
        self.__enMarcha = False

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos 
        if(self.__enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche se encuetra apagado"

    def __str__(self):
        return "Este auto es marca {}, de color {}, tiene {} ruedas".format(self.__marca,self.__color,self.__ruedas)

miCoche = Coche() #instanciamos la clase
print(miCoche.arrancar(True))
print(str(miCoche))


print("***************** OTRO VEHICULO ******************")

miCoche2 = Coche()
miCoche2.ruedas = 20 
miCoche2.marca = "Rm" 
print(miCoche2.arrancar(1))
print(str(miCoche2))



