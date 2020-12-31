class Coche:
    def __init__(self,marca,km,año):
        self.marca = marca
        self.km = km
        self.año = año
        print('Se ha creado un auto ', self.marca)

    def __del__(self):
        print('Se ha vendido el auto', self.marca)

    def __str__(self):
        return "El auto tiene {} km y es del año {}".format(self.km,self.año)

miCoche = Coche('Audi',2000,1993)
print(str(miCoche))
#del(miCoche)

