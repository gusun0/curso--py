#clases y objetos
class Gelatina:
    #constructor que inicializa las caracteristicas
    def __init__(self,sabor,color,tamaño):
        self.sabor = sabor
        self.color = color
        self.tamaño = tamaño 

    #método
    def imprimir(self):
        print("La gelatina es de: " + self.sabor)
        print("La gelatina se ve de color: " + self.color)
        print("La gelatina es: " + self.tamaño)


#inicializamos una instancia
gel1 = Gelatina('manzana','verde','mediana')
gel2 = Gelatina('Mora','azul','pequeña')
gel3 = Gelatina('Rojo','fresa','grande')
gel4 = Gelatina('limón','verde','grande')

gel1.imprimir()
gel2.imprimir()
gel3.imprimir()
gel4.imprimir()
