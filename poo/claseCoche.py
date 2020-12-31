class Coche:
    def __init__(self):
        self.marca = "Audi"
        self.color = "rojo"
        self.ruedas = 4
        self.enMarcha = False

    def arrancar(self, arrancamos):
        self.enMarcha = arrancamos 
        if(self.enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche se encuetra apagado"

    def __str__(self):
        return "Este auto es marca {}, de color {}, tiene {} ruedas".format(self.marca,self.color,self.ruedas)

miCoche = Coche() #instanciamos la clase
print(miCoche.arrancar(2))
print(str(miCoche))



